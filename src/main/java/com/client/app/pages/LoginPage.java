package com.client.app.pages;
import appium.webdriver.extensions.DriverFactory;
import appium.webdriver.extensions.Utility;
import org.openqa.selenium.By;
import org.openqa.selenium.support.ui.ExpectedConditions;
import org.openqa.selenium.support.ui.WebDriverWait;
import java.time.Duration;

public class LoginPage extends DriverFactory {
   // Locators
   private final By EpturaURL = By.id("com.condecosoftware.condeco:id/editTextServerUrl");
   private final By UserCredentials_Screen=By.id("com.condecosoftware.condeco:id/title");
  // private final By passwordField = By.id("com.client.app:id/password");
   private final By Continue_btn=By.className("android.widget.Button");
   
   private final By Username_id=By.id("com.condecosoftware.condeco:id/username");
   private final By Password_id=By.id("com.condecosoftware.condeco:id/password");
  // private final By LocationPermissionCheck_id = By.id("android:id/alertTitle");
  // private final By OK_Button_Id= By.id("android:id/button1");
   // Fixed: Use proper locator for Today page - assuming it has a different identifier when logged in
   private final By Todaypage_Header = By.id("com.condecosoftware.condeco:id/username");
   private final By CalendarPage_Header = By.xpath("(//android.widget.TextView[@text=\"Calendar\"])[1]");
   private final By BookPage_Header = By.xpath("(//android.widget.TextView[@text=\"Book\"])[1]");
   private final By YourTeamPage_Header = By.xpath("(//android.widget.TextView[@text=\"Your team\"])[1]");
   private final By textInputErrorOnLogin_id = By.id("com.condecosoftware.condeco:id/textinput_error");
   private final By Profile_menu_btn = By.xpath("//android.widget.LinearLayout[@content-desc=\"Profile\"]/android.widget.ImageView");
   private final By logout_option = By.id("com.condecosoftware.condeco:id/logout");
   private final By logout_confirm = By.id("com.condecosoftware.condeco:id/core_dlg_positive_button");
  
   // method to ensure user is on login page
   public void ensureLoginPageIsDisplayed() {
        try {
            System.out.println("========================================");
            System.out.println("Ensuring user is on login page...");
            System.out.println("Current Activity: " + driver.currentActivity());
            System.out.println("========================================");
            
            // Give app time to settle after launch
            Thread.sleep(3000);
            
            // First, check if we're already on the login page (URL entry or credentials screen)
            boolean onUrlScreen = Utility.isElementPresent(EpturaURL, 5);
            boolean onCredentialsScreen = Utility.isElementPresent(UserCredentials_Screen, 10);
            
            System.out.println("Initial state check:");
            System.out.println("  - On URL screen: " + onUrlScreen);
            System.out.println("  - On credentials screen: " + onCredentialsScreen);
            
            if (onUrlScreen || onCredentialsScreen) {
                System.out.println("✅ Already on login page, no action needed");
                return;
            }
            
            // Not on login page - check if we're logged in (check for profile menu or toolbar)
            System.out.println("Not on login page, checking if user is logged in...");
            
            if (Utility.isElementPresent(Profile_menu_btn, 3) || Utility.isElementPresent(Todaypage_Header, 3) || Utility.isElementPresent(CalendarPage_Header, 3) || Utility.isElementPresent(BookPage_Header, 3) || Utility.isElementPresent(YourTeamPage_Header, 3)) {
                System.out.println("User already logged in, attempting logout...");
                performLogout();
                
                // After logout, wait for login page
                Thread.sleep(2000);
                if (Utility.isElementPresent(EpturaURL, 5) || Utility.isElementPresent(Username_id, 5 )) {
                    System.out.println("✅ Logout successful, now on login page");
                    return;
                }
            }
            
            // Still not on login page - restart the app
            System.out.println("Could not reach login page through logout, restarting app...");
            DriverFactory.restartApp();
            
            // After restart, wait longer for the app to initialize
            System.out.println("Waiting for app to initialize after restart...");
            Thread.sleep(5000);
            
            // Check again for login page elements with increased timeout
            System.out.println("Checking for login page elements after restart...");
            for (int i = 0; i < 3; i++) {
                System.out.println("Attempt " + (i + 1) + " - Current Activity: " + driver.currentActivity());
                
                if (Utility.isElementPresent(EpturaURL, 5)) {
                    System.out.println("✅ Found URL entry field on login page");
                    return;
                }
                
                if (Utility.isElementPresent(Username_id, 5)) {
                    System.out.println("✅ Found username field on login page");
                    return;
                }
                
                System.out.println("Login page not detected yet, waiting...");
                Thread.sleep(3000);
            }
            
            // Last resort - print page source for debugging
            System.out.println("❌ ERROR: Could not reach login page after all attempts");
            System.out.println("Current Activity: " + driver.currentActivity());
            System.out.println("Printing page source for debugging:");
            System.out.println(driver.getPageSource());
            
            throw new RuntimeException("Failed to navigate to login page after multiple attempts");
            
        } catch (InterruptedException e) {
            System.out.println("Thread interrupted: " + e.getMessage());
            Thread.currentThread().interrupt();
            throw new RuntimeException("Interrupted while ensuring login page: " + e.getMessage());
        } catch (Exception e) {
            System.out.println("❌ Error ensuring login page is displayed: " + e.getMessage());
            e.printStackTrace();
            throw new RuntimeException("Failed to navigate to login page: " + e.getMessage());
        }
    }
    
