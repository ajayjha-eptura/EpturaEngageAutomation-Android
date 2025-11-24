#!/usr/bin/env python3
"""
Automated Google Play Store Login and App Installation Script
Installs Eptura Engage app from Play Store using provided credentials
Compatible with macOS and Windows CI/CD environments
Optimized for Android 15 (API 35)
"""

import os
import sys
import time
import subprocess
import platform
from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException

class PlayStoreInstaller:
    def __init__(self, email, password):
        self.email = email
        self.password = password
        self.driver = None
        self.is_macos = platform.system() == 'Darwin'
        self.is_windows = platform.system() == 'Windows'
        self.temp_dir = '/tmp' if self.is_macos else ('C:\\Temp' if self.is_windows else '/tmp')
        
        # Ensure temp directory exists on Windows
        if self.is_windows and not os.path.exists(self.temp_dir):
            try:
                os.makedirs(self.temp_dir)
            except:
                self.temp_dir = os.path.expanduser('~\\AppData\\Local\\Temp')
    
    def _run_adb_command(self, args, timeout=10):
        """Cross-platform ADB command execution"""
        try:
            # On macOS/Linux, shell=False is preferred; on Windows, use shell=True for better compatibility
            result = subprocess.run(
                ['adb'] + args,
                capture_output=True,
                text=True,
                timeout=timeout,
                shell=self.is_windows
            )
            return result
        except subprocess.TimeoutExpired:
            print(f"❌ Timeout executing ADB command: {' '.join(args)}")
            return None
        except Exception as e:
            print(f"❌ Error executing ADB command: {e}")
            return None
    
    def check_emulator_ready(self):
        """Verify emulator is fully booted and services are ready"""
        print("🔍 Verifying emulator readiness...")
        
        # Check if device is connected
        result = self._run_adb_command(['devices'])
        if not result or 'emulator' not in result.stdout:
            print("❌ No emulator device found")
            return False
        
        # Check boot completed
        result = self._run_adb_command(['shell', 'getprop', 'sys.boot_completed'])
        if not result or '1' not in result.stdout:
            print("❌ Emulator boot not completed")
            return False
        
        # Check Android version (API 35 for Android 15)
        result = self._run_adb_command(['shell', 'getprop', 'ro.build.version.sdk'])
        if result:
            api_level = result.stdout.strip()
            print(f"📱 Android API Level: {api_level}")
            if api_level == '35':
                print("✅ Running Android 15 (API 35)")
        
        # Check package manager service with platform-appropriate timeout
        result = self._run_adb_command(['shell', 'pm', 'list', 'packages'], timeout=20)
        if not result or result.returncode != 0:
            print("❌ Package manager service not ready")
            return False
        
        print("✅ Emulator is ready")
        return True
    
    def wait_for_emulator_ready(self, max_wait=180):
        """Wait for emulator to be fully ready with all services"""
        print(f"⏳ Waiting for emulator to be fully ready (max {max_wait}s)...")
        
        start_time = time.time()
        while time.time() - start_time < max_wait:
            if self.check_emulator_ready():
                # Additional wait for stability - macOS typically faster than Windows
                stability_wait = 8 if self.is_macos else (15 if self.is_windows else 10)
                print(f"⏳ Waiting {stability_wait} seconds for system stability...")
                time.sleep(stability_wait)
                return True
            
            elapsed = int(time.time() - start_time)
            if elapsed % 15 == 0:
                print(f"  Still waiting... ({elapsed}/{max_wait}s)")
            
            time.sleep(5)
        
        print(f"❌ Emulator not ready after {max_wait} seconds")
        return False
        
    def setup_driver(self):
        """Initialize Appium driver for Play Store automation
        Optimized for macOS and Android 15"""
        print("🔧 Setting up Appium driver for Play Store...")
        print(f"🖥️  Platform: {platform.system()}")
        
        # First ensure emulator is ready
        if not self.wait_for_emulator_ready():
            print("⚠️  Proceeding anyway, but may encounter issues...")
        
        options = UiAutomator2Options()
        options.platform_name = "Android"
        options.automation_name = "UiAutomator2"
        options.device_name = "Android Emulator"
        options.no_reset = True
        options.full_reset = False
        # Timeouts optimized for macOS environment (typically faster than Windows)
        options.new_command_timeout = 600
        options.adb_exec_timeout = 100000
        options.uiautomator2_server_launch_timeout = 60000
        options.uiautomator2_server_install_timeout = 60000
        
        # Android 15 specific settings
        options.skip_server_installation = False
        options.skip_device_initialization = False
        
        # Add retry logic
        max_retries = 3
        retry_count = 0
        
        while retry_count < max_retries:
            try:
                print(f"  Attempt {retry_count + 1}/{max_retries}...")
                self.driver = webdriver.Remote(
                    command_executor='http://127.0.0.1:4723',
                    options=options
                )
                print("✅ Appium driver initialized successfully")
                # Give it a moment to settle - macOS typically faster
                time.sleep(3 if self.is_macos else (5 if self.is_windows else 3))
                return True
            except Exception as e:
                retry_count += 1
                print(f"⚠️  Attempt {retry_count}/{max_retries} failed: {e}")
                if retry_count < max_retries:
                    wait_time = 15 * retry_count  # Standard backoff
                    print(f"⏳ Retrying in {wait_time} seconds...")
                    time.sleep(wait_time)
                else:
                    print(f"❌ Failed to initialize Appium driver after {max_retries} attempts")
                    return False
    
    def wait_and_click(self, locator_type, locator_value, timeout=30):
        """Wait for element and click it"""
        try:
            element = WebDriverWait(self.driver, timeout).until(
                EC.element_to_be_clickable((locator_type, locator_value))
            )
            element.click()
            return True
        except TimeoutException:
            print(f"⚠️  Timeout waiting for element: {locator_value}")
            return False
        except Exception as e:
            print(f"⚠️  Error clicking element: {e}")
            return False
    
    def wait_and_send_keys(self, locator_type, locator_value, text, timeout=30):
        """Wait for element and send keys to it"""
        try:
            element = WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located((locator_type, locator_value))
            )
            element.clear()
            element.send_keys(text)
            return True
        except TimeoutException:
            print(f"⚠️  Timeout waiting for element: {locator_value}")
            return False
        except Exception as e:
            print(f"⚠️  Error sending keys: {e}")
            return False
    
    def open_play_store(self):
        """Open Google Play Store app"""
        print("🏪 Opening Google Play Store...")
        try:
            os.system('adb shell am start -n com.android.vending/com.android.vending.AssetBrowserActivity')
            time.sleep(5)
            print("✅ Play Store opened")
            return True
        except Exception as e:
            print(f"❌ Failed to open Play Store: {e}")
            return False
    
    def login_to_google_account(self):
        """Automate Google account login in Play Store"""
        print("🔐 Attempting to login to Google account...")
        
        try:
            # Check if already logged in
            time.sleep(3)
            
            # Look for common "Sign in" or "Add account" buttons
            sign_in_texts = [
                "Sign in",
                "Add account",
                "GET STARTED",
                "Use another account"
            ]
            
            signed_in = True
            for text in sign_in_texts:
                try:
                    if self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 
                                               f'new UiSelector().textContains("{text}")'):
                        signed_in = False
                        break
                except:
                    continue
            
            if signed_in:
                print("✅ Already logged in to Google account")
                return True
            
            # Click on Sign In button
            print("📝 Clicking Sign In...")
            sign_in_clicked = False
            for text in sign_in_texts:
                try:
                    element = self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,
                                                      f'new UiSelector().textContains("{text}")')
                    element.click()
                    sign_in_clicked = True
                    time.sleep(3)
                    break
                except:
                    continue
            
            if not sign_in_clicked:
                print("⚠️  Could not find Sign In button, may already be logged in")
                return True
            
            # Enter email
            print(f"📧 Entering email: {self.email}")
            email_selectors = [
                'new UiSelector().resourceId("identifierId")',
                'new UiSelector().className("android.widget.EditText")',
                'new UiSelector().textContains("Email")'
            ]
            
            email_entered = False
            for selector in email_selectors:
                try:
                    email_field = self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, selector)
                    email_field.clear()
                    email_field.send_keys(self.email)
                    email_entered = True
                    break
                except:
                    continue
            
            if not email_entered:
                print("❌ Could not find email input field")
                return False
            
            time.sleep(2)
            
            # Click Next button
            print("➡️  Clicking Next...")
            next_texts = ["Next", "NEXT", "Continue", "CONTINUE"]
            for text in next_texts:
                try:
                    next_btn = self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,
                                                       f'new UiSelector().textContains("{text}")')
                    next_btn.click()
                    break
                except:
                    continue
            
            time.sleep(3)
            
            # Enter password
            print("🔑 Entering password...")
            password_selectors = [
                'new UiSelector().resourceId("password")',
                'new UiSelector().className("android.widget.EditText")',
                'new UiSelector().textContains("password")'
            ]
            
            password_entered = False
            for selector in password_selectors:
                try:
                    password_field = self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, selector)
                    password_field.clear()
                    password_field.send_keys(self.password)
                    password_entered = True
                    break
                except:
                    continue
            
            if not password_entered:
                print("❌ Could not find password input field")
                return False
            
            time.sleep(2)
            
            # Click Next/Sign in button
            print("➡️  Clicking Sign In...")
            for text in next_texts:
                try:
                    sign_in_btn = self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,
                                                          f'new UiSelector().textContains("{text}")')
                    sign_in_btn.click()
                    break
                except:
                    continue
            
            # Wait for login to complete
            time.sleep(10)
            
            # Handle post-login prompts (Skip, Not now, etc.)
            skip_texts = ["Skip", "SKIP", "Not now", "NO THANKS", "Accept"]
            for _ in range(3):  # Try multiple times for different prompts
                for text in skip_texts:
                    try:
                        skip_btn = self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,
                                                           f'new UiSelector().textContains("{text}")')
                        skip_btn.click()
                        time.sleep(2)
                    except:
                        continue
            
            print("✅ Login process completed")
            return True
            
        except Exception as e:
            print(f"❌ Error during login: {e}")
            return False
    
    def search_and_install_app(self, app_name="Eptura Engage"):
        """Search for app and install it"""
        print(f"🔍 Searching for app: {app_name}")
        
        try:
            # Click on search icon
            print("🔎 Opening search...")
            search_selectors = [
                'new UiSelector().resourceId("com.android.vending:id/search_bar_hint")',
                'new UiSelector().resourceId("com.android.vending:id/search_box_idle_text")',
                'new UiSelector().descriptionContains("Search")',
                'new UiSelector().textContains("Search")',
                'new UiSelector().className("android.widget.EditText")'
            ]
            
            search_opened = False
            for selector in search_selectors:
                try:
                    search_icon = self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, selector)
                    search_icon.click()
                    time.sleep(3)
                    search_opened = True
                    print(f"✅ Search opened using selector: {selector[:50]}...")
                    break
                except:
                    continue
            
            if not search_opened:
                print("⚠️  Could not open search, trying to proceed anyway")
            
            # Enter app name in search field
            print(f"⌨️  Typing '{app_name}'...")
            search_field_selectors = [
                'new UiSelector().resourceId("com.android.vending:id/search_bar_text_input")',
                'new UiSelector().resourceId("com.android.vending:id/search_box_text_input")',
                'new UiSelector().className("android.widget.EditText")',
                'new UiSelector().focused(true)'
            ]
            
            text_entered = False
            for selector in search_field_selectors:
                try:
                    search_field = self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, selector)
                    search_field.clear()
                    time.sleep(1)
                    search_field.send_keys(app_name)
                    text_entered = True
                    print(f"✅ Text entered successfully")
                    time.sleep(2)
                    break
                except Exception as e:
                    continue
            
            if not text_entered:
                print("❌ Could not enter search text")
                return False
            
            # Press Enter or click search button
            try:
                self.driver.press_keycode(66)  # KEYCODE_ENTER
                print("✅ Pressed Enter key")
                time.sleep(5)  # Wait for search results
            except:
                print("⚠️  Could not press Enter key")
            
            # Click on the app from search results
            print("📱 Selecting app from results...")
            app_clicked = False
            
            # Try multiple ways to find and click the app
            app_selectors = [
                f'new UiSelector().textContains("{app_name}")',
                f'new UiSelector().descriptionContains("{app_name}")',
                'new UiSelector().textContains("Eptura")',
                'new UiSelector().textContains("Condeco")',
                'new UiSelector().resourceId("com.android.vending:id/li_title")'
            ]
            
            for selector in app_selectors:
                try:
                    app_item = self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, selector)
                    app_item.click()
                    print(f"✅ App clicked using selector: {selector[:50]}...")
                    time.sleep(5)
                    app_clicked = True
                    break
                except:
                    continue
            
            if not app_clicked:
                print("⚠️  Could not find app in search results, trying to continue anyway")
            
            # Click Install button - try multiple times with different selectors
            print("📲 Looking for Install button...")
            install_clicked = False
            install_texts = ["Install", "INSTALL", "Update", "UPDATE", "Open", "OPEN", "Get"]
            
            for attempt in range(3):  # Try 3 times
                for text in install_texts:
                    try:
                        install_btn = self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,
                                                              f'new UiSelector().textContains("{text}").className("android.widget.Button")')
                        button_text = install_btn.text
                        
                        if button_text.upper() in ["OPEN"]:
                            print("✅ App is already installed!")
                            return True
                        
                        install_btn.click()
                        print(f"✅ Clicked '{button_text}' button")
                        install_clicked = True
                        time.sleep(3)
                        
                        # Handle any confirmation dialogs
                        try:
                            continue_selectors = [
                                'new UiSelector().textContains("Continue")',
                                'new UiSelector().textContains("Accept")',
                                'new UiSelector().textContains("OK")'
                            ]
                            for selector in continue_selectors:
                                try:
                                    confirm_btn = self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, selector)
                                    confirm_btn.click()
                                    print("✅ Confirmed installation")
                                    time.sleep(2)
                                except:
                                    pass
                        except:
                            pass
                        
                        break
                    except:
                        continue
                
                if install_clicked:
                    break
                    
                if attempt < 2:
                    print(f"⏳ Retrying... (attempt {attempt + 2}/3)")
                    time.sleep(3)
            
            if not install_clicked:
                print("❌ Could not find or click Install button")
                return False
            
            # Wait for installation to complete with better verification
            print("⏳ Waiting for installation to complete...")
            print("   Checking both UI and package manager...")
            max_wait = 300  # 5 minutes
            wait_time = 0
            check_interval = 10
            
            while wait_time < max_wait:
                # Method 1: Check for "Open" button in UI
                try:
                    open_btn = self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,
                                                       'new UiSelector().text("Open").className("android.widget.Button")')
                    print("✅ Installation completed successfully (Open button found)!")
                    return True
                except:
                    pass
                
                # Method 2: Check package manager directly
                try:
                    import subprocess
                    result = subprocess.run(['adb', 'shell', 'pm', 'list', 'packages', 'com.condecosoftware.condeco'],
                                          capture_output=True, text=True, timeout=5)
                    if 'com.condecosoftware.condeco' in result.stdout:
                        print("✅ Installation completed successfully (package detected)!")
                        return True
                except:
                    pass
                
                time.sleep(check_interval)
                wait_time += check_interval
                
                if wait_time % 30 == 0:
                    print(f"⏳ Still installing... ({wait_time}/{max_wait} seconds)")
            
            print("❌ Installation timeout - app was not installed")
            return False
            
        except Exception as e:
            print(f"❌ Error during app installation: {e}")
            return False
    
    def install_via_deep_link(self, package_name="com.condecosoftware.condeco"):
        """Alternative method: Open app directly via package ID and install
        Optimized for macOS and Android 15"""
        print(f"🔗 Opening app via deep link: {package_name}")
        
        try:
            # Open Play Store app page directly - cross-platform compatible
            result = self._run_adb_command([
                'shell', 'am', 'start', '-a', 'android.intent.action.VIEW',
                '-d', f'market://details?id={package_name}'
            ], timeout=15)
            
            if not result or result.returncode != 0:
                print("⚠️  Failed to open Play Store via deep link")
                return False
            
            # macOS typically has faster response times
            time.sleep(8 if self.is_macos else (10 if self.is_windows else 8))
            
            if not self.driver:
                if not self.setup_driver():
                    print("❌ Could not setup driver")
                    return False
            
            # Wait for page to load - macOS is typically faster
            print("⏳ Waiting for Play Store page to load...")
            time.sleep(5 if self.is_macos else (8 if self.is_windows else 5))
            
            # Click Install button - try multiple times
            print("📲 Looking for Install button...")
            install_clicked = False
            install_texts = ["Install", "INSTALL", "Update", "UPDATE", "Open", "OPEN", "Get"]
            
            # Standard attempts for macOS (should be more responsive)
            max_attempts = 5 if self.is_macos else (7 if self.is_windows else 5)
            
            for attempt in range(max_attempts):
                for text in install_texts:
                    try:
                        # Try with multiple selector strategies
                        selectors = [
                            f'new UiSelector().text("{text}").className("android.widget.Button")',
                            f'new UiSelector().textContains("{text}")',
                            f'new UiSelector().description("{text}")'
                        ]
                        
                        for selector in selectors:
                            try:
                                install_btn = self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, selector)
                                button_text = install_btn.text if hasattr(install_btn, 'text') else text
                                
                                if button_text.upper() in ["OPEN"]:
                                    print("✅ App is already installed!")
                                    return True
                                
                                # Get button location and click
                                install_btn.click()
                                print(f"✅ Clicked '{button_text}' button (attempt {attempt + 1})")
                                install_clicked = True
                                time.sleep(3)
                                
                                # Handle any confirmation dialogs
                                confirm_texts = ["Continue", "Accept", "OK", "Agree"]
                                for confirm_text in confirm_texts:
                                    try:
                                        confirm_btn = self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,
                                                                              f'new UiSelector().textContains("{confirm_text}")')
                                        confirm_btn.click()
                                        print(f"✅ Confirmed with '{confirm_text}'")
                                        time.sleep(2)
                                    except:
                                        pass
                                
                                break
                            except:
                                continue
                        
                        if install_clicked:
                            break
                    except:
                        continue
                
                if install_clicked:
                    break
                
                if attempt < max_attempts - 1:
                    # Standard retry wait
                    wait_time = 5
                    print(f"⏳ Waiting before retry... (attempt {attempt + 2}/{max_attempts})")
                    time.sleep(wait_time)
            
            if not install_clicked:
                print(f"❌ Could not find or click Install button after {max_attempts} attempts")
                return False
            
            # Wait for installation with dual verification
            print("⏳ Waiting for installation to complete...")
            print("   Monitoring both Play Store UI and package manager...")
            # macOS typically faster, so shorter timeout
            max_wait = 360 if self.is_macos else (420 if self.is_windows else 360)  # 6 min on macOS, 7 min on Windows
            wait_time = 0
            check_interval = 10
            last_status = ""
            
            while wait_time < max_wait:
                # Check UI for completion
                try:
                    open_btn = self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,
                                                       'new UiSelector().text("Open").className("android.widget.Button")')
                    print("✅ Installation completed successfully (Open button appeared)!")
                    return True
                except:
                    pass
                
                # Check for progress indicators
                try:
                    progress_selectors = [
                        'new UiSelector().textContains("Installing")',
                        'new UiSelector().textContains("Downloading")',
                        'new UiSelector().textContains("%")',
                        'new UiSelector().resourceId("com.android.vending:id/progress_bar")'
                    ]
                    
                    for selector in progress_selectors:
                        try:
                            progress_elem = self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, selector)
                            status_text = progress_elem.text if hasattr(progress_elem, 'text') else "In progress"
                            if status_text != last_status:
                                print(f"📥 Status: {status_text}")
                                last_status = status_text
                            break
                        except:
                            continue
                except:
                    pass
                
                # Check package manager
                result = self._run_adb_command(['shell', 'pm', 'list', 'packages'], timeout=10)
                if result and package_name in result.stdout:
                    print("✅ App package detected on device!")
                    time.sleep(5)
                    return True
                
                time.sleep(check_interval)
                wait_time += check_interval
                
                if wait_time % 30 == 0:
                    print(f"⏳ Still waiting... ({wait_time}/{max_wait} seconds)")
            
            # Final verification
            print("⏳ Performing final verification...")
            time.sleep(10)
            
            result = self._run_adb_command(['shell', 'pm', 'list', 'packages', package_name], timeout=10)
            if result and package_name in result.stdout:
                print("✅ Installation verified via package manager!")
                return True
            
            print("❌ Installation timeout - app was not installed")
            return False
            
        except Exception as e:
            print(f"❌ Error during deep link installation: {e}")
            import traceback
            traceback.print_exc()
            return False
    
    def cleanup(self):
        """Clean up resources"""
        if self.driver:
            try:
                self.driver.quit()
                print("✅ Appium driver closed")
            except:
                pass


