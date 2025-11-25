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
                print("⚠️  No recording process found")
                return False
            
            print("⏹️  Stopping screen recording...")
            
            # Get the device path before terminating
            local_path, device_path = self.recording_file
            
            # Send SIGINT (Ctrl+C) to gracefully stop recording instead of terminate
            # This allows screenrecord to properly finalize the video file
            try:
                print("   Sending stop signal to recording process...")
                # On Unix-like systems (macOS), use SIGINT for graceful shutdown
                if self.is_macos:
                    import signal
                    self.recording_process.send_signal(signal.SIGINT)
                else:
                    # On Windows, terminate is the best option
                    self.recording_process.terminate()
            except Exception as e:
                print(f"   ⚠️  Error sending signal: {e}")
                # Fallback to terminate
                try:
                    self.recording_process.terminate()
                except:
                    pass
            
            # Wait for process to complete with timeout
            print("⏳ Waiting for recording process to finish...")
            try:
                self.recording_process.wait(timeout=10)
                print("   ✅ Recording process completed")
            except subprocess.TimeoutExpired:
                print("   ⚠️  Recording process didn't exit cleanly, forcing termination...")
                self.recording_process.kill()
                try:
                    self.recording_process.wait(timeout=5)
                except:
                    pass
            
            # CRITICAL FIX: Wait much longer for the file to be fully written and closed on device
            # Slow emulators need significant time to flush buffers and finalize the video
            print("⏳ Waiting for recording to finalize on device (this may take up to 45 seconds)...")
            time.sleep(45)  # Increased from 30 to 45 seconds - critical for macOS-hosted emulators
            
            # Check if file exists on device with retries
            print(f"🔍 Checking if recording file exists on device...")
            file_found = False
            file_size_bytes = 0
            
            for check_attempt in range(15):  # Increased from 10 to 15 attempts
                check_result = self._run_adb_command(['shell', 'ls', '-lh', device_path], timeout=30)
                if check_result and check_result.returncode == 0:
                    file_info = check_result.stdout.strip()
                    print(f"✅ Recording file found on device: {file_info}")
                    
                    # Extract file size to verify it's not empty or still being written
                    try:
                        # Parse size from ls output (format varies but size is typically 5th field)
                        parts = file_info.split()
                        if len(parts) >= 5:
                            size_str = parts[4]
                            # Convert human-readable size to bytes for comparison
                            if 'K' in size_str:
                                file_size_bytes = float(size_str.replace('K', '')) * 1024
                            elif 'M' in size_str:
                                file_size_bytes = float(size_str.replace('M', '')) * 1024 * 1024
                            elif 'G' in size_str:
                                file_size_bytes = float(size_str.replace('G', '')) * 1024 * 1024 * 1024
                            else:
                                try:
                                    file_size_bytes = float(size_str)
                                except:
                                    file_size_bytes = 0
                            
                            print(f"   📊 File size: {size_str} ({file_size_bytes:.0f} bytes)")
                            
                            # File must be at least 1KB to be considered valid
                            if file_size_bytes > 1024:
                                file_found = True
                                break
                            else:
                                print(f"   ⚠️  File too small ({file_size_bytes:.0f} bytes), may still be writing...")
                    except Exception as parse_error:
                        print(f"   ⚠️  Could not parse file size: {parse_error}")
                
                if check_attempt < 14:
                    wait_time = 5 if check_attempt < 7 else 10  # Increase wait time after 7 attempts
                    print(f"   ⏳ File not ready yet, waiting {wait_time}s... (attempt {check_attempt + 1}/15)")
                    time.sleep(wait_time)
            
            if not file_found:
                print(f"⚠️  Recording file not found or invalid on device: {device_path}")
                # Try to find any recent recordings as fallback
                print("🔍 Searching for any screen recordings on device...")
                search_result = self._run_adb_command(['shell', 'find', '/sdcard/', '-name', '*.mp4', '-type', 'f'], timeout=30)
                if search_result and search_result.returncode == 0:
                    print(f"   Found files:\n{search_result.stdout}")
                return False
            
            # Create target directory if it doesn't exist
            os.makedirs(os.path.dirname(local_path), exist_ok=True)
            
            # Pull the recording from device with aggressive retries
            print(f"📥 Pulling recording from device...")
            max_pull_attempts = 15  # Increased from 10 to 15
            pull_successful = False
            
            for attempt in range(max_pull_attempts):
                print(f"   Pull attempt {attempt + 1}/{max_pull_attempts}...")
                
                # Add a small delay before each pull attempt to ensure file is stable
                if attempt > 0:
                    time.sleep(5)
                
                # Use explicit adb pull command with longer timeout
                result = self._run_adb_command(['pull', device_path, local_path], timeout=240)
                
                if result and result.returncode == 0:
                    # Verify the pulled file actually has content
                    if os.path.exists(local_path):
                        local_size = os.path.getsize(local_path)
                        if local_size > 1024:  # At least 1KB
                            print(f"✅ Successfully pulled recording from device ({local_size} bytes)")
                            pull_successful = True
                            break
                        else:
                            print(f"⚠️  Pulled file is too small ({local_size} bytes), retrying...")
                            try:
                                os.remove(local_path)
                            except:
                                pass
                    else:
                        print(f"⚠️  Pulled file doesn't exist at {local_path}")
                else:
                    if result:
                        error_msg = result.stderr.strip() if result.stderr else "Unknown error"
                        stdout_msg = result.stdout.strip() if result.stdout else ""
                        print(f"⚠️  Pull attempt {attempt + 1} failed:")
                        if error_msg:
                            print(f"      Error: {error_msg}")
                        if stdout_msg:
                            print(f"      Output: {stdout_msg}")
                    else:
                        print(f"⚠️  Pull attempt {attempt + 1} failed: Command timeout")
                
                if attempt < max_pull_attempts - 1:
                    wait_time = 5 if attempt < 7 else 10
                    print(f"   ⏳ Retrying in {wait_time} seconds...")
                    time.sleep(wait_time)
            
            if not pull_successful:
                print("❌ Failed to pull recording after all attempts")
                # Don't clean up device file - leave it for manual inspection
                print(f"💡 Recording may still be on device at: {device_path}")
                print("   You can manually pull it later with:")
                print(f"   adb pull {device_path} {local_path}")
                return False
            
            # Clean up device file
            print("🧹 Cleaning up device file...")
            self._run_adb_command(['shell', 'rm', device_path], timeout=30)
            
            # Verify local file exists and has content
            if os.path.exists(local_path):
                file_size = os.path.getsize(local_path)
                if file_size > 0:
                    file_size_mb = file_size / (1024 * 1024)  # MB
                    print(f"✅ Recording saved successfully!")
                    print(f"   📁 Location: {local_path}")
                    print(f"   📊 File size: {file_size_mb:.2f} MB")
                    return True
                else:
                    print(f"⚠️  Recording file is empty (0 bytes): {local_path}")
                    return False
            else:
                print(f"⚠️  Recording file not found at: {local_path}")
                return False
                
        except Exception as e:
            print(f"⚠️  Error stopping ADB recording: {e}")
            import traceback
            traceback.print_exc()
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
        print("🏪 METHOD 2: INSTALL PLAY STORE + FULL AUTOMATION")
        print("="*70)
        print("ℹ️  This fallback method will:")
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
            
            # Step 5: Search for the app
            print(f"\n[Step 5/6] Searching for '{app_name}'...")
            
            # Open search
            search_opened = False
            search_selectors = [
                ('search_bar_hint', 'new UiSelector().resourceId("com.android.vending:id/search_bar_hint")'),
                ('search_box_idle_text', 'new UiSelector().resourceId("com.android.vending:id/search_box_idle_text")'),
                ('Search description', 'new UiSelector().descriptionContains("Search")'),
            ]
            
            for selector_name, selector in search_selectors:
                try:
                    print(f"   🔍 Opening search with: {selector_name}")
                    search_icon = self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, selector)
                    search_icon.click()
                    time.sleep(3)
                    search_opened = True
                    print(f"   ✅ Search opened")
                    break
                except:
                    continue
            
            if not search_opened:
                print("   ❌ Could not open search")
                return False
            
            # Type app name
            print(f"   ⌨️  Typing '{app_name}'...")
            search_field_selectors = [
                ('search_bar_text_input', 'new UiSelector().resourceId("com.android.vending:id/search_bar_text_input")'),
                ('EditText class', 'new UiSelector().className("android.widget.EditText")'),
            ]
            
            text_entered = False
            for selector_name, selector in search_field_selectors:
                try:
                    search_field = self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, selector)
                    search_field.clear()
                    time.sleep(1)
                    search_field.send_keys(app_name)
                    text_entered = True
                    print(f"   ✅ Typed '{app_name}'")
                    time.sleep(2)
                    break
                except:
                    continue
            
            if not text_entered:
                print("   ❌ Could not type search text")
                return False
            
            # Press Enter
            print("   🔍 Executing search...")
            try:
                self.driver.press_keycode(66)  # KEYCODE_ENTER
                time.sleep(5)
                print("   ✅ Search executed")
            except:
                try:
                    self._run_adb_command(['shell', 'input', 'keyevent', 'KEYCODE_ENTER'])
                    time.sleep(5)
                    print("   ✅ Search executed via ADB")
                except:
                    print("   ⚠️  Could not press Enter")
            
            # Check for crash after search
            if self._handle_app_crash_dialog():
                print("   🔧 Handled crash after search, continuing...")
                time.sleep(3)
            
            # Step 6: Click on the app from search results
            print(f"\n[Step 6/6] Clicking on '{app_name}' in results...")
            
            # Wait for results
            time.sleep(5)
            self._take_debug_screenshot("fallback_method_search_results")
            
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
            self._take_debug_screenshot("fallback_method_app_page")
            
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
                        return self._wait_for_installation("com.condecosoftware.condeco")
                    except:
                        continue
                
                if attempt < 4:
                    print(f"   ⏳ Retrying... (attempt {attempt + 2}/5)")
                    time.sleep(5)
            
            print("   ❌ Could not find or click Install button")
            return False
            
        except Exception as e:
            print(f"\n❌ Error in fallback method: {e}")
            import traceback
            traceback.print_exc()
            self._take_debug_screenshot("fallback_method_error")
            return False

    def search_and_install_app(self, app_name="Eptura Engage"):
        """Search for app and install it"""
        print("\n" + "="*70)
        print(f"🔍 STARTING APP SEARCH AND INSTALLATION")
        print("="*70)
        print(f"📱 App to search: {app_name}")
        
        try:
            # PRIORITY 1: Try browser-style search method (user's preferred method)
            print("\n🌐 METHOD 1: BROWSER-STYLE SEARCH (Recommended)")
            if self._search_via_browser_method(app_name, max_retries=3):
                print("✅ Browser-style search installation succeeded!")
                return True
            
            print("\n⚠️  Browser-style search didn't complete, trying fallback method...\n")
            
            # PRIORITY 2: Install Play Store (if needed) + Full Automation
            print("\n🏪 METHOD 2: INSTALL PLAY STORE + FULL AUTOMATION (Fallback)")
            if self._install_playstore_and_retry(app_name):
                print("✅ Fallback method installation succeeded!")
                return True
            
            print("\n⚠️  Fallback method didn't complete, trying direct URL method...\n")
            
            # PRIORITY 3: Try direct URL approach
            print("\n🚀 METHOD 3: DIRECT URL METHOD")
            if self._install_via_url("com.condecosoftware.condeco"):
                print("✅ Direct URL installation succeeded!")
                return True
            
            print("⚠️  Direct URL method didn't complete, trying traditional search method...\n")
            
            # PRIORITY 4: Traditional Play Store search (final fallback)
            print("\n🔍 METHOD 4: TRADITIONAL PLAY STORE SEARCH (Final Fallback)")
            
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
            time.sleep(5)  # Increased from 3
            
            # CRITICAL FIX: Scroll down to load more results
            print("   📜 Scrolling to load all search results...")
            for scroll_attempt in range(3):
                try:
                    self.driver.swipe(500, 1500, 500, 500, 500)
                    time.sleep(2)
                    print(f"      Scrolled {scroll_attempt + 1}/3")
                except:
                    pass
            
            # Try multiple ways to find and click the app
            app_selectors = [
                (f'text:{app_name}', f'new UiSelector().textContains("{app_name}")'),
                (f'desc:{app_name}', f'new UiSelector().descriptionContains("{app_name}")'),
                ('text:Eptura', 'new UiSelector().textContains("Eptura")'),
                ('text:Condeco', 'new UiSelector().textContains("Condeco")'),
                ('li_title', 'new UiSelector().resourceId("com.android.vending:id/li_title")'),
                # NEW: Try finding by scrolling through list items
                ('scrollable_item', 'new UiScrollable(new UiSelector().scrollable(true)).scrollIntoView(new UiSelector().textContains("Eptura"))')
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
                print("   Trying direct package URL as fallback...")
                # Fallback to direct URL if search fails
                if self._install_via_url("com.condecosoftware.condeco"):
                    return True
                print("   ❌ All methods failed")
                return False
            
            # Step 5: Click Install button
            print(f"\n[Step 5/6] Clicking Install button...")
            install_clicked = False
            install_texts = ["Install", "INSTALL", "Update", "UPDATE", "Open", "OPEN", "Get"]
            
            # CRITICAL FIX: Wait longer for app page to fully load after clicking from search results
            print("   ⏳ Waiting for app detail page to fully load (15 seconds)...")
            time.sleep(15)  # Increased from 5 to 15 seconds
            
            # Take a screenshot before trying to find Install button
            self._take_debug_screenshot("before_install_button_search")
            
            for attempt in range(10):  # Increased from 5 to 10 attempts
                print(f"   Attempt {attempt + 1}/10:")
                
                # First, verify we're on the app detail page
                try:
                    # Look for app name or package name on the page
                    page_check = self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,
                                                         'new UiSelector().textContains("Eptura")')
                    print(f"      ✅ On app detail page (found: {page_check.text if hasattr(page_check, 'text') else 'Eptura'})")
                except:
                    print(f"      ⚠️  May not be on app detail page, retrying...")
                    self._take_debug_screenshot(f"not_on_app_page_attempt_{attempt + 1}")
                    time.sleep(5)
                    continue
                
                # Try to find Install button with multiple strategies
                for text in install_texts:
                    try:
                        # Strategy 1: Text + Button class
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
                        break
                    except:
                        pass
                    
                    # Strategy 2: Just text match (no class restriction)
                    try:
                        install_btn = self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,
                                                              f'new UiSelector().text("{text}")')
                        button_text = install_btn.text
                        
                        if button_text.upper() in ["OPEN"]:
                            print(f"      ✅ App is already installed! (found '{button_text}' button)")
                            print("="*70 + "\n")
                            return True
                        
                        print(f"      🔍 Found '{button_text}' button (strategy 2)")
                        install_btn.click()
                        print(f"      ✅ Clicked '{button_text}' button")
                        install_clicked = True
                        time.sleep(3)
                        break
                    except:
                        pass
                    
                    # Strategy 3: Use resource ID (for newer Play Store versions)
                    try:
                        install_btn = self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,
                                                              'new UiSelector().resourceIdMatches(".*install.*|.*action_button.*")')
                        button_text = install_btn.text if hasattr(install_btn, 'text') else text
                        
                        if button_text and button_text.upper() in ["OPEN"]:
                            print(f"      ✅ App is already installed! (found '{button_text}' button)")
                            print("="*70 + "\n")
                            return True
                        
                        print(f"      🔍 Found button via resource ID: '{button_text}'")
                        install_btn.click()
                        print(f"      ✅ Clicked button via resource ID")
                        install_clicked = True
                        time.sleep(3)
                        break
                    except:
                        pass
                
                if install_clicked:
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
                
                if attempt < 9:
                    # Take screenshot before retry to see what's on screen
                    self._take_debug_screenshot(f"install_button_not_found_attempt_{attempt + 1}")
                    wait_time = 5 if attempt < 5 else 8  # Longer waits after 5 attempts
                    print(f"   ⏳ Retrying after {wait_time} seconds...")
                    time.sleep(wait_time)
            
            if not install_clicked:
                print("   ❌ FAILED: Could not find or click Install button")
                self._take_debug_screenshot("install_button_not_found_final")
                
                # Last resort: Try to dump the UI hierarchy for debugging
                try:
                    print("   🔍 Attempting to get page source for debugging...")
                    page_source = self.driver.page_source
                    debug_file = os.path.join(os.getcwd(), 'playstore_screenshots', 'page_source_debug.xml')
                    with open(debug_file, 'w', encoding='utf-8') as f:
                        f.write(page_source)
                    print(f"   📄 Page source saved to: {debug_file}")
                except Exception as e:
                    print(f"   ⚠️  Could not save page source: {e}")
                
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
    
    def _handle_app_crash_dialog(self):
        """Handle 'app isn't responding' or crash dialogs"""
        try:
            crash_texts = [
                "isn't responding",
                "has stopped",
                "Close app",
                "Wait",
                "OK"
            ]
            
            for text in crash_texts:
                try:
                    # Look for crash dialog
                    crash_dialog = self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,
                        f'new UiSelector().textContains("{text}")')
                    
                    if crash_dialog:
                        print(f"   ⚠️  Found crash dialog: '{text}'")
                        
                        # Try to click "Close app" button
                        close_buttons = ["Close app", "Close", "OK"]
                        for btn_text in close_buttons:
                            try:
                                close_btn = self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,
                                    f'new UiSelector().text("{btn_text}")')
                                close_btn.click()
                                print(f"   ✅ Clicked '{btn_text}' button")
                                time.sleep(3)
                                return True
                            except:
                                continue
                        
                        return True
                except:
                    continue
            
            return False
        except:
            return False
    
    def _search_via_browser_method(self, app_name="Eptura Engage", max_retries=3):
        """