    // Helper method to perform logout
    private void performLogout() {
        try {
            System.out.println("Performing logout...");
            
            if (Utility.isElementPresent(Profile_menu_btn, 5)) {
                driver.findElement(Profile_menu_btn).click();
                System.out.println("Clicked Profile menu");
                Thread.sleep(1500);
                
                if (Utility.isElementPresent(logout_option, 5)) {
                    driver.findElement(logout_option).click();
                    System.out.println("Clicked Logout option");
                    Thread.sleep(1000);
                    
                    if (Utility.isElementPresent(logout_confirm, 5)) {
                        driver.findElement(logout_confirm).click();
                        System.out.println("Confirmed logout");
                        Thread.sleep(2000);
                    }
                }
            } else {
                System.out.println("Profile menu not found, cannot logout");
            }
        } catch (Exception e) {
            System.out.println("Logout failed: " + e.getMessage());
            throw new RuntimeException("Could not logout: " + e.getMessage());
        }
    }

   //CUMA-C226538 Perform Login with valid credential
   public void perform_Forms_Login(String serverName,String userName, String password) throws InterruptedException
	{
		try {
			System.out.println("========================================");
			System.out.println("Attempting to perform login...");
			System.out.println("Server: " + serverName + ", Username: " + userName);
			System.out.println("========================================");

            // Give app time to fully load and handle any initial popups
            System.out.println("⏳ Waiting for app to stabilize...");
            Thread.sleep(3000);
            
            // Handle any notifications or permission dialogs that might be blocking
            System.out.println("🔔 Checking for and dismissing any notifications...");
            Utility.handleAppNotifications();
            Thread.sleep(1000);

            // Check if we need to enter the URL or if we're already on the username/password screen
            // Use longer timeouts to handle slow loading
            boolean onUrlScreen = Utility.isElementPresent(EpturaURL, 10);
            boolean onCredentialsScreen = Utility.isElementPresent(Username_id, 10);
            
            System.out.println("Login flow state check:");
            System.out.println("  - On URL entry screen: " + onUrlScreen);
            System.out.println("  - On credentials screen: " + onCredentialsScreen);
            
            // If neither screen is detected, retry with longer waits
            if (!onUrlScreen && !onCredentialsScreen) {
                System.out.println("⚠️ Neither login screen detected, attempting recovery...");
                System.out.println("Current Activity: " + driver.currentActivity());
                
                // Handle notifications again in case they appeared
                Utility.handleAppNotifications();
                Thread.sleep(2000);
                
                // Retry detection with longer timeout
                for (int attempt = 1; attempt <= 3; attempt++) {
                    System.out.println("🔄 Retry attempt " + attempt + "/3...");
                    
                    onUrlScreen = Utility.isElementPresent(EpturaURL, 10);
                    onCredentialsScreen = Utility.isElementPresent(Username_id, 10);
                    
                    if (onUrlScreen || onCredentialsScreen) {
                        System.out.println("✅ Login screen detected on retry " + attempt);
                        break;
                    }
                    
                    // Handle any popups and wait before next retry
                    Utility.handleAppNotifications();
                    Thread.sleep(3000);
                }
                
                // If still not detected, print debug info and throw error
                if (!onUrlScreen && !onCredentialsScreen) {
                    System.out.println("❌ ERROR: Could not detect login screen after retries");
                    System.out.println("Current Activity: " + driver.currentActivity());
                    System.out.println("Page source for debugging:");
                    System.out.println("========================================");
                    System.out.println(driver.getPageSource());
                    System.out.println("========================================");
                    throw new RuntimeException("Cannot proceed with login - login screen not detected after multiple attempts");
                }
            }
            
            if (onCredentialsScreen) {
                // We're already on the username/password screen, skip URL entry
                System.out.println("✅ Already on credentials screen, skipping URL entry");
            } else if (onUrlScreen) {
                // We're on the URL entry screen, need to enter server name
                System.out.println("📝 On URL entry screen, entering server name...");
                WebDriverWait wait = new WebDriverWait(driver, Duration.ofSeconds(10));
                wait.until(ExpectedConditions.visibilityOfElementLocated(EpturaURL));
                
                driver.findElement(EpturaURL).click();
                Thread.sleep(2000);
                driver.findElement(EpturaURL).clear();
                Thread.sleep(2000);
                driver.findElement(EpturaURL).sendKeys(serverName);
                System.out.println("✅ Server name entered: " + serverName);
                
                // Wait a bit before hiding keyboard
                Thread.sleep(1000);
                
                try {
                    driver.hideKeyboard();
                    System.out.println("✅ Keyboard hidden");
                    Thread.sleep(1000);
                } catch (Exception keyboardEx) {
                    System.out.println("Keyboard already hidden or not shown");
                }
                
                Thread.sleep(500);
                System.out.println("🔘 Clicking Continue button...");
                driver.findElement(Continue_btn).click();
                System.out.println("✅ Continue button clicked");
                
                // Wait for transition to credentials screen
                System.out.println("⏳ Waiting for credentials screen to load...");
                System.out.println("Current Activity: " + driver.currentActivity());
                
                // First, wait for the URL entry screen to disappear
                // This is indicated by the EditText field no longer being present
                System.out.println("Waiting for URL screen to disappear...");
                Thread.sleep(2000);
                
                // Now wait for the username field to appear with a longer timeout
                System.out.println("Waiting for username field with explicit wait (30 seconds timeout)...");
                WebDriverWait usernameWait = new WebDriverWait(driver, Duration.ofSeconds(30));
                try {
                    usernameWait.until(ExpectedConditions.visibilityOfElementLocated(Username_id));
                    System.out.println("✅ Username field found - successfully transitioned to credentials screen");
                } catch (Exception e) {
                    System.out.println("⚠️ WARNING: Username field not found after URL submission!");
                    System.out.println("Current Activity: " + driver.currentActivity());
                    System.out.println("Attempting to find any EditText fields...");
                    
                    // Check if there are any EditText fields visible (might be on a different screen)
                    try {
                        if (Utility.isElementPresent(EpturaURL, 2)) {
                            System.out.println("Still on URL entry screen - clicking Continue again");
                            driver.findElement(Continue_btn).click();
                            Thread.sleep(3000);
                            usernameWait.until(ExpectedConditions.visibilityOfElementLocated(Username_id));
                        }
                    } catch (Exception retryEx) {
                        System.out.println("Retry failed. Printing page source for debugging:");
                        System.out.println("========================================");
                        System.out.println(driver.getPageSource());
                        System.out.println("========================================");
                        throw new RuntimeException("Cannot find username field after URL submission. Check page source above.", e);
                    }
                }
                
                Thread.sleep(1500); // Give UI time to stabilize after transition
            } else {
                // We're on neither screen - this is an error state
                System.out.println("❌ ERROR: Not on URL screen or credentials screen.");
                System.out.println("Current Activity: " + driver.currentActivity());
                System.out.println("Printing page source:");
                System.out.println(driver.getPageSource());
                throw new RuntimeException("Cannot proceed with login - app is in unexpected state");
            }
            
            // At this point, we should be on the credentials screen
            System.out.println("========================================");
            System.out.println("📝 Entering credentials...");
            System.out.println("========================================");
            
            // Ensure username field is still visible and interactable
            WebDriverWait credWait = new WebDriverWait(driver, Duration.ofSeconds(15));
            credWait.until(ExpectedConditions.visibilityOfElementLocated(Username_id));
            credWait.until(ExpectedConditions.elementToBeClickable(Username_id));
            
            driver.findElement(Username_id).click();
            Thread.sleep(500);
            driver.findElement(Username_id).clear();
            Thread.sleep(300);
            driver.findElement(Username_id).sendKeys(userName);
            System.out.println("✅ Username entered");
            Thread.sleep(500);
            
            // Ensure password field is visible
            credWait.until(ExpectedConditions.visibilityOfElementLocated(Password_id));
            driver.findElement(Password_id).click();
            Thread.sleep(500);
            driver.findElement(Password_id).clear();
            Thread.sleep(300);
            driver.findElement(Password_id).sendKeys(password);
            System.out.println("✅ Password entered");
            Thread.sleep(800);
            
            try {
                driver.hideKeyboard();
                System.out.println("✅ Keyboard hidden after password entry");
                Thread.sleep(800);
            } catch (Exception keyboardEx) {
                System.out.println("Keyboard already hidden");
            }
            
            Thread.sleep(500);
            System.out.println("🔘 Submitting login credentials...");
            driver.findElement(Continue_btn).click();
            System.out.println("✅ Login credentials submitted successfully");
            System.out.println("========================================");
            

            // Wait for page to load after login submission
            System.out.println("⏳ Waiting for page to load after login...");
            Thread.sleep(0300); // Initial wait for transition to start
            
            // Wait for login screen to disappear (username field should not be visible)
            WebDriverWait postLoginWait = new WebDriverWait(driver, Duration.ofSeconds(30));
            try {
                postLoginWait.until(ExpectedConditions.invisibilityOfElementLocated(Username_id));
                System.out.println("✅ Login screen disappeared - page is loading");
            } catch (Exception waitEx) {
                System.out.println("⚠️ Username field still visible after login submission");
            }
            
            // Additional wait for the home screen to start appearing
            Thread.sleep(5000); // Allow time for home screen elements to initialize
            System.out.println("✅ Page load wait completed, ready for notification handling");
            System.out.println("========================================");
            
		} catch (Exception e) {
			System.out.println("========================================");
			System.out.println("❌ ERROR during login: " + e.getMessage());
			System.out.println("========================================");
			e.printStackTrace();
			throw e;
		}
	}
	
