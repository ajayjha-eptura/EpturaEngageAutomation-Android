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
import base64
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
        self.recording_process = None
        self.recording_file = None
        self.video_dir = None
        
        # Ensure temp directory exists on Windows
        if self.is_windows and not os.path.exists(self.temp_dir):
            try:
                os.makedirs(self.temp_dir)
            except:
                self.temp_dir = os.path.expanduser('~\\AppData\\Local\\Temp')
        
        # Setup video directory
        self.setup_video_directory()
    
    def setup_video_directory(self):
        """Setup directory for storing video recordings"""
        try:
            # Try to use workspace directory first, fallback to temp
            workspace_dir = os.getcwd()
            video_dir = os.path.join(workspace_dir, 'playstore-recordings')
            
            if not os.path.exists(video_dir):
                os.makedirs(video_dir)
            
            self.video_dir = video_dir
            print(f"📹 Video recordings will be saved to: {video_dir}")
        except Exception as e:
            print(f"⚠️  Could not create video directory: {e}")
            self.video_dir = self.temp_dir
    
    def start_screen_recording_adb(self):
        """Start screen recording using ADB screenrecord (fallback method)"""
        try:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            self.recording_file = os.path.join(self.video_dir, f"playstore_install_{timestamp}.mp4")
            device_path = f"/sdcard/playstore_recording_{timestamp}.mp4"
            
            print(f"🎥 Starting screen recording via ADB...")
            print(f"   Device path: {device_path}")
            
            # Start recording in background with time limit (10 minutes max)
            # --time-limit in seconds, --bit-rate for quality
            cmd = ['adb', 'shell', 'screenrecord', '--verbose', 
                   '--time-limit', '600', '--bit-rate', '4000000', device_path]
            
            self.recording_process = subprocess.Popen(
                cmd,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                shell=self.is_windows
            )
            
            # Store device path for later retrieval
            self.recording_file = (self.recording_file, device_path)
            
            print("✅ Screen recording started (ADB method)")
            return True
            
        except Exception as e:
            print(f"⚠️  Could not start ADB screen recording: {e}")
            return False
    
    def start_screen_recording_appium(self):
        """Start screen recording using Appium's built-in method"""
        try:
            if not self.driver:
                print("⚠️  No Appium driver available for recording")
                return False
            
            print("🎥 Starting screen recording via Appium...")
            
            # Start recording with Appium (automatically handles encoding)
            # Options: videoQuality (low/medium/high), timeLimit (seconds)
            self.driver.start_recording_screen(
                videoQuality='medium',
                timeLimit='600',  # 10 minutes max
                bitRate='4000000'  # 4 Mbps
            )
            
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            self.recording_file = os.path.join(self.video_dir, f"playstore_install_{timestamp}.mp4")
            
            print("✅ Screen recording started (Appium method)")
            return True
            
        except Exception as e:
            print(f"⚠️  Could not start Appium screen recording: {e}")
            return False
    
    def stop_and_save_recording_adb(self):
        """Stop ADB screen recording and pull the file"""
        try:
            if not self.recording_process:
                return False
            
            print("⏹️  Stopping screen recording...")
            
            # Send interrupt signal to stop recording
            self.recording_process.terminate()
            time.sleep(2)
            
            # Get the device path
            local_path, device_path = self.recording_file
            
            # Wait a bit for file to be finalized
            time.sleep(3)
            
            # Pull the recording from device
            print(f"📥 Pulling recording from device...")
            result = self._run_adb_command(['pull', device_path, local_path], timeout=60)
            
            if result and result.returncode == 0:
                # Clean up device file
                self._run_adb_command(['shell', 'rm', device_path])
                
                # Check if file exists and has size
                if os.path.exists(local_path) and os.path.getsize(local_path) > 0:
                    file_size = os.path.getsize(local_path) / (1024 * 1024)  # MB
                    print(f"✅ Recording saved: {local_path}")
                    print(f"   File size: {file_size:.2f} MB")
                    return True
                else:
                    print(f"⚠️  Recording file is empty or missing")
                    return False
            else:
                print(f"⚠️  Failed to pull recording from device")
                return False
                
        except Exception as e:
            print(f"⚠️  Error stopping ADB recording: {e}")
            return False
    
    def stop_and_save_recording_appium(self):
        """Stop Appium screen recording and save the file"""
        try:
            if not self.driver or not self.recording_file:
                return False
            
            print("⏹️  Stopping screen recording...")
            
            # Stop recording and get base64 encoded video
            video_base64 = self.driver.stop_recording_screen()
            
            # Decode and save the video file
            print(f"💾 Saving recording...")
            with open(self.recording_file, 'wb') as f:
                f.write(base64.b64decode(video_base64))
            
            # Check if file was saved successfully
            if os.path.exists(self.recording_file) and os.path.getsize(self.recording_file) > 0:
                file_size = os.path.getsize(self.recording_file) / (1024 * 1024)  # MB
                print(f"✅ Recording saved: {self.recording_file}")
                print(f"   File size: {file_size:.2f} MB")
                return True
            else:
                print(f"⚠️  Recording file is empty or missing")
                return False
                
        except Exception as e:
            print(f"⚠️  Error stopping Appium recording: {e}")
            return False
    
    def start_recording(self):
        """Start screen recording using best available method"""
        print("\n" + "="*60)
        print("🎬 STARTING VIDEO RECORDING")
        print("="*60)
        
        # Try Appium method first (cleaner, no cleanup needed)
        if self.driver and self.start_screen_recording_appium():
            return True
        
        # Fallback to ADB method
        if self.start_screen_recording_adb():
            return True
        
        print("⚠️  Could not start recording with any method")
        return False
    
    def stop_recording(self):
        """Stop screen recording and save the file"""
        print("\n" + "="*60)
        print("🎬 STOPPING VIDEO RECORDING")
        print("="*60)
        
        # Try to stop based on which method was used
        if self.recording_process:
            # ADB method was used
            return self.stop_and_save_recording_adb()
        elif self.driver and self.recording_file:
            # Appium method was used
            return self.stop_and_save_recording_appium()
        else:
            print("⚠️  No active recording found")
            return False
    
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
        options.adb_exec_timeout = 180000  # Increased from 100000 to 180000 (3 minutes)
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
                error_msg = str(e)
                print(f"⚠️  Attempt {retry_count}/{max_retries} failed: {error_msg}")
                
                # If it's a timeout issue, suggest increasing timeout
                if 'timed out' in error_msg.lower() and 'install' in error_msg.lower():
                    print("💡 APK installation timeout detected - emulator is too slow")
                    print("   This usually resolves after emulator warms up")
                    # If we thought APKs were installed but got timeout, disable skip on retry
                    if appium_apks_installed and retry_count < max_retries:
                        print("   Disabling skip_server_installation for next attempt...")
                        options.skip_server_installation = False
                        options.skip_device_initialization = False
                
                if retry_count < max_retries:
                    # Exponential backoff: 30, 60, 90 seconds
                    wait_time = 30 * retry_count
                    print(f"⏳ Retrying in {wait_time} seconds...")
                    
                    # During wait, give emulator time to settle
                    if retry_count == 1:
                        print("   Allowing emulator to stabilize...")
                        # Do a simple ADB command to keep things active
                        self._run_adb_command(['shell', 'settings', 'get', 'global', 'animator_duration_scale'], timeout=10)
                    
                    time.sleep(wait_time)
                else:
                    print(f"❌ Failed to initialize Appium driver after {max_retries} attempts")
                    return False
    
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
            os.system('adb shell am start -n com.android.vending/com.android.vending.AssetBrowserActivity')
            time.sleep(5)
            print("✅ Play Store opened")
            return True
        except Exception as e:
            print(f"❌ Failed to open Play Store: {e}")
            return False
    
    def login_to_google_account(self):
        """Automate Google account login in Play Store"""
        print("\n" + "="*70)
        print("🔐 STARTING GOOGLE ACCOUNT LOGIN PROCESS")
        print("="*70)
        print(f"📧 Email to use: {self.email[:3]}...@{self.email.split('@')[1] if '@' in self.email else 'unknown'}")
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
                self._take_debug_screenshot("login_email_field_not_found")
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
                self._take_debug_screenshot("login_password_field_not_found")
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
            self._take_debug_screenshot("login_critical_error")
            print("="*70 + "\n")
            return False
    
    def _take_debug_screenshot(self, filename_prefix):
        """Take a debug screenshot and save it"""
        try:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            screenshot_dir = os.path.join(os.getcwd(), 'playstore_screenshots')
            os.makedirs(screenshot_dir, exist_ok=True)
            
            screenshot_path = os.path.join(screenshot_dir, f"{filename_prefix}_{timestamp}.png")
            self.driver.save_screenshot(screenshot_path)
            print(f"   📸 Debug screenshot saved: {screenshot_path}")
        except Exception as e:
            print(f"   ⚠️  Could not save screenshot: {e}")
    
    def search_and_install_app(self, app_name="Eptura Engage"):
        """Search for app and install it"""
        print("\n" + "="*70)
        print(f"🔍 STARTING APP SEARCH AND INSTALLATION")
        print("="*70)
        print(f"📱 App to search: {app_name}")
        
        try:
            # Click on search icon
            print("\n[Step 1/6] Opening search interface...")
            search_selectors = [
                ('search_bar_hint', 'new UiSelector().resourceId("com.android.vending:id/search_bar_hint")'),
                ('search_box_idle_text', 'new UiSelector().resourceId("com.android.vending:id/search_box_idle_text")'),
                ('Search description', 'new UiSelector().descriptionContains("Search")'),
                ('Search text', 'new UiSelector().textContains("Search")'),
                ('EditText class', 'new UiSelector().className("android.widget.EditText")')
            ]
            
            search_opened = False
            for selector_name, selector in search_selectors:
                try:
                    print(f"   🔍 Trying selector: {selector_name}")
                    search_icon = self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, selector)
                    search_icon.click()
                    time.sleep(3)
                    search_opened = True
                    print(f"   ✅ Search opened using: {selector_name}")
                    break
                except Exception as e:
                    print(f"   ⚠️  {selector_name} failed: {str(e)[:80]}")
                    continue
            
            if not search_opened:
                print("   ⚠️  Could not open search, trying to proceed anyway")
                self._take_debug_screenshot("search_open_failed")
            
            # Step 2: Type "Eptura Engage" in search field
            print(f"\n[Step 2/6] Typing search text: '{app_name}'...")
            search_field_selectors = [
                ('search_bar_text_input', 'new UiSelector().resourceId("com.android.vending:id/search_bar_text_input")'),
                ('search_box_text_input', 'new UiSelector().resourceId("com.android.vending:id/search_box_text_input")'),
                ('EditText class', 'new UiSelector().className("android.widget.EditText")'),
                ('focused element', 'new UiSelector().focused(true)')
            ]
            
            text_entered = False
            for selector_name, selector in search_field_selectors:
                try:
                    print(f"   🔍 Trying selector: {selector_name}")
                    search_field = self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, selector)
                    search_field.clear()
                    time.sleep(1)
                    # Type the app name character by character for better reliability
                    print(f"   ⌨️  Typing '{app_name}'...")
                    search_field.send_keys(app_name)
                    text_entered = True
                    print(f"   ✅ Text typed successfully: '{app_name}'")
                    time.sleep(2)
                    break
                except Exception as e:
                    print(f"   ⚠️  {selector_name} failed: {str(e)[:80]}")
                    continue
            
            if not text_entered:
                print("   ❌ FAILED: Could not type search text")
                self._take_debug_screenshot("search_text_entry_failed")
                print("="*70 + "\n")
                return False
            
            # Step 3: Press search button from keyboard (Enter key)
            print(f"\n[Step 3/6] Pressing search button from keyboard...")
            search_executed = False
            
            # Primary method: Press Enter key from keyboard using Appium
            try:
                print("   ⌨️  Pressing Enter key (KEYCODE_ENTER)...")
                self.driver.press_keycode(66)  # KEYCODE_ENTER - simulates keyboard search button
                print("   ✅ Search button pressed from keyboard")
                search_executed = True
                print("   ⏳ Waiting for search results to load...")
                time.sleep(5)
            except Exception as e:
                print(f"   ⚠️  Appium press_keycode failed: {str(e)[:80]}")
            
            # Fallback: Use ADB to press Enter key
            if not search_executed:
                try:
                    print("   ⌨️  Trying ADB input keyevent ENTER...")
                    result = self._run_adb_command(['shell', 'input', 'keyevent', 'KEYCODE_ENTER'])
                    if result and result.returncode == 0:
                        print("   ✅ Search button pressed via ADB")
                        search_executed = True
                        print("   ⏳ Waiting for search results to load...")
                        time.sleep(5)
                    else:
                        print(f"   ⚠️  ADB keyevent failed")
                except Exception as e:
                    print(f"   ⚠️  ADB method failed: {str(e)[:80]}")
            
            if not search_executed:
                print("   ⚠️  Could not press search button, trying to proceed anyway")
                self._take_debug_screenshot("search_button_press_failed")
                time.sleep(3)
            
            # Step 4: Wait for and click on the Eptura Engage app from search results
            print(f"\n[Step 4/6] Selecting '{app_name}' from search results...")
            app_clicked = False
            
            # Wait a bit more for results to fully load
            time.sleep(3)
            
            # Try multiple ways to find and click the app
            app_selectors = [
                (f'text:{app_name}', f'new UiSelector().textContains("{app_name}")'),
                (f'desc:{app_name}', f'new UiSelector().descriptionContains("{app_name}")'),
                ('text:Eptura', 'new UiSelector().textContains("Eptura")'),
                ('text:Condeco', 'new UiSelector().textContains("Condeco")'),
                ('li_title', 'new UiSelector().resourceId("com.android.vending:id/li_title")')
            ]
            
            for selector_name, selector in app_selectors:
                try:
                    print(f"   🔍 Looking for app with: {selector_name}")
                    app_item = self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, selector)
                    app_name_found = app_item.text if hasattr(app_item, 'text') else selector_name
                    print(f"   ✅ Found app: '{app_name_found}'")
                    app_item.click()
                    print(f"   ✅ Clicked on '{app_name_found}'")
                    time.sleep(5)
                    app_clicked = True
                    break
                except Exception as e:
                    print(f"   ⚠️  {selector_name} failed: {str(e)[:80]}")
                    continue
            
            if not app_clicked:
                print("   ⚠️  Could not find app in search results")
                self._take_debug_screenshot("app_not_found_in_results")
                print("   Trying to continue anyway...")
            
            # Step 5: Click Install button
            print(f"\n[Step 5/6] Clicking Install button...")
            install_clicked = False
            install_texts = ["Install", "INSTALL", "Update", "UPDATE", "Open", "OPEN", "Get"]
            
            for attempt in range(5):  # Try 5 times for better reliability
                print(f"   Attempt {attempt + 1}/5:")
                for text in install_texts:
                    try:
                        install_btn = self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,
                                                              f'new UiSelector().textContains("{text}").className("android.widget.Button")')
                        button_text = install_btn.text
                        
                        if button_text.upper() in ["OPEN"]:
                            print(f"      ✅ App is already installed! (found '{button_text}' button)")
                            print("="*70 + "\n")
                            return True
                        
                        print(f"      🔍 Found '{button_text}' button")
                        install_btn.click()
                        print(f"      ✅ Clicked '{button_text}' button")
                        install_clicked = True
                        time.sleep(3)
                        
                        # Handle any confirmation dialogs
                        print("      📱 Checking for confirmation dialogs...")
                        try:
                            continue_selectors = [
                                'new UiSelector().textContains("Continue")',
                                'new UiSelector().textContains("Accept")',
                                'new UiSelector().textContains("OK")',
                                'new UiSelector().textContains("Agree")'
                            ]
                            for selector in continue_selectors:
                                try:
                                    confirm_btn = self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, selector)
                                    confirm_btn.click()
                                    print(f"         ✅ Confirmed installation")
                                    time.sleep(2)
                                except:
                                    pass
                        except:
                            pass
                        
                        break
                    except Exception as e:
                        continue
                
                if install_clicked:
                    break
                    
                if attempt < 4:
                    print(f"   ⏳ Retrying after 3 seconds...")
                    time.sleep(3)
            
            if not install_clicked:
                print("   ❌ FAILED: Could not find or click Install button")
                self._take_debug_screenshot("install_button_not_found")
                print("="*70 + "\n")
                return False
            
            # Step 6: Wait until installation is complete
            print(f"\n[Step 6/6] Waiting for installation to complete...")
            print("   ⏳ Monitoring installation progress...")
            print("   (This may take several minutes depending on app size and network speed)")
            max_wait = 300  # 5 minutes
            wait_time = 0
            check_interval = 10
            last_status = ""
            
            while wait_time < max_wait:
                # Check for "Open" button - indicates installation is complete
                try:
                    open_btn = self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,
                                                       'new UiSelector().text("Open").className("android.widget.Button")')
                    print(f"\n✅ INSTALLATION COMPLETED SUCCESSFULLY!")
                    print(f"   Total time: {wait_time} seconds")
                    print(f"   Status: Open button detected - app is installed")
                    print("="*70 + "\n")
                    return True
                except:
                    pass
                
                # Check for progress indicators to show user what's happening
                try:
                    progress_selectors = [
                        'new UiSelector().textContains("Installing")',
                        'new UiSelector().textContains("Downloading")',
                        'new UiSelector().textContains("Pending")',
                        'new UiSelector().textContains("%")',
                        'new UiSelector().resourceId("com.android.vending:id/progress_bar")'
                    ]
                    
                    for selector in progress_selectors:
                        try:
                            progress_elem = self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, selector)
                            status_text = progress_elem.text if hasattr(progress_elem, 'text') else "In progress"
                            if status_text and status_text != last_status:
                                print(f"   📥 Status: {status_text}")
                                last_status = status_text
                            break
                        except:
                            continue
                except:
                    pass
                
                # Also check package manager directly
                result = self._run_adb_command(['shell', 'pm', 'list', 'packages', 'com.condecosoftware.condeco'], timeout=10)
                if result and 'com.condecosoftware.condeco' in result.stdout:
                    print(f"\n✅ INSTALLATION COMPLETED SUCCESSFULLY!")
                    print(f"   Total time: {wait_time} seconds")
                    print(f"   Status: App package detected in device package manager")
                    print("="*70 + "\n")
                    return True
                
                time.sleep(check_interval)
                wait_time += check_interval
                
                if wait_time % 30 == 0:
                    print(f"   ⏳ Still installing... ({wait_time}/{max_wait} seconds)")
            
            # Final verification after timeout
            print(f"\n⚠️  Installation timeout reached after {max_wait} seconds")
            print("   🔍 Performing final verification...")
            time.sleep(10)
            
            result = self._run_adb_command(['shell', 'pm', 'list', 'packages', 'com.condecosoftware.condeco'], timeout=10)
            if result and 'com.condecosoftware.condeco' in result.stdout:
                print("✅ Installation verified via package manager!")
                print("="*70 + "\n")
                return True
            
            print("❌ Installation failed - app was not installed within timeout period")
            self._take_debug_screenshot("installation_timeout")
            print("="*70 + "\n")
            return False
        except Exception as e:
            print(f"\n❌ CRITICAL ERROR during app installation: {e}")
            print(f"   Exception type: {type(e).__name__}")
            print(f"   Exception details: {str(e)}")
            self._take_debug_screenshot("install_critical_error")
            print("="*70 + "\n")
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
            max_wait = 360 if self.is_macos else (420 if self.is_windows else 360) # 6 min on macOS, 7 min on Windows
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
                        'new UiSelector().textContains("Pending")',
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
    print("=" * 70)
    print("🏪 Google Play Store Automated Installer")
    print(f"🖥️  Platform: {platform.system()}")
    print(f"🤖 Optimized for Android 15 (API 35)")
    print("=" * 70)
    
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
    
    # ============================================================================
    # STEP 1: VERIFY GOOGLE PLAY STORE IS INSTALLED
    # ============================================================================
    print("\n" + "=" * 70)
    print("📋 STEP 1: VERIFYING GOOGLE PLAY STORE INSTALLATION")
    print("=" * 70)
    
    try:
        print("🔍 Checking if Google Play Store app is installed on device...")
        print("   Package to check: com.android.vending")
        
        # Check for Play Store package
        result = subprocess.run(
            ['adb', 'shell', 'pm', 'list', 'packages', 'com.android.vending'],
            capture_output=True,
            text=True,
            timeout=10
        )
        
        if result.returncode == 0 and 'com.android.vending' in result.stdout:
            print("   ✅ Google Play Store is INSTALLED")
            print(f"   📦 Package found: {result.stdout.strip()}")
            
            # Get Play Store version
            try:
                version_result = subprocess.run(
                    ['adb', 'shell', 'dumpsys', 'package', 'com.android.vending', '|', 'grep', 'versionName'],
                    capture_output=True,
                    text=True,
                    timeout=10,
                    shell=True
                )
                if version_result.returncode == 0:
                    print(f"   📱 Version info: {version_result.stdout.strip()}")
            except:
                pass
                
        else:
            print("   ❌ Google Play Store is NOT INSTALLED")
            print("   ⚠️  The device may not have Google Play Services")
            print("   ⚠️  Installation will likely fail without Play Store")
            print(f"   📋 ADB response: {result.stdout if result.stdout else 'No output'}")
    except Exception as e:
        print(f"   ⚠️  Could not verify Play Store installation: {e}")
        print("   ⏩ Proceeding anyway...")
    
    print("=" * 70)
    
    # ============================================================================
    # STEP 2: CHECK IF TARGET APP IS ALREADY INSTALLED
    # ============================================================================
    print("\n" + "=" * 70)
    print("📋 STEP 2: CHECKING IF EPTURA ENGAGE APP IS ALREADY INSTALLED")
    print("=" * 70)
    
    target_package = "com.condecosoftware.condeco"
    print(f"🔍 Target app package: {target_package}")
    
    try:
        result = subprocess.run(
            ['adb', 'shell', 'pm', 'list', 'packages', target_package],
            capture_output=True,
            text=True,
            timeout=10
        )
        
        if result.returncode == 0 and target_package in result.stdout:
            print(f"   ✅ App is ALREADY INSTALLED")
            print(f"   📦 Package found: {result.stdout.strip()}")
            print("\n🎉 No installation needed! App is already present on device.")
            print("=" * 70)
            sys.exit(0)
        else:
            print(f"   ℹ️  App is NOT installed")
            print(f"   📋 Will proceed with installation from Play Store")
    except Exception as e:
        print(f"   ⚠️  Could not check app installation: {e}")
        print("   ⏩ Proceeding with installation...")
    
    print("=" * 70)
    
    # ============================================================================
    # STEP 3: INITIALIZE INSTALLER AND START INSTALLATION PROCESS
    # ============================================================================
    print("\n" + "=" * 70)
    print("📋 STEP 3: INITIALIZING PLAY STORE INSTALLER")
    print("=" * 70)
    
    installer = PlayStoreInstaller(email, password)
    installation_successful = False
    exit_code = 1
    
    try:
        # Start video recording early (before driver setup)
        print("\n🎬 Starting screen recording for debugging...")
        installer.start_recording()
        
        # ========================================================================
        # STEP 4: METHOD 1 - DIRECT DEEP LINK INSTALLATION
        # ========================================================================
        print("\n" + "=" * 70)
        print("📋 STEP 4: METHOD 1 - DIRECT DEEP LINK INSTALLATION")
        print("=" * 70)
        print("ℹ️  This method opens the app page directly in Play Store")
        print("ℹ️  Faster method, doesn't require login automation")
        print("=" * 70)
        
        if installer.install_via_deep_link(target_package):
            print("\n✅ Installation successful via Method 1!")
            installation_successful = True
            exit_code = 0
        else:
            print("\n⚠️  Method 1 failed, trying Method 2...")
            
            # ====================================================================
            # STEP 5: METHOD 2 - FULL PLAY STORE AUTOMATION WITH LOGIN
            # ====================================================================
            print("\n" + "=" * 70)
            print("📋 STEP 5: METHOD 2 - FULL PLAY STORE AUTOMATION")
            print("=" * 70)
            print("ℹ️  This method automates the complete Play Store flow:")
            print("    1. Setup Appium driver")
            print("    2. Open Play Store")
            print("    3. Login with Google credentials")
            print("    4. Search for app")
            print("    5. Install app")
            print("=" * 70)
            
            if not installer.setup_driver():
                print("❌ Failed to setup Appium driver")
                exit_code = 1
            else:
                # Start recording after driver is ready (if not already started)
                if not installer.recording_process and not installer.recording_file:
                    installer.start_recording()
                
                if not installer.open_play_store():
                    print("❌ Failed to open Play Store")
                    exit_code = 1
                else:
                    # Try to login (may already be logged in)
                    installer.login_to_google_account()
                    
                    # Search and install app
                    if installer.search_and_install_app(app_name):
                        print("\n✅ Installation successful via Method 2!")
                        installation_successful = True
                        exit_code = 0
                    else:
                        print("\n⚠️  Installation may not have completed")
                        exit_code = 1
            
    except Exception as e:
        print("\n" + "=" * 70)
        print("❌ UNEXPECTED ERROR DURING INSTALLATION")
        print("=" * 70)
        print(f"Error: {e}")
        import traceback
        traceback.print_exc()
        exit_code = 1
    finally:
        # ========================================================================
        # FINAL STEP: CLEANUP AND VERIFICATION
        # ========================================================================
        print("\n" + "=" * 70)
        print("📋 FINAL STEP: CLEANUP AND VERIFICATION")
        print("=" * 70)
        
        # Always stop recording and save video (especially important on failure for debugging)
        try:
            installer.stop_recording()
            
            if not installation_successful and installer.recording_file:
                # Provide clear message about where to find the recording for debugging
                actual_file = installer.recording_file[0] if isinstance(installer.recording_file, tuple) else installer.recording_file
                print(f"\n🎥 Video recording saved for debugging: {actual_file}")
                print(f"   Review this video to see what went wrong during installation")
        except Exception as e:
            print(f"⚠️  Could not stop recording properly: {e}")
        
        installer.cleanup()
        
        # Final verification
        print("\n🔍 Final verification - checking if app is now installed...")
        try:
            result = subprocess.run(
                ['adb', 'shell', 'pm', 'list', 'packages', target_package],
                capture_output=True,
                text=True,
                timeout=10
            )
            
            if result.returncode == 0 and target_package in result.stdout:
                print(f"✅ VERIFICATION SUCCESSFUL: App is installed!")
                print(f"   Package: {result.stdout.strip()}")
                installation_successful = True
                exit_code = 0
            else:
                print(f"❌ VERIFICATION FAILED: App is NOT installed")
                print(f"   Package searched: {target_package}")
                exit_code = 1
        except Exception as e:
            print(f"⚠️  Could not perform final verification: {e}")
        
        print("=" * 70)
        
        if installation_successful:
            print("\n🎉 INSTALLATION COMPLETED SUCCESSFULLY!")
        else:
            print("\n❌ INSTALLATION FAILED")
            print("📸 Check debug screenshots in: playstore_screenshots/")
            print("🎥 Check video recording in: playstore-recordings/")
        
        print("=" * 70)
    
    sys.exit(exit_code)


if __name__ == '__main__':
    main()
