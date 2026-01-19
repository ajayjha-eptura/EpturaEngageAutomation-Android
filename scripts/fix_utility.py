#!/usr/bin/env python3
"""Script to fix the Utility.java file for CI/CD compatibility"""

content = '''package appium.webdriver.extensions;
import org.openqa.selenium.By;
import org.openqa.selenium.NoSuchElementException;
import org.openqa.selenium.TimeoutException;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.support.ui.ExpectedConditions;
import org.openqa.selenium.support.ui.WebDriverWait;
import java.io.InputStream;
import java.io.IOException;
import java.time.Duration;
import java.util.Properties;
public class Utility {
    private static Properties properties;
    static {
        try {
            // Use classpath-based resource loading instead of file path
            // This works both locally and in CI/CD pipeline
            InputStream inputStream = Utility.class.getClassLoader().getResourceAsStream("Config.properties");
            if (inputStream == null) {
                // Fallback: try alternative filename (lowercase)
                inputStream = Utility.class.getClassLoader().getResourceAsStream("config.properties");
            }
            if (inputStream == null) {
                throw new RuntimeException("Could not find Config.properties in classpath. Ensure the file exists in src/main/resources/");
            }
            properties = new Properties();
            properties.load(inputStream);
            inputStream.close();
            System.out.println("Config.properties loaded successfully from classpath");
        } catch (IOException e) {
            e.printStackTrace();
            throw new RuntimeException("Could not load config.properties file: " + e.getMessage());
        }
    }
    public static String getProperty(String key) {
        return properties.getProperty(key);
    }
    public static WebElement waitForElementUntilPresent(By locator, int timeoutInSeconds) {
        WebDriverWait wait = new WebDriverWait(DriverFactory.getDriver(), Duration.ofSeconds(timeoutInSeconds));
        return wait.until(ExpectedConditions.presenceOfElementLocated(locator));
    }
    public static void clickElement(By locator, int timeoutInSeconds) {
        WebElement element = waitForElementUntilPresent(locator, timeoutInSeconds);
        element.click();
    }
    public static void sendKeys(By locator, String text, int timeoutInSeconds) {
        WebElement element = waitForElementUntilPresent(locator, timeoutInSeconds);
        element.clear();
        element.sendKeys(text);
    }
    public static String getTextFromid(By locator, int timeoutInSeconds) {
        WebElement element = waitForElementUntilPresent(locator, timeoutInSeconds);
        String value = element.getText();
        return value;
    }
    /**
     * Checks if an element is present on the page within the specified timeout.
     */
    public static boolean isElementPresent(By locator, int timeoutInSeconds) {
        try {
            WebDriverWait wait = new WebDriverWait(DriverFactory.getDriver(), Duration.ofSeconds(timeoutInSeconds));
            wait.until(ExpectedConditions.presenceOfElementLocated(locator));
            return true;
        } catch (NoSuchElementException | TimeoutException e) {
            return false;
        }
    }
    /**
     * Handles and dismisses app-specific and system-level notifications.
     * This method will try to click the buttons for both notifications in a loop.
     */
    public static void handleAppNotifications() {
        System.out.println("Checking for and handling app notifications...");
        // Define the locators for the notifications
        By appNotificationAllowButton = By.id("com.android.permissioncontroller:id/permission_allow_button");
        By automaticCheckInCancelButton = By.id("com.condecosoftware.condeco:id/buttonCancelAutomaticCheckIn");

        // Loop a few times to handle potential race conditions
        for (int i = 0; i < 3; i++) {
            try {
                // Check for system notification
                if (isElementPresent(appNotificationAllowButton, 5)) {
                    clickElement(appNotificationAllowButton, 5);
                    System.out.println("Allowed App to send notifications");
                }

                // Check for app-specific notification
                if (isElementPresent(automaticCheckInCancelButton, 5)) {
                    clickElement(automaticCheckInCancelButton, 5);
                    System.out.println("Automatic Check-In notification dismissed.");
                }

                // If neither notification is present, we can break the loop
                if (!isElementPresent(appNotificationAllowButton, 1) && !isElementPresent(automaticCheckInCancelButton, 1)) {
                    break;
                }

            } catch (Exception e) {
                // Catch any exception and continue the loop
                System.out.println("Notification handling attempt failed: " + e.getMessage());
            }
        }
    }
}
'''

import os
script_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.dirname(script_dir)
target_file = os.path.join(project_dir, 'src', 'main', 'java', 'appium', 'webdriver', 'extensions', 'Utility.java')

with open(target_file, 'w', encoding='utf-8') as f:
    f.write(content)

print(f"Successfully fixed: {target_file}")