def main():
    """Main execution function"""
    print("=" * 60)
    print("🏪 Google Play Store Automated Installer")
    print(f"🖥️  Platform: {platform.system()}")
    print(f"🤖 Optimized for Android 15 (API 35)")
    print("=" * 60)
    
    # Get credentials from command-line arguments or environment variables
    if len(sys.argv) >= 3:
        email = sys.argv[1]
        password = sys.argv[2]
        app_name = sys.argv[3] if len(sys.argv) >= 4 else "Eptura Engage"
        print("📋 Using credentials from command-line arguments")
    else:
        email = os.environ.get('GOOGLE_EMAIL', '')
        password = os.environ.get('GOOGLE_PASSWORD', '')
        app_name = os.environ.get('APP_NAME', 'Eptura Engage')
        print("📋 Using credentials from environment variables")
    
    if not email or not password:
        print("\n❌ ERROR: Google credentials not provided!")
        print("\nUsage:")
        print("  python3 install_from_playstore.py <email> <password> [app_name]")
        print("\nOR set environment variables:")
        print("  export GOOGLE_EMAIL='your@email.com'")
        print("  export GOOGLE_PASSWORD='yourpassword'")
        print("  export APP_NAME='Eptura Engage'")
        sys.exit(1)
    
    print(f"📧 Email: {email[:2]}***@***")
    print(f"📱 App: {app_name}")
    
    installer = PlayStoreInstaller(email, password)
    
    try:
        # Method 1: Direct deep link installation (faster, doesn't require login)
        print("\n📍 Method 1: Trying direct deep link installation...")
        if installer.install_via_deep_link("com.condecosoftware.condeco"):
            print("\n✅ Installation successful!")
            return 0
        
        # Method 2: Full automation with search (requires login)
        print("\n📍 Method 2: Trying full Play Store automation...")
        if not installer.setup_driver():
            print("❌ Failed to setup Appium driver")
            return 1
        
        if not installer.open_play_store():
            print("❌ Failed to open Play Store")
            return 1
        
        # Try to login (may already be logged in)
        installer.login_to_google_account()
        
        # Search and install app
        if installer.search_and_install_app(app_name):
            print("\n✅ Installation successful!")
            return 0
        else:
            print("\n⚠️  Installation may not have completed")
            return 1
            
    except Exception as e:
        print(f"\n❌ Unexpected error: {e}")
        import traceback
        traceback.print_exc()
        return 1
    finally:
        installer.cleanup()


if __name__ == "__main__":
    sys.exit(main())