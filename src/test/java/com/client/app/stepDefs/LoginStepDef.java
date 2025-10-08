package com.client.app.stepDefs;
import com.client.app.pages.LoginPage;
import appium.webdriver.extensions.Utility;
import io.cucumber.java.en.Given;
import io.cucumber.java.en.When;
import io.cucumber.java.en.Then;
import java.net.MalformedURLException;

import org.testng.Assert;


public class LoginStepDef {
	
   private final LoginPage loginPage = new LoginPage();
   
	String getServerName = Utility.getProperty("mobile.app.login.servername");
	String getUserName = Utility.getProperty("mobile.app.login.username");
	String getPassword = Utility.getProperty("mobile.app.login.password");
	
   @Given("User is on Login page")
   public void UserLogin() throws MalformedURLException, InterruptedException
	{
		System.out.println("App Launched");
		// Ensure we're on the login page by checking for login elements or logging out if needed
		loginPage.ensureLoginPageIsDisplayed();
	}
   
	@When("User performs Forms Login")
	public void User_performs_Forms_Login() throws InterruptedException
	{
		loginPage.perform_Forms_Login(getServerName, getUserName, getPassword);
	}
   
	
	@When("^User attempts Forms Login with wrong password as \"([^\"]*)\"$")
	public void user_performs_Forms_Login_with_invalid_credentials(String incorrectpassword) throws InterruptedException
	{
		loginPage.perform_Forms_Login(getServerName, getUserName, incorrectpassword);
	}
	
	
	@Then("Verify authentication failed message")
	public void verify_invalid_Forms_login()
	{
		Assert.assertTrue(loginPage.verify_invalid_login());
		//The Assert.assertTrue() method will pass the test if verify_invalid_login() returns true and fail if it returns false.
	}
	
	@Then("User successfully logged-in")
	public void verify_UserLogin()
	{
		
		loginPage.verify_Valid_Login();

	}
}