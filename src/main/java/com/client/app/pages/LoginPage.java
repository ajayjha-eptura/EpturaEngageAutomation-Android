package com.client.app.pages;
import appium.webdriver.extensions.DriverFactory;
import appium.webdriver.extensions.Utility;
import org.openqa.selenium.By;
public class LoginPage extends DriverFactory {
   // Locators
   private final By EpturaURL = By.className("android.widget.EditText");
  // private final By passwordField = By.id("com.client.app:id/password");
   private final By Continue_btn=By.className("android.widget.Button");
   private final By Username_id=By.id("com.condecosoftware.condeco:id/username");
   private final By Password_id=By.id("com.condecosoftware.condeco:id/password");
  // private final By LocationPermissionCheck_id = By.id("android:id/alertTitle");
  // private final By OK_Button_Id= By.id("android:id/button1");
   private final By Todaypage_Header = By.id("com.condecosoftware.condeco:id/username");
   private final By textInputErrorOnLogin_id = By.id("com.condecosoftware.condeco:id/textinput_error");
   private final By Profile_menu_btn = By.xpath("//android.widget.LinearLayout[@content-desc=\"Profile\"]/android.widget.ImageView");
   private final By logout_option = By.id("com.condecosoftware.condeco:id/logout");
   private final By logout_confirm = By.id("com.condecosoftware.condeco:id/core_dlg_positive_button");
  
   // method to ensure user is on login page
   public void ensureLoginPageIsDisplayed() {
        try {
            // Check if already on login page by looking for URL field
            if (Utility.isElementPresent(EpturaURL, 3)) {
                System.out.println("User is already on login page");
                return;
            }
            
            // Check if user is logged in
            if (Utility.isElementPresent(Todaypage_Header, 3)) {
                System.out.println("User is already logged in, logging out first");
                // Perform logout
                Utility.waitForElementUntilPresent(Profile_menu_btn, 5);
                driver.findElement(Profile_menu_btn).click();
                
                Utility.waitForElementUntilPresent(logout_option, 5);
                driver.findElement(logout_option).click();
                
                // Confirm logout if prompted
                if (Utility.isElementPresent(logout_confirm, 3)) {
                    driver.findElement(logout_confirm).click();
                }
                
                // Wait for login page
                Utility.waitForElementUntilPresent(EpturaURL, 10);
            }
            
            // If neither login page nor logged in state detected
            if (!Utility.isElementPresent(EpturaURL, 5)) {
                System.out.println("Could not detect login page elements, app may be in unexpected state");
                // Force restart the app to reset state
                DriverFactory.restartApp();
                Utility.waitForElementUntilPresent(EpturaURL, 10);
            }
        } catch (Exception e) {
            System.out.println("Error ensuring login page is displayed: " + e.getMessage());
            e.printStackTrace();
        }
    }
   
   //CUMA-C226538 Perform Login with valid credential
   public void perform_Forms_Login(String serverName,String userName, String password) throws InterruptedException
	{
		try {
			Utility.waitForElementUntilPresent (Todaypage_Header,10);
			if(driver.findElement(Todaypage_Header).isDisplayed())
			{
				System.out.println(" User already Logged-in");
			}
		} catch (Exception e) {
			Utility.waitForElementUntilPresent(EpturaURL,10);
			driver.findElement(EpturaURL).click();
			driver.findElement(EpturaURL).clear();
			driver.findElement(EpturaURL).sendKeys(serverName);
			driver.hideKeyboard();
			driver.findElement(Continue_btn).click();
			
			Utility.waitForElementUntilPresent(Username_id,10);
			driver.findElement(Username_id).sendKeys(userName);
			driver.findElement(Password_id).sendKeys(password);
			driver.findElement(Continue_btn).click();
			//Utility.handleAppNotifications();
			
		}
	}
	
	public Boolean verify_invalid_login()
	{
	
		Utility.waitForElementUntilPresent(textInputErrorOnLogin_id,30);
		String returnStringMessage = Utility.getTextFromid(textInputErrorOnLogin_id,10);
		if(returnStringMessage.contains("You are not authorized to login. Please check your user name and password."))
		{
			return true;
		}
		return false;
	}
	
	public void verify_Valid_Login()
	
	{
		Utility.handleAppNotifications();
		try {
			Utility.waitForElementUntilPresent(Todaypage_Header,30);
			if(driver.findElement(Todaypage_Header).isDisplayed())
			{
				System.out.println("User successfully logged in");
			}
		} catch (Exception e) {
			System.out.println("Login failed: " + e.getMessage());
			throw new AssertionError("Login verification failed: " + e.getMessage());
		}
	}
}