	public Boolean verify_invalid_login()
	{
		System.out.println("========================================");
		System.out.println("Verifying invalid login - checking for error messages...");
		System.out.println("========================================");
		
		try {
			// First, check if we're still on the login screen (expected for invalid login)
			boolean onLoginScreen = Utility.isElementPresent(Username_id, 3) || 
			                        Utility.isElementPresent(Password_id, 3) ||
			                        Utility.isElementPresent(EpturaURL, 3);
			
			System.out.println("On login screen: " + onLoginScreen);
			
			// Try to find the textinput_error element first
			if (Utility.isElementPresent(textInputErrorOnLogin_id, 30)) {
				String returnStringMessage = Utility.getTextFromid(textInputErrorOnLogin_id, 10);
				System.out.println("Found error message: " + returnStringMessage);
				if(returnStringMessage.contains("You are not authorized to login") || 
				   returnStringMessage.contains("Please check your user name and password") ||
				   returnStringMessage.contains("Invalid") ||
				   returnStringMessage.contains("incorrect") ||
				   returnStringMessage.contains("failed")) {
					System.out.println("✅ Authentication error message verified");
					return true;
				}
			}
			
			// Alternative: Check for toast messages or dialog with error
			By toastMessage = By.xpath("//*[contains(@text, 'not authorized') or contains(@text, 'Invalid') or contains(@text, 'incorrect') or contains(@text, 'failed') or contains(@text, 'error')]");
			if (Utility.isElementPresent(toastMessage, 5)) {
				System.out.println("✅ Found error toast/dialog message");
				return true;
			}
			
			// Alternative: Check for snackbar error
			By snackbarError = By.id("com.condecosoftware.condeco:id/snackbar_text");
			if (Utility.isElementPresent(snackbarError, 5)) {
				String snackbarText = Utility.getTextFromid(snackbarError, 3);
				System.out.println("Found snackbar message: " + snackbarText);
				return true;
			}
			
			// If we're still on login screen after submission, that also indicates login failed
			if (onLoginScreen) {
				System.out.println("✅ Still on login screen after submission - login was rejected");
				return true;
			}
			
			System.out.println("❌ Could not verify invalid login - no error message found and not on login screen");
			// Print page source for debugging
			System.out.println("Current page source:");
			System.out.println(DriverFactory.getDriver().getPageSource());
			return false;
			
		} catch (Exception e) {
			System.out.println("Error during invalid login verification: " + e.getMessage());
			return false;
		}
	}
	
