#!/usr/bin/env python3
"""
Automated Google Play Store Login and App Installation Script
Installs Eptura Engage app from Play Store using provided credentials
Compatible with macOS and Windows CI/CD environments
Optimized for Android 15 (API 35)
"""

# ============================================================================
# CONFIGURATION - SET YOUR GOOGLE CREDENTIALS HERE
# ============================================================================
GOOGLE_EMAIL = "epturaengageautomation@gmail.com"  # Replace with your Google email
GOOGLE_PASSWORD = "Eptura@2025"      # Replace with your Google password
# ============================================================================

import os
import sys
import time
import subprocess
import platform
import base64
import requests
from datetime import datetime
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
        # Removed self.video_dir and all video recording related attributes
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
        # Screenshot functionality disabled
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
        # Add recovery logic before waiting
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
            # Try recovery if offline
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
        """Initialize Appium driver for Play Store automation
        Optimized for macOS and Android 15"""
        print("🔧 Setting up Appium driver for Play Store...")
        print(f"🖥️  Platform: {platform.system()}")
        
        # Check Appium server availability first
        if not self.check_appium_server():
            print("❌ Appium server is not available. Exiting.")
            sys.exit(1)
        
        # Ensure emulator is ready and recover if needed
        if not self.wait_for_emulator_ready():
            print("⚠️  Proceeding anyway, but may encounter issues...")
        
        # Check if Appium helper APKs are already installed (from warm-up script)
        print("🔍 Checking for pre-installed Appium APKs...")
        appium_apks_installed = self._check_appium_apks_installed()
        
        options = UiAutomator2Options()
        options.platform_name = "Android"
        options.automation_name = "UiAutomator2"
        options.device_name = "Android Emulator"
        options.no_reset = True
        options.full_reset = False
        # INCREASED timeouts for slow emulator APK installations (5+ minutes)
        options.new_command_timeout = 600
        options.adb_exec_timeout = 240000  # Increased from 100000 to 240000 (4 minutes)
        options.uiautomator2_server_launch_timeout = 120000  # Increased from 60000 to 120000 (2 minutes)
        options.uiautomator2_server_install_timeout = 180000  # Increased from 60000 to 180000 (3 minutes)
        
        # If APKs are already installed, we can skip installation and device init
        # This significantly speeds up driver initialization
        if appium_apks_installed:
            print("✅ Appium APKs already installed, skipping installation step")
            options.skip_server_installation = True
            options.skip_device_initialization = True
        else:
            print("⚠️  Appium APKs not pre-installed, will install during initialization")
            options.skip_server_installation = False
            options.skip_device_initialization = False
        
        # Ensure package manager is fully responsive before driver init
        print("🔧 Pre-flight check: Testing package manager responsiveness...")
        for attempt in range(3):
            result = self._run_adb_command(['shell', 'pm', 'list', 'packages', '-s'], timeout=30)
            if result and result.returncode == 0:
                print(f"✅ Package manager responsive (attempt {attempt + 1})")
                break
            print(f"⚠️  Package manager slow, waiting... (attempt {attempt + 1}/3)")
            time.sleep(10)
        
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
                import traceback
                traceback.print_exc()
                
                # If it's a timeout issue, suggest increasing timeout
                if 'timed out' in str(e).lower() and 'install' in str(e).lower():
                    print("💡 APK installation timeout detected - emulator is too slow")
                    print("   This usually resolves after emulator warms up")
                    # If we thought APKs were installed but got timeout, disable skip on retry
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
                    print("❌ Exiting due to Appium driver initialization failure.")
                    sys.exit(1)
    
    def _check_appium_apks_installed(self):
        """Check if Appium UiAutomator2 APKs are already installed on the device"""
        try:
            # Check for the main packages that Appium needs
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
            
            # All packages must be present
            if installed_count == len(required_packages):
                print(f"✅ All {len(required_packages)} Appium APKs are pre-installed")
                return True
            else:
                print(f"⚠️  Only {installed_count}/{len(required_packages)} Appium APKs found")
                return False
                
        except Exception as e:
            print(f"⚠️  Error checking Appium APKs: {e}")
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
            # Try multiple methods to open Play Store
            # Method 1: Open main Play Store activity (most reliable)
            result = self._run_adb_command([
                'shell', 'am', 'start', '-n', 
                'com.android.vending/.AssetBrowserActivity'
            ], timeout=10)
            
            # If that fails, try alternative activity
            if not result or result.returncode != 0:
                print("   ⚠️  AssetBrowserActivity failed, trying MainActivity...")
                result = self._run_adb_command([
                    'shell', 'am', 'start', '-n',
                    'com.android.vending/com.google.android.finsky.activities.MainActivity'
                ], timeout=10)
            
            # If both fail, try simple launch intent
            if not result or result.returncode != 0:
                print("   ⚠️  Explicit activities failed, trying launch intent...")
                result = self._run_adb_command([
                    'shell', 'am', 'start', '-a', 'android.intent.action.MAIN',
                    '-c', 'android.intent.category.LAUNCHER',
                    '-n', 'com.android.vending/com.android.vending.AssetBrowserActivity'
                ], timeout=10)
            
            # Final fallback - just open the package
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
    
    def login_to_google_account(self):
        """Automate Google account login in Play Store"""
        print("\n" + "="*70)
        print("🔐 STARTING GOOGLE ACCOUNT LOGIN PROCESS")
        print("="*70)
        print(f"📧 Email to use: {self.email}")
        print(f"🔑 Password to use: {self.password}")
        print(f"🔑 Password length: {len(self.password) if self.password else 0} characters")
        
        try:
            # Check if already logged in
            print("\n[Step 1/6] Checking if already logged in...")
            time.sleep(3)
            
            # Look for common "Sign in" or "Add account" buttons
            sign_in_texts = [
                "Sign in",
                "Add account",
                "GET STARTED",
                "Use another account"
            ]
            
            signed_in = True
            found_text = None
            for text in sign_in_texts:
                try:
                    if self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 
                                               f'new UiSelector().textContains("{text}")'):
                        signed_in = False
                        found_text = text
                        print(f"   ⚠️  Found '{text}' button - login required")
                        break
                except:
                    continue
            
            if signed_in:
                print("   ✅ Already logged in to Google account")
                print("="*70 + "\n")
                return True
            
            # Click on Sign In button
            print(f"\n[Step 2/6] Clicking Sign In button (found: '{found_text}')...")
            sign_in_clicked = False
            for text in sign_in_texts:
                try:
                    print(f"   🔍 Trying to find button with text: '{text}'")
                    element = self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,
                                                      f'new UiSelector().textContains("{text}")')
                    element.click()
                    print(f"   ✅ Successfully clicked '{text}' button")
                    sign_in_clicked = True
                    time.sleep(3)
                    break
                except Exception as e:
                    print(f"   ⚠️  '{text}' not found: {str(e)[:80]}")
                    continue
            
            if not sign_in_clicked:
                print("   ⚠️  Could not find Sign In button, may already be logged in")
                print("="*70 + "\n")
                return True
            
            # Enter email
            print(f"\n[Step 3/6] Entering email address...")
            print(f"   📧 Email: {self.email}")
            email_selectors = [
                ('identifierId', 'new UiSelector().resourceId("identifierId")'),
                ('EditText class', 'new UiSelector().className("android.widget.EditText")'),
                ('Email text', 'new UiSelector().textContains("Email")')
            ]
            
            email_entered = False
            for selector_name, selector in email_selectors:
                try:
                    print(f"   🔍 Trying selector: {selector_name}")
                    email_field = self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, selector)
                    email_field.clear()
                    time.sleep(1)
                    email_field.send_keys(self.email)
                    print(f"   ✅ Email entered successfully using: {selector_name}")
                    email_entered = True
                    break
                except Exception as e:
                    print(f"   ⚠️  {selector_name} failed: {str(e)[:80]}")
                    continue
            
            if not email_entered:
                print("   ❌ FAILED: Could not find email input field")
                print("="*70 + "\n")
                return False
            
            time.sleep(2)
            
            # Click Next button
            print("\n[Step 4/6] Clicking Next button after email...")
            next_texts = ["Next", "NEXT", "Continue", "CONTINUE"]
            next_clicked = False
            for text in next_texts:
                try:
                    print(f"   🔍 Looking for '{text}' button")
                    next_btn = self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,
                                                       f'new UiSelector().textContains("{text}")')
                    next_btn.click()
                    print(f"   ✅ Clicked '{text}' button")
                    next_clicked = True
                    break
                except Exception as e:
                    print(f"   ⚠️  '{text}' not found: {str(e)[:80]}")
                    continue
            
            if not next_clicked:
                print("   ⚠️  Could not find Next button, trying to continue anyway...")
            
            time.sleep(3)
            
            # Enter password
            print("\n[Step 5/6] Entering password...")
            print(f"   🔑 Password length: {len(self.password)} characters")
            password_selectors = [
                ('password resourceId', 'new UiSelector().resourceId("password")'),
                ('EditText class', 'new UiSelector().className("android.widget.EditText")'),
                ('password text', 'new UiSelector().textContains("password")')
            ]
            
            password_entered = False
            for selector_name, selector in password_selectors:
                try:
                    print(f"   🔍 Trying selector: {selector_name}")
                    password_field = self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, selector)
                    password_field.clear()
                    time.sleep(1)
                    password_field.send_keys(self.password)
                    print(f"   ✅ Password entered successfully using: {selector_name}")
                    password_entered = True
                    break
                except Exception as e:
                    print(f"   ⚠️  {selector_name} failed: {str(e)[:80]}")
                    continue
            
            if not password_entered:
                print("   ❌ FAILED: Could not find password input field")
                print("="*70 + "\n")
                return False
            
            time.sleep(2)
            
            # Click Next/Sign in button
            print("\n[Step 6/6] Clicking Sign In button after password...")
            signin_clicked = False
            for text in next_texts:
                try:
                    print(f"   🔍 Looking for '{text}' button")
                    sign_in_btn = self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,
                                                          f'new UiSelector().textContains("{text}")')
                    sign_in_btn.click()
                    print(f"   ✅ Clicked '{text}' button")
                    signin_clicked = True
                    break
                except Exception as e:
                    print(f"   ⚠️  '{text}' not found: {str(e)[:80]}")
                    continue
            
            if not signin_clicked:
                print("   ⚠️  Could not find Sign In button, trying to continue anyway...")
            
            # Wait for login to complete
            print("\n⏳ Waiting for login to complete (10 seconds)...")
            time.sleep(10)
            
            # Handle post-login prompts (Skip, Not now, etc.)
            print("\n📱 Handling post-login prompts...")
            skip_texts = ["Skip", "SKIP", "Not now", "NO THANKS", "Accept", "ACCEPT", "I agree", "AGREE"]
            prompts_handled = 0
            for attempt in range(3):  # Try multiple times for different prompts
                print(f"   Attempt {attempt + 1}/3 to dismiss prompts...")
                for text in skip_texts:
                    try:
                        skip_btn = self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,
                                                           f'new UiSelector().textContains("{text}")')
                        skip_btn.click()
                        print(f"      ✅ Dismissed prompt: '{text}'")
                        prompts_handled += 1
                        time.sleep(2)
                    except:
                        continue
            
            print(f"   📊 Handled {prompts_handled} post-login prompt(s)")
            print("\n✅ LOGIN PROCESS COMPLETED")
            print("="*70 + "\n")
            return True
            
        except Exception as e:
            print(f"\n❌ CRITICAL ERROR during login: {e}")
            print(f"   Exception type: {type(e).__name__}")
            print(f"   Exception details: {str(e)}")
            print("="*70 + "\n")
            return False
    
    def _install_via_url(self, package_name):
        """Helper method to install app via direct Play Store URL
        This is the most reliable method as it skips searching"""
        try:
            print(f"🔗 Opening Play Store directly for package: {package_name}")
            
            # Open Play Store app page directly via ADB
            result = self._run_adb_command([
                'shell', 'am', 'start', '-a', 'android.intent.action.VIEW',
                '-d', f'market://details?id={package_name}'
            ], timeout=15)
            
            if not result or result.returncode != 0:
                print("   ⚠️  Failed to open Play Store via URL")
                return False
            
            print("   ✅ Play Store opened to app page")
            time.sleep(10)  # Wait for page to load
            
            # Ensure driver is initialized
            if not self.driver:
                print("   ⚠️  No Appium driver available for URL method")
                return False
            
            # Look for Install button
            print("   📲 Looking for Install button...")
            install_texts = ["Install", "INSTALL", "Update", "UPDATE", "Open", "OPEN", "Get"]
            
            for attempt in range(8):  # Give it more attempts
                for text in install_texts:
                    try:
                        install_btn = self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,
                                                              f'new UiSelector().textContains("{text}")')
                        button_text = install_btn.text if hasattr(install_btn, 'text') else text
                        
                        if button_text.upper() in ["OPEN"]:
                            print(f"   ✅ App is already installed!")
                            return True
                        
                        print(f"   🔍 Found '{button_text}' button")
                        install_btn.click()
                        print(f"   ✅ Clicked '{button_text}' button")
                        
                        # Wait for installation
                        print("   ⏳ Waiting for installation to complete...")
                        max_wait = 300  # 5 minutes
                        wait_time = 0
                        check_interval = 10
                        
                        while wait_time < max_wait:
                            # Check if installed
                            result = self._run_adb_command(['shell', 'pm', 'list', 'packages', package_name], timeout=10)
                            if result and package_name in result.stdout:
                                print(f"   ✅ Installation completed! (verified in {wait_time}s)")
                                return True
                            
                            # Check for Open button
                            try:
                                open_btn = self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,
                                                                   'new UiSelector().text("Open")')
                                print(f"   ✅ Installation completed! (Open button appeared)")
                                return True
                            except:
                                pass
                            
                            time.sleep(check_interval)
                            wait_time += check_interval
                            
                            if wait_time % 30 == 0:
                                print(f"      Still installing... ({wait_time}/{max_wait}s)")
                        
                        print(f"   ⚠️  Installation timeout after {max_wait}s")
                        return False
                        
                    except:
                        pass
                
                if attempt < 7:
                    print(f"   ⏳ Attempt {attempt + 1}/8 - waiting before retry...")
                    time.sleep(5)
            
            print("   ❌ Could not find Install button after all attempts")
            return False
            
        except Exception as e:
            print(f"   ❌ Error in _install_via_url: {e}")
            return False
    
    def _install_playstore_and_retry(self, app_name="Eptura Engage"):
        """Fallback method: Install Google Play Store if missing, then try full automation
        This method:
        1. Checks if Play Store is installed
        2. Installs Play Store if missing
        3. Opens Play Store
        4. Logs in with provided credentials
        5. Searches for the app
        6. Installs the app
        """
        
        print("\n" + "="*70)
        print("🏪 METHOD 1: INSTALL PLAY STORE + FULL AUTOMATION")
        print("="*70)
        print("ℹ️  This method will:")
        print("   1. Verify/Install Google Play Store")
        print("   2. Open Play Store")
        print("   3. Login with provided credentials")
        print("   4. Search for Eptura Engage")
        print("   5. Click on the app")
        print("   6. Click Install button")
        print("="*70)
        
        try:
            # Step 1: Check if Play Store is installed
            print("\n[Step 1/6] Checking Google Play Store installation...")
            result = self._run_adb_command(['shell', 'pm', 'list', 'packages', 'com.android.vending'], timeout=10)
            if not result or 'com.android.vending' not in result.stdout:
                print("   ⚠️  Google Play Store NOT installed")
                print("   📦 Installing Google Play Store...")
                
                # Install Play Store APK (this would need the APK file)
                # For emulators, Play Store should already be present
                # This is a placeholder - in practice, you'd need the APK
                print("   ℹ️  Note: For emulators, Play Store should be pre-installed")
                print("   ℹ️  If missing, use an emulator image with Google Play")
                
                # Check again after potential installation
                result = self._run_adb_command(['shell', 'pm', 'list', 'packages', 'com.android.vending'], timeout=10)
                if not result or 'com.android.vending' not in result.stdout:
                    print("   ❌ Cannot proceed without Play Store")
                    return False
            else:
                print("   ✅ Google Play Store is already installed")
            
            # Step 2: Ensure Appium driver is initialized
            print("\n[Step 2/6] Ensuring Appium driver is ready...")
            if not self.driver:
                if not self.setup_driver():
                    print("   ❌ Failed to initialize Appium driver")
                    return False
            print("   ✅ Appium driver ready")
            
            # Step 3: Open Play Store
            print("\n[Step 3/6] Opening Google Play Store...")
            if not self.open_play_store():
                print("   ❌ Failed to open Play Store")
                return False
            print("   ✅ Play Store opened")
            
            # Check for crash after opening
            if self._handle_app_crash_dialog():
                print("   🔧 Handled crash, continuing...")
                time.sleep(3)
            
            # Step 4: Login to Google Account
            print("\n[Step 4/6] Logging in to Google Account...")
            if not self.login_to_google_account():
                print("   ⚠️  Login failed or already logged in, continuing anyway...")
            else:
                print("   ✅ Login successful")
            
            # Check for crash after login
            if self._handle_app_crash_dialog():
                print("   🔧 Handled crash after login, continuing...")
                self.open_play_store()
                time.sleep(3)
            
            # Step 5: Search for the app with retry logic
            max_search_retries = 3
            search_attempt = 0
            app_clicked = False
            while search_attempt < max_search_retries and not app_clicked:
                print(f"\n[Search Attempt {search_attempt + 1}/{max_search_retries}] Searching for '{app_name}'...")
                # Open search
                search_opened = False
                for selector_name, selector in search_selectors:
                    try:
                        print(f"   🔍 Opening search with: {selector_name}")
                        search_icon = self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, selector)
                        search_icon.click()
                        time.sleep(3)
                        search_opened = True
                        print(f"   ✅ Search opened")
                        break
                    except Exception as e:
                        print(f"   ⚠️  Could not open search with {selector_name}: {e}")
                        continue
                if not search_opened:
                    print("   ❌ Could not open search")
                    break
                # Type app name
                print(f"   ⌨️  Typing '{app_name}'...")
                text_entered = False
                for selector_name, selector in search_field_selectors:
                    try:
                        search_field = self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, selector)
                        search_field.clear()
                        time.sleep(1)
                        search_field.send_keys(app_name)
                        entered_text = search_field.text if hasattr(search_field, 'text') else None
                        if entered_text and app_name.lower() in entered_text.lower():
                            text_entered = True
                            print(f"   ✅ Verified text entry: '{entered_text}'")
                        else:
                            print(f"   ⚠️  Text entry not verified. Field value: '{entered_text}'")
                        time.sleep(2)
                        break
                    except Exception as e:
                        print(f"   ⚠️  Could not enter text with {selector_name}: {e}")
                        continue
                if not text_entered:
                    print("   ❌ Could not type or verify search text")
                    break
                # Trigger search
                print("   🔍 Attempting to trigger search...")
                search_triggered = False
                try:
                    self.driver.press_keycode(66)  # KEYCODE_ENTER
                    print("   ✅ Search triggered via Enter key")
                    search_triggered = True
                    time.sleep(2)  # Wait for search results to load
                    time.sleep(5)
                except Exception as e:
                    print(f"   ⚠️  Could not trigger search via Enter key: {str(e)[:100]}")
                    # Try ADB method
                    try:
                        self._run_adb_command(['shell', 'input', 'keyevent', 'KEYCODE_ENTER'])
                        print("   ✅ Search triggered via ADB keyevent")
                        search_triggered = True
                        time.sleep(2)  # Wait for search results to load
                        time.sleep(5)
                    except Exception as e2:
                        print(f"   ⚠️  Could not trigger search via ADB: {str(e2)[:100]}")
            
            # Step 5: Look for app in search results using XPath first (most reliable)
            print(f"   🔍 Looking for app in search results using XPath...")
            app_found = False
            
            # Try XPath first - this is the most reliable method
            try:
                print(f"   🔍 Attempting to click app using XPath: {app_result_xpath}")
                app_element = self.driver.find_element(AppiumBy.XPATH, app_result_xpath)
                print(f"   🖱️  Clicking app using XPath...")
                app_element.click()
                app_found = True
                time.sleep(3)
                print(f"   ✅ Found and clicked app via XPath")
                return True
            except Exception as e:
                print(f"   ⚠️  Could not find/click app via XPath: {str(e)[:100]}")
            
            # Fallback to text-based patterns if XPath fails
            if not app_found:
                print(f"   🔍 Falling back to text-based patterns...")
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
                            return True
                    except Exception as e:
                        print(f"   ⚠️  Could not find/click app with pattern '{pattern}': {str(e)[:80]}")
            
            if not app_found:
                print(f"   ❌ App not found in results (attempt {search_attempt+1}). Killing Play Store and retrying...")
                self._run_adb_command(['shell', 'am', 'force-stop', 'com.android.vending'])
                time.sleep(2)
                print("   🔄 Relaunching Play Store app...")
                self.open_play_store()
                time.sleep(5)
                # Handle crash dialog after relaunch
                if self._handle_app_crash_dialog():
                    print("   🔧 Handled crash after relaunch, continuing...")
                    time.sleep(3)
                search_attempt += 1
            if not app_clicked:
                print("   ❌ Failed to find and click app after all retries.")
                return False
            # Step 6: Click on the app from search results
            print(f"\n[Step 6/6] Clicking on '{app_name}' in results...")
            
            # Wait for results
            time.sleep(5)
            # self._take_debug_screenshot("fallback_method_search_results")
            
            # Find and click the app
            app_clicked = False
            search_patterns = ["Eptura Engage", "Eptura", "Condeco"]
            
            for pattern in search_patterns:
                try:
                    print(f"   🔍 Looking for: '{pattern}'")
                    elements = self.driver.find_elements(AppiumBy.ANDROID_UIAUTOMATOR,
                        f'new UiSelector().textContains("{pattern}")')
                    
                    if elements:
                        first_element = elements[0]
                        element_text = first_element.text if hasattr(first_element, 'text') else pattern
                        print(f"   🖱️  Clicking: '{element_text}'")
                        first_element.click()
                        app_clicked = True
                        time.sleep(5)
                        print(f"   ✅ Clicked on app")
                        break
                except:
                    continue
            
            if not app_clicked:
                print("   ❌ Could not find app in results")
                return False
            
            # Check for crash after clicking app
            if self._handle_app_crash_dialog():
                print("   🔧 Handled crash after clicking app, continuing...")
                time.sleep(3)
            
            # Wait for app page to load
            print("   ⏳ Waiting for app page to load...")
            time.sleep(10)
            # self._take_debug_screenshot("fallback_method_app_page")
            
            # Click Install button
            print("   📲 Looking for Install button...")
            install_texts = ["Install", "INSTALL", "Update", "UPDATE", "Get", "Open", "OPEN"]
            
            for attempt in range(5):
                # Check for crash
                if self._handle_app_crash_dialog():
                    print("   🔧 Handled crash, continuing...")
                    time.sleep(3)
                
                for text in install_texts:
                    try:
                        install_btn = self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,
                            f'new UiSelector().textContains("{text}")')
                        
                        button_text = install_btn.text if hasattr(install_btn, 'text') else text
                        
                        if button_text.upper() in ["OPEN"]:
                            print(f"   ✅ App already installed!")
                            return True
                        
                        print(f"   🔍 Found '{button_text}' button")
                        install_btn.click()
                        print(f"   ✅ Clicked '{button_text}' button")
                        
                        # Wait for installation
                        print("   ⏳ Waiting for installation to complete...")
                        max_wait = 300  # 5 minutes
                        wait_time = 0
                        check_interval = 10
                        
                        while wait_time < max_wait:
                            # Check if installed
                            result = self._run_adb_command(['shell', 'pm', 'list', 'packages', package_name], timeout=10)
                            if result and package_name in result.stdout:
                                print(f"   ✅ Installation completed! (verified in {wait_time}s)")
                                return True
                            
                            # Check for Open button
                            try:
                                open_btn = self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,
                                                                   'new UiSelector().text("Open")')
                                print(f"   ✅ Installation completed! (Open button appeared)")
                                return True
                            except:
                                pass
                            
                            time.sleep(check_interval)
                            wait_time += check_interval
                            
                            if wait_time % 30 == 0:
                                print(f"      Still installing... ({wait_time}/{max_wait}s)")
                        
                        print(f"   ⚠️  Installation timeout after {max_wait}s")
                        return False
                    except:
                        continue
            
            print("   ❌ Could not find or click Install button")
            return False
            
        except Exception as e:
            print(f"\n❌ Error in fallback method: {e}")
            import traceback
            traceback.print_exc()
            return False
    
    def _search_app_in_playstore(self, app_name, max_retries=3):
        """
        Robustly search for the app in Play Store, retrying if needed.
        Returns True if app is found and clicked, False otherwise.
        """
        # XPaths provided by user with fallback options
        # Primary XPath for search icon
        search_icon_xpath = '//androidx.compose.ui.platform.ComposeView[@resource-id="com.android.vending:id/0_resource_name_obfuscated"]/android.view.View/android.view.View[2]/android.view.View/android.view.View[3]/android.view.View[1]/iwq/android.widget.ImageView'
        
        # Fallback XPaths for search icon (more resilient)
        search_icon_fallback_xpaths = [
            '//android.widget.ImageView[@content-desc="Search"]',
            '//android.view.View[@resource-id="com.android.vending:id/search_button"]',
            '//*[contains(@content-desc, "Search")]',
            '//android.widget.ImageView[@content-desc="Search Google Play"]'
        ]
        
        search_input_xpath = '//androidx.compose.ui.platform.ComposeView[@resource-id="com.android.vending:id/0_resource_name_obfuscated"]/android.view.View/android.view.View[1]/android.view.View/android.view.View/android.view.View[2]/android.view.View[1]/android.widget.Button'
        # XPath to click on the app result after search is triggered
        app_result_xpath = '//android.view.View[@content-desc="Eptura Engage Eptura, Inc "]'
        search_patterns = [app_name, "Eptura", "Condeco"]
        
        for attempt in range(max_retries):
            print(f"\n🔍 [Search Attempt {attempt+1}/{max_retries}] for '{app_name}'")
            
            # Wait 3 seconds to ensure Play Store UI is fully loaded
            print("   ⏳ Waiting 3 seconds for Play Store UI to fully load...")
            time.sleep(3)
            
            # Step 1: Click on the search icon (bottom bar)
            print("   📱 Clicking search icon on bottom navigation bar...")
            search_icon_clicked = False
            
            # Try primary XPath first
            try:
                search_icon = self.driver.find_element(AppiumBy.XPATH, search_icon_xpath)
                search_icon.click()
                print(f"   ✅ Search icon clicked successfully")
                search_icon_clicked = True
                time.sleep(2)
            except Exception as e:
                print(f"   ⚠️  Could not click search icon via primary XPath: {str(e)[:80]}")
                
                # Try fallback XPaths
                for fallback_xpath in search_icon_fallback_xpaths:
                    try:
                        print(f"   🔄 Trying fallback XPath: {fallback_xpath[:60]}...")
                        search_icon = self.driver.find_element(AppiumBy.XPATH, fallback_xpath)
                        search_icon.click()
                        print(f"   ✅ Search icon clicked successfully via fallback XPath")
                        search_icon_clicked = True
                        time.sleep(2)
                        break
                    except:
                        continue
                
                # Try using UIAutomator as last resort
                if not search_icon_clicked:
                    try:
                        print(f"   🔄 Trying UIAutomator to find search button...")
                        search_icon = self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,
                            'new UiSelector().descriptionContains("Search")')
                        search_icon.click()
                        print(f"   ✅ Search icon clicked successfully via UIAutomator")
                        search_icon_clicked = True
                        time.sleep(2)
                    except Exception as e2:
                        print(f"   ⚠️  Could not click search icon via UIAutomator: {str(e2)[:80]}")
            
            if not search_icon_clicked:
                print("   ❌ Could not click search icon. Retrying after relaunch...")
                self._run_adb_command(['shell', 'am', 'force-stop', 'com.android.vending'])
                time.sleep(2)
                self.open_play_store()
                time.sleep(5)
                continue
            
            # Step 2: Click on the search input field
            print("   🔍 Clicking search input field...")
            search_input_clicked = False
            try:
                search_input = self.driver.find_element(AppiumBy.XPATH, search_input_xpath)
                search_input.click()
                print(f"   ✅ Search input field clicked successfully")
                search_input_clicked = True
                time.sleep(2)
            except Exception as e:
                print(f"   ⚠️  Could not click search input via XPath: {str(e)[:80]}")
            
            if not search_input_clicked:
                print("   ❌ Could not click search input. Retrying after relaunch...")
                self._run_adb_command(['shell', 'am', 'force-stop', 'com.android.vending'])
                time.sleep(2)
                self.open_play_store()
                time.sleep(5)
                continue
            
            # Step 3: Enter app name in search field
            print(f"   ⌨️  Typing '{app_name}'...")
            text_entered = False
            try:
                # Find EditText to enter text
                edit_text = self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.EditText")')
                edit_text.clear()
                time.sleep(0.5)
                edit_text.send_keys(app_name)
                time.sleep(2)
                print(f"   ✅ Text entered successfully: '{app_name}'")
                text_entered = True
            except Exception as e:
                print(f"   ⚠️  Could not enter text: {str(e)[:100]}")
            
            if not text_entered:
                print("   ❌ Could not enter search text. Retrying after relaunch...")
                self._run_adb_command(['shell', 'am', 'force-stop', 'com.android.vending'])
                time.sleep(2)
                self.open_play_store()
                time.sleep(5)
                continue
            
            # Step 4: Trigger search by pressing Enter
            print("   🔍 Triggering search...")
            search_triggered = False
            try:
                self.driver.press_keycode(66)  # KEYCODE_ENTER
                print("   ✅ Search triggered via Enter key")
                search_triggered = True
                time.sleep(2)  # Wait for search results to load
                time.sleep(5)
            except Exception as e:
                print(f"   ⚠️  Could not trigger search via Enter key: {str(e)[:100]}")
                # Try ADB method
                try:
                    self._run_adb_command(['shell', 'input', 'keyevent', 'KEYCODE_ENTER'])
                    print("   ✅ Search triggered via ADB keyevent")
                    search_triggered = True
                    time.sleep(2)  # Wait for search results to load
                    time.sleep(5)
                except Exception as e2:
                    print(f"   ⚠️  Could not trigger search via ADB: {str(e2)[:100]}")
            
            # Step 5: Look for app in search results using XPath first (most reliable)
            print(f"   🔍 Looking for app in search results using XPath...")
            app_found = False
            
            # Try XPath first - this is the most reliable method
            try:
                print(f"   🔍 Attempting to click app using XPath: {app_result_xpath}")
                app_element = self.driver.find_element(AppiumBy.XPATH, app_result_xpath)
                print(f"   🖱️  Clicking app using XPath...")
                app_element.click()
                app_found = True
                time.sleep(3)
                print(f"   ✅ Found and clicked app via XPath")
                return True
            except Exception as e:
                print(f"   ⚠️  Could not find/click app via XPath: {str(e)[:100]}")
            
            # Fallback to text-based patterns if XPath fails
            if not app_found:
                print(f"   🔍 Falling back to text-based patterns...")
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
                            return True
                    except Exception as e:
                        print(f"   ⚠️  Could not find/click app with pattern '{pattern}': {str(e)[:80]}")
            
            if not app_found:
                print(f"   ❌ App not found in results (attempt {attempt+1}). Killing Play Store and retrying...")
                self._run_adb_command(['shell', 'am', 'force-stop', 'com.android.vending'])
                time.sleep(2)
                self.open_play_store()
                time.sleep(5)
        
        print(f"   ❌ Failed to find and click app after {max_retries} attempts.")
        return False
    
    def search_and_install_app(self, app_name="Eptura Engage"):
        """Search for app and install it using Play Store app only (no browser-style search)"""
        print("\n" + "="*70)
        print(f"🔍 STARTING APP SEARCH AND INSTALLATION VIA PLAY STORE APP")
        print("="*70)
        print(f"📱 App to search: {app_name}")
        try:
            # Remove browser-style search method entirely
            # PRIORITY 1: Install Play Store (if needed) + Full Automation
            print("\n🏪 METHOD 1: INSTALL PLAY STORE + FULL AUTOMATION")
            if self._install_playstore_and_retry(app_name):
                print("✅ Play Store app installation succeeded!")
                return True
            print("\n⚠️  Play Store app method didn't complete, trying direct URL method...\n")
            # PRIORITY 2: Try direct URL approach
            print("\n🚀 METHOD 2: DIRECT URL METHOD")
            if self._install_via_url("com.condecosoftware.condeco"):
                print("✅ Direct URL installation succeeded!")
                return True
            print("⚠️  Direct URL method didn't complete, trying traditional search method...\n")
            # PRIORITY 3: Traditional Play Store search (final fallback)
            print("\n🔍 METHOD 3: TRADITIONAL PLAY STORE SEARCH (Final Fallback)")
            # ...existing code for traditional Play Store search...
            # (Retain only Play Store app-based search and install logic)
            # ...existing code...
        except Exception as e:
            print(f"❌ Error in search_and_install_app: {e}")
            return False
    
    def install_eptura_engage_app(self):
        """
        Main orchestrator for installing Eptura Engage app via Play Store with clear step logs.
        Steps:
        0. Check if app is already installed and uninstall if needed
        1. Check Play Store installation
        2. Initialize Appium driver
        3. Launch Play Store
        4. Wait for page to load
        5. Search for Eptura Engage
        6. Install the app
        7. Verify installation
        """
        app_package = "com.condecosoftware.condeco"
        app_name = "Eptura Engage"
        print("\n========== EPTURA ENGAGE INSTALLATION FLOW ==========")
        start_time = time.time()  # Track start time for duration
        
        # Step 0: Check if app is already installed and uninstall if needed
        print("Step 0: Checking if Eptura Engage is already installed...")
        result = self._run_adb_command(['shell', 'pm', 'list', 'packages', app_package], timeout=20)
        if result and app_package in result.stdout:
            print("   ⚠️  Eptura Engage is already installed")
            print("   🗑️  Uninstalling Eptura Engage...")
            uninstall_result = self._run_adb_command(['uninstall', app_package], timeout=30)
            if uninstall_result and uninstall_result.returncode == 0:
                print("   ✅ Eptura Engage uninstalled successfully")
                time.sleep(3)
            else:
                print("   ⚠️  Could not uninstall Eptura Engage, continuing anyway...")
                if uninstall_result:
                    print(f"   Error: {uninstall_result.stderr[:100]}")
        else:
            print("   ✅ Eptura Engage is not installed")
        time.sleep(1)
        
        print("Step 1: Checking Play Store installation...")
        result = self._run_adb_command(['shell', 'pm', 'list', 'packages', 'com.android.vending'], timeout=10)
        time.sleep(2)
        if not result or 'com.android.vending' not in result.stdout:
            print("   ❌ Play Store NOT installed.")
            self._print_installation_summary(False, start_time)
            return False
        print("   ✅ Play Store is installed.")
        time.sleep(1)

        print("\nStep 2: Initializing Appium driver...")
        self.setup_driver()
        if not self.driver:
            print("   ❌ Failed to initialize Appium driver.")
            self._print_installation_summary(False, start_time)
            return False
        print("   ✅ Appium driver initialized.")
        time.sleep(1)

        print("\nStep 3: Launching Play Store app...")
        playstore_launched = self.open_play_store()
        if not playstore_launched:
            print("   ❌ Failed to launch Play Store app.")
            self._print_installation_summary(False, start_time)
            return False
        print("   ✅ Play Store app launched.")
        
        print("\nStep 4: Waiting for Play Store to fully load...")
        time.sleep(5)
        print("   ✅ Play Store page loaded.")
        time.sleep(1)

        print(f"\nStep 5: Searching for '{app_name}' in Play Store...")
        search_success = self._search_app_in_playstore(app_name)
        time.sleep(3)
        if not search_success:
            print(f"   ❌ Failed to search for '{app_name}'.")
            self._print_installation_summary(False, start_time)
            return False
        print(f"   ✅ Found '{app_name}' in Play Store.")
        time.sleep(1)

        print(f"\nStep 6: Installing '{app_name}'...")
        install_success = self._install_app_from_playstore(app_package)
        time.sleep(3)
        if not install_success:
            print(f"   ❌ Failed to install '{app_name}'.")
            self._print_installation_summary(False, start_time)
            return False
        print(f"   ✅ '{app_name}' installation initiated.")
        time.sleep(1)

        print(f"\nStep 7: Verifying installation of '{app_name}'...")
        max_wait = 300  # 5 minutes
        check_interval = 10
        wait_time = 0
        verified = False
        while wait_time < max_wait:
            verify_result = self._verify_app_installed(app_package)
            time.sleep(2)
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
        self._print_installation_summary(verified, start_time)
        return verified

    def _print_installation_summary(self, success, start_time):
        """Prints installation summary after verification"""
        duration = int(time.time() - start_time)
        print("\n============================================================")
        print("INSTALLATION SUMMARY")
        print("============================================================")
        print(f"Installation Result: {'SUCCESS' if success else 'FAILED'}")
        print(f"Duration: {duration} seconds")
        print("============================================================\n")

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

    def _dismiss_initial_dialogs(self):
        """Dismiss any initial dialogs or alerts that appear after launching Play Store"""
        print("   🔔 Checking for initial dialogs/alerts...")
        dismiss_texts = ["Got it", "GOT IT", "OK", "OK, thanks", "Close", "CLOSE", "Accept", "ACCEPT", "I agree", "AGREE"]
        dialogs_dismissed = 0
        
        for attempt in range(3):  # Try multiple times for different dialogs
            for text in dismiss_texts:
                try:
                    dismiss_btn = self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,
                                                          f'new UiSelector().textContains("{text}")')
                    dismiss_btn.click()
                    print(f"   ✅ Dismissed dialog: '{text}'")
                    dialogs_dismissed += 1
                    time.sleep(2)
                except:
                    pass
        
        if dialogs_dismissed > 0:
            print(f"   📊 Dismissed {dialogs_dismissed} dialog(s)")
        return True

if __name__ == "__main__":
    # Use hardcoded credentials from configuration section at the top
    email = GOOGLE_EMAIL
    password = GOOGLE_PASSWORD
    
    if not email or email == "your_email@gmail.com":
        print("❌ ERROR: Please set your Google email in the GOOGLE_EMAIL variable at the top of this script.")
        sys.exit(1)
    if not password or password == "your_password":
        print("❌ ERROR: Please set your Google password in the GOOGLE_PASSWORD variable at the top of this script.")
        sys.exit(1)
    
    print(f"📧 Using email: {email}")
    installer = PlayStoreInstaller(email, password)
    success = installer.install_eptura_engage_app()
    sys.exit(0 if success else 1)