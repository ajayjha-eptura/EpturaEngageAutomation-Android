#!/usr/bin/env python3
"""
Automated Google Play Store App Installation Script
Installs Eptura Engage app from Play Store when user is already logged in
Compatible with macOS and Windows CI/CD environments
Optimized for Android 15 (API 35)
"""

import os
import sys
import time
import subprocess
import platform
import requests
from datetime import datetime
from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException

class PlayStoreInstaller:
    def __init__(self):
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
        # Setup screenshot directory
        self.setup_screenshot_directory()

    def setup_screenshot_directory(self):
        """Setup directory for storing screenshots"""
        try:
            workspace_dir = os.getcwd()
            screenshot_dir = os.path.join(workspace_dir, 'playstore_screenshots')
            if not os.path.exists(screenshot_dir):
                os.makedirs(screenshot_dir)
            self.screenshot_dir = screenshot_dir
            print(f"📸 Debug screenshots will be saved to: {screenshot_dir}")
        except Exception as e:
            print(f"⚠️  Could not create screenshot directory: {e}")
            self.screenshot_dir = self.temp_dir

    def take_screenshot(self, name_prefix="debug"):
        """Take a screenshot and save to screenshot directory"""
        if not self.driver:
            print("⚠️  No Appium driver available for screenshot")
            return None
        try:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"{name_prefix}_{timestamp}.png"
            filepath = os.path.join(self.screenshot_dir, filename)
            self.driver.save_screenshot(filepath)
            print(f"📸 Screenshot saved: {filepath}")
            return filepath
        except Exception as e:
            print(f"⚠️  Could not take screenshot: {e}")
            return None

    def _run_adb_command(self, args, timeout=10):
        """Cross-platform ADB command execution"""
        try:
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

    def print_device_info(self):
        """Prints Android version, API level, and device model"""
        try:
            api_result = self._run_adb_command(['shell', 'getprop', 'ro.build.version.sdk'])
            version_result = self._run_adb_command(['shell', 'getprop', 'ro.build.version.release'])
            model_result = self._run_adb_command(['shell', 'getprop', 'ro.product.model'])
            api_level = api_result.stdout.strip() if api_result else 'Unknown'
            android_version = version_result.stdout.strip() if version_result else 'Unknown'
            device_model = model_result.stdout.strip() if model_result else 'Unknown'
            print("\n================ DEVICE INFO ================")
            print(f"📱 Device Model: {device_model}")
            print(f"🤖 Android Version: {android_version}")
            print(f"🔢 API Level: {api_level}")
            print("============================================\n")
        except Exception as e:
            print(f"⚠️  Could not fetch device info: {e}")
    
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
    
    def recover_emulator_adb_connection(self, max_retries=5, wait_per_retry=10):
        """Attempt to recover emulator from offline ADB state."""
        print("\n================ ADB/EMULATOR RECOVERY ================")
        for attempt in range(max_retries):
            result = self._run_adb_command(['devices'])
            if result and 'emulator' in result.stdout and 'offline' not in result.stdout:
                print(f"✅ Emulator is online (attempt {attempt+1})")
                return True
            print(f"⚠️  Emulator offline (attempt {attempt+1}/{max_retries}), restarting ADB server...")
            self._run_adb_command(['kill-server'])
            time.sleep(2)
            self._run_adb_command(['start-server'])
            time.sleep(wait_per_retry)
        # Final check
        result = self._run_adb_command(['devices'])
        if result and 'emulator' in result.stdout and 'offline' not in result.stdout:
            print("✅ Emulator is online after recovery attempts.")
            return True
        print("❌ Emulator remains offline after recovery attempts.")
        return False

    def wait_for_emulator_ready(self, max_wait=180):
        """Wait for emulator to be fully ready with all services"""
        print(f"⏳ Waiting for emulator to be fully ready (max {max_wait}s)...")
        self.recover_emulator_adb_connection()
        start_time = time.time()
        while time.time() - start_time < max_wait:
            if self.check_emulator_ready():
                stability_wait = 8 if self.is_macos else (15 if self.is_windows else 10)
                print(f"⏳ Waiting {stability_wait} seconds for system stability...")
                time.sleep(stability_wait)
                return True
            elapsed = int(time.time() - start_time)
            if elapsed % 15 == 0:
                print(f"  Still waiting... ({elapsed}/{max_wait}s)")
            self.recover_emulator_adb_connection()
            time.sleep(5)
        print(f"❌ Emulator not ready after {max_wait} seconds")
        return False
        
    def check_appium_server(self, url='http://127.0.0.1:4723/status', timeout=10):
        """Check if Appium server is available before driver setup"""
        try:
            response = requests.get(url, timeout=timeout)
            if response.status_code == 200:
                print(f"✅ Appium server is available at {url}")
                return True
            else:
                print(f"❌ Appium server responded with status {response.status_code}")
                return False
        except Exception as e:
            print(f"❌ Could not connect to Appium server at {url}: {e}")
            return False
    
    def setup_driver(self):
        """Initialize Appium driver for Play Store automation"""
        print("🔧 Setting up Appium driver for Play Store...")
        print(f"🖥️  Platform: {platform.system()}")
        
        if not self.check_appium_server():
            print("❌ Appium server is not available. Exiting.")
            sys.exit(1)
        
        if not self.wait_for_emulator_ready():
            print("⚠️  Proceeding anyway, but may encounter issues...")
        
        print("🔍 Checking for pre-installed Appium APKs...")
        appium_apks_installed = self._check_appium_apks_installed()
        
        options = UiAutomator2Options()
        options.platform_name = "Android"
        options.automation_name = "UiAutomator2"
        options.device_name = "Android Emulator"
        options.no_reset = True
        options.full_reset = False
        options.new_command_timeout = 600
        options.adb_exec_timeout = 240000
        options.uiautomator2_server_launch_timeout = 120000
        options.uiautomator2_server_install_timeout = 180000
        
        if appium_apks_installed:
            print("✅ Appium APKs already installed, skipping installation step")
            options.skip_server_installation = True
            options.skip_device_initialization = True
        else:
            print("⚠️  Appium APKs not pre-installed, will install during initialization")
            options.skip_server_installation = False
            options.skip_device_initialization = False
        
        print("🔧 Pre-flight check: Testing package manager responsiveness...")
        for attempt in range(3):
            result = self._run_adb_command(['shell', 'pm', 'list', 'packages', '-s'], timeout=30)
            if result and result.returncode == 0:
                print(f"✅ Package manager responsive (attempt {attempt + 1})")
                break
            print(f"⚠️  Package manager slow, waiting... (attempt {attempt + 1}/3)")
            time.sleep(10)
        
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
                time.sleep(3 if self.is_macos else (5 if self.is_windows else 3))
                return True
            except Exception as e:
                retry_count += 1
                print(f"⚠️  Attempt {retry_count}/{max_retries} failed: {e}")
                import traceback
                traceback.print_exc()
                
                if 'timed out' in str(e).lower() and 'install' in str(e).lower():
                    print("💡 APK installation timeout detected - emulator is too slow")
                    print("   This usually resolves after emulator warms up")
                    if appium_apks_installed and retry_count < max_retries:
                        print("   Disabling skip_server_installation for next attempt...")
                        options.skip_server_installation = False
                        options.skip_device_initialization = False
                
                if retry_count < max_retries:
                    wait_time = 30 * retry_count
                    print(f"⏳ Retrying in {wait_time} seconds...")
                    if retry_count == 1:
                        print("   Allowing emulator to stabilize...")
                        self._run_adb_command(['shell', 'settings', 'get', 'global', 'animator_duration_scale'], timeout=10)
                    time.sleep(wait_time)
                else:
                    print(f"❌ Failed to initialize Appium driver after {max_retries} attempts")
                    sys.exit(1)
    
    def _check_appium_apks_installed(self):
        """Check if Appium UiAutomator2 APKs are already installed on the device"""
        try:
            required_packages = [
                'io.appium.uiautomator2.server',
                'io.appium.uiautomator2.server.test',
                'io.appium.settings'
            ]
            
            result = self._run_adb_command(['shell', 'pm', 'list', 'packages'], timeout=20)
            if not result or result.returncode != 0:
                return False
            
            packages_output = result.stdout
            installed_count = 0
            
            for package in required_packages:
                if package in packages_output:
                    installed_count += 1
                    print(f"   ✅ Found: {package}")
                else:
                    print(f"   ❌ Missing: {package}")
            
            if installed_count == len(required_packages):
                print(f"✅ All {len(required_packages)} Appium APKs are pre-installed")
                return True
            else:
                print(f"⚠️  Only {installed_count}/{len(required_packages)} Appium APKs found")
                return False
                
        except Exception as e:
            print(f"⚠️  Error checking Appium APKs: {e}")
            return False
    
    def _handle_app_crash_dialog(self):
        """Handle and dismiss app crash dialogs if present"""
        try:
            crash_texts = ["Close", "CLOSE", "OK", "Restart", "RESTART"]
            for text in crash_texts:
                try:
                    crash_btn = self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,
                                                        f'new UiSelector().textContains("{text}")')
                    try:
                        self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,
                                                'new UiSelector().textContains("error")')
                        crash_btn.click()
                        print(f"   ✅ Dismissed crash dialog with '{text}' button")
                        return True
                    except:
                        pass
                except:
                    pass
            return False
        except Exception as e:
            return False
    
    def open_play_store(self):
        """Open Google Play Store app"""
        print("🏪 Opening Google Play Store...")
        try:
            # Method 1: Open main Play Store activity (most reliable)
            result = self._run_adb_command([
                'shell', 'am', 'start', '-n', 
                'com.android.vending/.AssetBrowserActivity'
            ], timeout=10)
            
            if not result or result.returncode != 0:
                print("   ⚠️  AssetBrowserActivity failed, trying MainActivity...")
                result = self._run_adb_command([
                    'shell', 'am', 'start', '-n',
                    'com.android.vending/com.google.android.finsky.activities.MainActivity'
                ], timeout=10)
            
            if not result or result.returncode != 0:
                print("   ⚠️  Explicit activities failed, trying launch intent...")
                result = self._run_adb_command([
                    'shell', 'am', 'start', '-a', 'android.intent.action.MAIN',
                    '-c', 'android.intent.category.LAUNCHER',
                    '-n', 'com.android.vending/com.android.vending.AssetBrowserActivity'
                ], timeout=10)
            
            if not result or result.returncode != 0:
                print("   ⚠️  All activities failed, trying package launch...")
                result = self._run_adb_command([
                    'shell', 'monkey', '-p', 'com.android.vending', '-c',
                    'android.intent.category.LAUNCHER', '1'
                ], timeout=10)
            
            time.sleep(5)
            
            if result and result.returncode == 0:
                print("✅ Play Store opened")
                return True
            else:
                print("❌ Failed to open Play Store")
                if result:
                    print(f"   Error output: {result.stderr}")
                return False
                
        except Exception as e:
            print(f"❌ Failed to open Play Store: {e}")
            return False
    
    def _search_app_in_playstore(self, app_name, max_retries=3):
        """
        Search for the app in Play Store and click on it.
        Assumes user is already logged in to Google Play Store.
        """
        search_selectors = [
            ('search_bar_hint', 'new UiSelector().resourceId("com.android.vending:id/search_bar_hint")'),
            ('search_box_idle_text', 'new UiSelector().resourceId("com.android.vending:id/search_box_idle_text")'),
            ('Search description', 'new UiSelector().descriptionContains("Search")'),
        ]
        search_field_selectors = [
            ('search_bar_text_input', 'new UiSelector().resourceId("com.android.vending:id/search_bar_text_input")'),
            ('EditText class', 'new UiSelector().className("android.widget.EditText")'),
        ]
        search_patterns = [app_name, "Eptura", "Condeco"]
        
        for attempt in range(max_retries):
            print(f"\n🔍 [Search Attempt {attempt+1}/{max_retries}] for '{app_name}'")
            self.take_screenshot(f"search_attempt_{attempt+1}_start")
            
            # 1. Open search box
            search_box_opened = False
            for selector_name, selector in search_selectors:
                try:
                    search_icon = self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, selector)
                    search_icon.click()
                    print(f"   ✅ Search box opened using: {selector_name}")
                    time.sleep(2)
                    search_box_opened = True
                    break
                except Exception as e:
                    print(f"   ⚠️  Could not open search box with {selector_name}: {e}")
            
            if not search_box_opened:
                print("   ❌ Could not open search box. Retrying after relaunch...")
                self.take_screenshot(f"search_box_failed_{attempt+1}")
                self._run_adb_command(['shell', 'am', 'force-stop', 'com.android.vending'])
                time.sleep(2)
                self.open_play_store()
                time.sleep(5)
                continue
            
            # 2. Enter app name and verify
            text_entered = False
            for selector_name, selector in search_field_selectors:
                try:
                    search_field = self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, selector)
                    search_field.clear()
                    time.sleep(1)
                    search_field.send_keys(app_name)
                    time.sleep(2)
                    entered_text = getattr(search_field, 'text', None)
                    if entered_text and app_name.lower() in entered_text.lower():
                        print(f"   ✅ Verified text entry: '{entered_text}'")
                        text_entered = True
                        break
                    else:
                        print(f"   ⚠️  Text entry not verified. Field value: '{entered_text}'")
                except Exception as e:
                    print(f"   ⚠️  Could not enter text with {selector_name}: {e}")
            
            self.take_screenshot(f"search_text_entered_{attempt+1}")
            
            if not text_entered:
                print("   ❌ Could not type or verify search text. Retrying after relaunch...")
                self._run_adb_command(['shell', 'am', 'force-stop', 'com.android.vending'])
                time.sleep(2)
                self.open_play_store()
                time.sleep(5)
                continue
            
            # 3. Trigger search
            search_triggered = False
            try:
                self.driver.press_keycode(66)  # KEYCODE_ENTER
                print("   ✅ Search triggered via Appium KEYCODE_ENTER")
                search_triggered = True
            except Exception as e:
                print(f"   ⚠️  Could not trigger search via Appium: {e}")
                try:
                    self._run_adb_command(['shell', 'input', 'keyevent', 'KEYCODE_ENTER'])
                    print("   ✅ Search triggered via ADB keyevent")
                    search_triggered = True
                except:
                    pass
            
            self.take_screenshot(f"search_triggered_{attempt+1}")
            time.sleep(5)
            
            # 4. Check for app in results
            app_found = False
            for pattern in search_patterns:
                try:
                    elements = self.driver.find_elements(AppiumBy.ANDROID_UIAUTOMATOR,
                        f'new UiSelector().textContains("{pattern}")')
                    if elements:
                        first_element = elements[0]
                        element_text = getattr(first_element, 'text', pattern)
                        print(f"   🖱️  Clicking: '{element_text}'")
                        first_element.click()
                        app_found = True
                        time.sleep(3)
                        print(f"   ✅ Found and clicked app: {pattern}")
                        self.take_screenshot(f"search_success_{attempt+1}")
                        return True
                except Exception as e:
                    print(f"   ⚠️  Could not find/click app with pattern '{pattern}': {e}")
            
            if not app_found:
                print(f"   ❌ App not found in results (attempt {attempt+1}). Killing Play Store and retrying...")
                self.take_screenshot(f"search_app_not_found_{attempt+1}")
                self._run_adb_command(['shell', 'am', 'force-stop', 'com.android.vending'])
                time.sleep(2)
                self.open_play_store()
                time.sleep(5)
        
        print(f"   ❌ Failed to find and click app after {max_retries} attempts.")
        self.take_screenshot("search_final_failure")
        return False
    
    def _install_app_from_playstore(self, package_name="com.condecosoftware.condeco", max_attempts=5):
        """
        Click Install button and wait for installation to complete
        """
        print(f"📲 Looking for Install button...")
        install_texts = ["Install", "INSTALL", "Update", "UPDATE", "Get"]
        
        for attempt in range(max_attempts):
            if self._handle_app_crash_dialog():
                print("   🔧 Handled crash, continuing...")
                time.sleep(3)
            
            for text in install_texts:
                try:
                    install_btn = self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,
                        f'new UiSelector().textContains("{text}")')
                    
                    button_text = getattr(install_btn, 'text', text)
                    
                    if button_text.upper() in ["OPEN"]:
                        print(f"   ✅ App already installed!")
                        return True
                    
                    print(f"   🔍 Found '{button_text}' button")
                    install_btn.click()
                    print(f"   ✅ Clicked '{button_text}' button")
                    time.sleep(2)
                    return True
                    
                except:
                    continue
            
            if attempt < max_attempts - 1:
                print(f"   ⏳ Retrying... (attempt {attempt + 2}/{max_attempts})")
                time.sleep(5)
        
        print("   ❌ Could not find or click Install button")
        return False
    
    def _verify_app_installed(self, package_name):
        """Verify app is installed via ADB"""
        try:
            result = self._run_adb_command(['shell', 'pm', 'list', 'packages', package_name], timeout=10)
            if result and package_name in result.stdout:
                return True
            return False
        except Exception as e:
            print(f"   ⚠️  Error verifying installation: {e}")
            return False

    def install_eptura_engage_app(self):
        """
        Main orchestrator for installing Eptura Engage app via Play Store.
        
        Streamlined Flow (User already logged in to Google Play Store):
        1. Launch Play Store
        2. Search for Eptura Engage
        3. Install the app
        4. Verify installation
        """
        app_package = "com.condecosoftware.condeco"
        app_name = "Eptura Engage"
        print("\n========== EPTURA ENGAGE INSTALLATION FLOW ==========")
        print("ℹ️  NOTE: User is already logged into Google Play Store\n")
        start_time = time.time()
        
        print("Step 1: Launching Play Store app...")
        playstore_launched = self.open_play_store()
        time.sleep(5)
        self.take_screenshot("step1_playstore_launch")
        if not playstore_launched:
            print("   ❌ Failed to launch Play Store app.")
            self._print_installation_summary(False, start_time)
            return False
        print("   ✅ Play Store app launched.")
        time.sleep(1)

        print(f"\nStep 2: Searching for '{app_name}' in Play Store...")
        search_success = self._search_app_in_playstore(app_name)
        time.sleep(3)
        self.take_screenshot("step2_search")
        if not search_success:
            print(f"   ❌ Failed to search for '{app_name}'.")
            self._print_installation_summary(False, start_time)
            return False
        print(f"   ✅ Found '{app_name}' in Play Store.")
        time.sleep(1)

        print(f"\nStep 3: Waiting for app page to load...")
        time.sleep(5)
        self.take_screenshot("step3_app_page_load")
        
        print(f"\nStep 4: Installing '{app_name}'...")
        install_success = self._install_app_from_playstore(app_package)
        time.sleep(3)
        self.take_screenshot("step4_install_clicked")
        if not install_success:
            print(f"   ❌ Failed to click Install button for '{app_name}'.")
            self._print_installation_summary(False, start_time)
            return False
        print(f"   ✅ Install button clicked.")
        time.sleep(1)

        print(f"\nStep 5: Verifying installation of '{app_name}'...")
        max_wait = 300  # 5 minutes
        check_interval = 10
        wait_time = 0
        verified = False
        while wait_time < max_wait:
            verify_result = self._verify_app_installed(app_package)
            time.sleep(2)
            if wait_time % 30 == 0:
                self.take_screenshot(f"step5_verification_{wait_time}s")
            if verify_result:
                print(f"   ✅ '{app_name}' is installed successfully!")
                verified = True
                break
            time.sleep(check_interval)
            wait_time += check_interval
            if wait_time % 30 == 0:
                print(f"      Still waiting for installation... ({wait_time}/{max_wait}s)")
        
        if not verified:
            print(f"   ❌ '{app_name}' installation verification failed after {max_wait}s.")
            self.take_screenshot("step5_verification_failed")
        
        self._print_installation_summary(verified, start_time)
        return verified

    def _print_installation_summary(self, success, start_time):
        """Prints installation summary after verification"""
        duration = int(time.time() - start_time)
        print("\n============================================================")
        print("INSTALLATION SUMMARY")
        print("============================================================")
        print(f"Installation Result: {'SUCCESS ✅' if success else 'FAILED ❌'}")
        print(f"Duration: {duration} seconds")
        print("============================================================\n")

if __name__ == "__main__":
    print("🚀 Starting Eptura Engage App Installation from Google Play Store")
    print("ℹ️  User is expected to be already logged into Google Play Store\n")
    
    installer = PlayStoreInstaller()
    success = installer.install_eptura_engage_app()
    sys.exit(0 if success else 1)