	public void verify_Valid_Login()
	{
		System.out.println("========================================");
		System.out.println("Verifying successful login...");
		System.out.println("========================================");
		
		Utility.handleAppNotifications();
		try {
			// Wait for the app to settle after login
			Thread.sleep(3000);
			
			// Check for home screen indicators (positive verification)
			boolean onHomeScreen = false;
			
			// Check for various home screen elements
			if (Utility.isElementPresent(Todaypage_Header, 5)) {
				System.out.println("✅ Found  Today page header - user is logged in and is on Today page");
				onHomeScreen = true;
			
			}
			
			// Also verify we're NOT on login screen anymore
			boolean notOnLoginScreen = !Utility.isElementPresent(EpturaURL, 2) && 
			                           !Utility.isElementPresent(Password_id, 2);
			
			System.out.println("On home screen: " + onHomeScreen);
			System.out.println("Not on login screen: " + notOnLoginScreen);
			
			if (onHomeScreen || notOnLoginScreen) {
				System.out.println("✅ User successfully logged in");
			} else {
				System.out.println("❌ Login verification failed");
				System.out.println("Current activity: " + driver.currentActivity());
				System.out.println("Page source:");
				System.out.println(driver.getPageSource());
				throw new AssertionError("Login appears to have failed - still on login screen");
			}
		} catch (AssertionError e) {
			throw e;
		} catch (Exception e) {
			System.out.println("Login verification failed: " + e.getMessage());
			throw new AssertionError("Login verification failed: " + e.getMessage());
		}
	}

	}