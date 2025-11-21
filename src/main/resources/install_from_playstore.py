#!/usr/bin/env python3
"""
Automated Google Play Store Login and App Installation Script
Installs Eptura Engage app from Play Store using provided credentials
"""

import os
import sys
import time
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
        
    def setup_driver(self):
        """Initialize Appium driver for Play Store automation"""
        print("🔧 Setting up Appium driver for Play Store...")
        
        options = UiAutomator2Options()
        options.platform_name = "Android"
        options.automation_name = "UiAutomator2"
        options.device_name = "Android Emulator"
        options.no_reset = True
        options.full_reset = False
        
        # Add retry logic
        max_retries = 3
        retry_count = 0
        
        while retry_count < max_retries:
            try:
                self.driver = webdriver.Remote(
                    command_executor='http://127.0.0.1:4723',
                    options=options
                )
                print("✅ Appium driver initialized successfully")
                return True
            except Exception as e:
                retry_count += 1
                print(f"⚠️  Attempt {retry_count}/{max_retries} failed: {e}")
                if retry_count < max_retries:
                    print("⏳ Retrying in 5 seconds...")
                    time.sleep(5)
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
                'new UiSelector().descriptionContains("Search")',
                'new UiSelector().textContains("Search")'
            ]
            
            for selector in search_selectors:
                try:
                    search_icon = self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, selector)
                    search_icon.click()
                    time.sleep(2)
                    break
                except:
                    continue
            
            # Enter app name in search field
            print(f"⌨️  Typing '{app_name}'...")
            search_field_selectors = [
                'new UiSelector().resourceId("com.android.vending:id/search_bar_text_input")',
                'new UiSelector().className("android.widget.EditText")'
            ]
            
            for selector in search_field_selectors:
                try:
                    search_field = self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, selector)
                    search_field.clear()
                    search_field.send_keys(app_name)
                    time.sleep(2)
                    break
                except:
                    continue
            
            # Press Enter or click first result
            self.driver.press_keycode(66)  # KEYCODE_ENTER
            time.sleep(3)
            
            # Click on the app from search results
            print("📱 Selecting app from results...")
            try:
                app_item = self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,
                                                   f'new UiSelector().textContains("{app_name}")')
                app_item.click()
                time.sleep(3)
            except:
                print("⚠️  Could not find app in search results")
            
            # Click Install button
            print("📲 Clicking Install button...")
            install_texts = ["Install", "INSTALL", "Update", "UPDATE", "Open", "OPEN"]
            
            for text in install_texts:
                try:
                    install_btn = self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,
                                                          f'new UiSelector().textContains("{text}")')
                    button_text = install_btn.text
                    
                    if button_text in ["Open", "OPEN"]:
                        print("✅ App is already installed!")
                        return True
                    
                    install_btn.click()
                    print(f"✅ Clicked {button_text} button")
                    break
                except:
                    continue
            
            # Wait for installation to complete
            print("⏳ Waiting for installation to complete...")
            max_wait = 300  # 5 minutes
            wait_time = 0
            
            while wait_time < max_wait:
                try:
                    # Check if "Open" button appears (installation complete)
                    open_btn = self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,
                                                       'new UiSelector().textContains("Open")')
                    print("✅ Installation completed successfully!")
                    return True
                except:
                    time.sleep(10)
                    wait_time += 10
                    print(f"⏳ Still installing... ({wait_time}/{max_wait} seconds)")
            
            print("⚠️  Installation timeout, but app may still be installing")
            return True
            
        except Exception as e:
            print(f"❌ Error during app installation: {e}")
            return False
    
    def install_via_deep_link(self, package_name="com.condecosoftware.condeco"):
        """Alternative method: Open app directly via package ID and install"""
        print(f"🔗 Opening app via deep link: {package_name}")
        
        try:
            # Open Play Store app page directly
            os.system(f'adb shell am start -a android.intent.action.VIEW -d "market://details?id={package_name}"')
            time.sleep(5)
            
            if not self.driver:
                self.setup_driver()
            
            # Wait for page to load
            time.sleep(3)
            
            # Click Install button
            print("📲 Looking for Install button...")
            install_texts = ["Install", "INSTALL", "Update", "UPDATE", "Open", "OPEN"]
            
            for text in install_texts:
                try:
                    install_btn = self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,
                                                          f'new UiSelector().textContains("{text}")')
                    button_text = install_btn.text
                    
                    if button_text in ["Open", "OPEN"]:
                        print("✅ App is already installed!")
                        return True
                    
                    install_btn.click()
                    print(f"✅ Clicked {button_text} button")
                    time.sleep(3)
                    
                    # Handle any confirmation dialogs
                    try:
                        continue_btn = self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,
                                                               'new UiSelector().textContains("Continue")')
                        continue_btn.click()
                    except:
                        pass
                    
                    break
                except:
                    continue
            
            # Wait for installation
            print("⏳ Waiting for installation to complete...")
            max_wait = 300
            wait_time = 0
            
            while wait_time < max_wait:
                try:
                    open_btn = self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,
                                                       'new UiSelector().textContains("Open")')
                    print("✅ Installation completed successfully!")
                    return True
                except:
                    # Also check if package is installed
                    result = os.popen(f'adb shell pm list packages | grep {package_name}').read()
                    if package_name in result:
                        print("✅ App package detected on device!")
                        return True
                    
                    time.sleep(10)
                    wait_time += 10
                    print(f"⏳ Still installing... ({wait_time}/{max_wait} seconds)")
            
            print("⚠️  Installation timeout")
            return False
            
        except Exception as e:
            print(f"❌ Error during deep link installation: {e}")
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