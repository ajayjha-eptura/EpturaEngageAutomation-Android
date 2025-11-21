package appium.webdriver.extensions;

import io.appium.java_client.android.AndroidDriver;
import io.appium.java_client.service.local.AppiumDriverLocalService;
import io.appium.java_client.service.local.AppiumServiceBuilder;
import org.openqa.selenium.OutputType;
import org.openqa.selenium.TakesScreenshot;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.remote.DesiredCapabilities;
import com.aventstack.extentreports.MediaEntityBuilder;
import appium.webdriver.reporting.ExtentReportManager;
import java.time.Duration;
import java.io.File;
import java.text.SimpleDateFormat;
import java.util.Date;
import org.apache.commons.io.FileUtils;
import java.util.HashMap;
import java.util.Map;

public class DriverFactory {

    protected static AndroidDriver driver;
    private static AppiumDriverLocalService service;

    public static void startServer() {
        service = new AppiumServiceBuilder()
                .withIPAddress("127.0.0.1")
                .usingPort(4723)
                .withArgument(() -> "--session-override")
                .withTimeout(Duration.ofSeconds(60))
                .build();
        service.start();
    }

    public static void stopServer() {
        if (service != null) {
            service.stop();
        }
    }

    public static void createDriver() {
        try {
            if (driver == null) {
                if (service == null || !service.isRunning()) {
                    startServer();   
                }
                System.out.println("🚀 Creating new driver instance");
                DesiredCapabilities caps = new DesiredCapabilities();
                caps.setCapability("platformName", Utility.getProperty("platformName"));
                caps.setCapability("appium:deviceName", Utility.getProperty("deviceName"));
                caps.setCapability("appium:automationName", "UiAutomator2");
                caps.setCapability("appium:appPackage", Utility.getProperty("appPackage"));
                caps.setCapability("appium:appActivity", Utility.getProperty("appActivity"));
                
                // Set app launch parameters
                caps.setCapability("appium:noReset", true);  // Using noReset:true to keep app state between tests
                caps.setCapability("appium:forceAppLaunch", true);  // Force first app launch
                
                driver = new AndroidDriver(service.getUrl(), caps);
                
                // Add a short wait for app to stabilize
                Thread.sleep(2000);
                System.out.println("✅ Driver created successfully, app launched on: " + driver.currentActivity());
            } else {
                // Check if the app is still running
                String appPackage = Utility.getProperty("appPackage");
                boolean isAppRunning = false;
                
                try {
                    isAppRunning = driver.isAppInstalled(appPackage) && 
                                  (driver.queryAppState(appPackage).toString().equals("RUNNING_IN_FOREGROUND") || 
                                   driver.queryAppState(appPackage).toString().equals("RUNNING_IN_BACKGROUND"));
                } catch (Exception e) {
                    System.out.println("⚠️ Could not determine app state: " + e.getMessage());
                    isAppRunning = false;
                }
                
                if (!isAppRunning) {
                    System.out.println("🔄 App not running, activating app");
                    try {
                        driver.activateApp(appPackage);
                        Thread.sleep(2000);
                        System.out.println("✅ App reactivated on: " + driver.currentActivity());
                    } catch (Exception e) {
                        System.out.println("❌ Failed to activate app, recreating driver: " + e.getMessage());
                        quitDriver();
                        createDriver(); // Recursive call to create a new driver
                    }
                } else {
                    System.out.println("✅ Driver already exists and app is running on: " + driver.currentActivity());
                }
            }
        } catch (Exception e) {
            System.out.println("❌ Error in createDriver: " + e.getMessage());
            e.printStackTrace();
            // Clean up any partial initialization
            quitDriver();
            throw new RuntimeException("Failed to initialize driver: " + e.getMessage());
        }
    }
    
    public static boolean isDriverInitialized() {
        return driver != null;
    }
    
    public static WebDriver getDriver() {
        if (driver == null) {
            throw new IllegalStateException("❌ Driver is not initialized! Call createDriver() first.");
        }
        return driver;
    }

    public static void quitDriver() {
        if (driver != null) {
            driver.quit();
            driver = null;
        }
    }
    
    /**
     * Restarts the application by closing and relaunching it
     * Preserves the existing driver session but brings the app back to its initial state
     */
    public static void restartApp() {
        if (driver != null) {
            String appPackage = Utility.getProperty("appPackage");
            String appActivity = Utility.getProperty("appActivity");
            
            try {
                // Check current app state before restarting
                boolean needsRestart = true;
                
                try {
                    // Only restart if necessary - check app state first
                    String appState = driver.queryAppState(appPackage).toString();
                    String currentActivity = driver.currentActivity();
                    
                    System.out.println("Current app state: " + appState + ", activity: " + currentActivity);
                    
                    if (appState.equals("RUNNING_IN_FOREGROUND") && 
                       (currentActivity.contains("LoginActivity") || 
                        currentActivity.contains("DeskStartupActivity"))) {
                        // App is already running and on the correct screen - no need to restart
                        System.out.println("✅ App is already on correct screen, skipping restart");
                        needsRestart = false;
                    }
                } catch (Exception e) {
                    System.out.println("⚠️ Could not determine app state: " + e.getMessage());
                    // If we can't determine state, proceed with restart
                }
                
                if (needsRestart) {
                    System.out.println("🔄 Resetting app state for next test...");
                    
                    // Try gentler approach first - reset app state without terminating
                    try {
                        // Navigate directly to the start activity instead of terminating
                        Map<String, Object> args = new HashMap<>();
                        args.put("packageName", appPackage);
                        args.put("activity", appActivity);
                        driver.executeScript("mobile:startActivity", args);
                        
                        Thread.sleep(2000);
                        
                        // Verify we're on the correct screen
                        String currentActivity = driver.currentActivity();
                        if (!currentActivity.contains("LoginActivity") && !currentActivity.contains("DeskStartupActivity")) {
                            // If gentle approach failed, use more aggressive approach
                            throw new Exception("Gentle reset failed, activity is: " + currentActivity);
                        }
                        
                        System.out.println("✅ App state reset successfully, now on: " + currentActivity);
                    } catch (Exception e) {
                        // Gentle approach failed, use more aggressive restart
                        System.out.println("⚠️ Gentle reset failed, using full app restart: " + e.getMessage());
                        
                        // Close the app completely
                        driver.terminateApp(appPackage);
                        Thread.sleep(1000);
                        
                        // Restart the app
                        driver.activateApp(appPackage);
                        Thread.sleep(3000);
                        
                        System.out.println("✅ App restarted via terminate/activate, now on: " + driver.currentActivity());
                    }
                }
            } catch (Exception e) {
                System.out.println("❌ Error during app restart: " + e.getMessage());
                e.printStackTrace();
                
                // Try recovery once more
                try {
                    System.out.println("🔄 Attempting basic recovery...");
                    driver.activateApp(appPackage);
                    Thread.sleep(2000);
                    System.out.println("✅ Basic recovery successful");
                } catch (Exception e2) {
                    // If all else fails, try driver recreation
                    System.out.println("⚠️ Basic recovery failed, recreating driver as last resort");
                    try {
                        quitDriver();
                        createDriver();
                    } catch (Exception e3) {
                        throw new RuntimeException("Complete restart failure: " + e3.getMessage());
                    }
                }
            }
        } else {
            throw new IllegalStateException("❌ Driver is not initialized! Cannot restart app.");
        }
    }
    
    public static String captureScreenshot(String name) {
        if (driver == null) {
            throw new IllegalStateException("❌ Driver is not initialized! Cannot capture screenshot.");
        }
        
        try {
            // Create screenshots directory if it doesn't exist
            File screenshotsDir = new File("target/screenshots");
            if (!screenshotsDir.exists()) {
                screenshotsDir.mkdirs();
            }
            
            // Generate a unique filename using timestamp and sanitized test name
            String timestamp = new SimpleDateFormat("yyyyMMdd_HHmmss").format(new Date());
            String sanitizedName = name.replaceAll("[^a-zA-Z0-9-_\\.]", "_");
            String fileName = sanitizedName + "_" + timestamp + ".png";
            String filePath = "target/screenshots/" + fileName;
            
            // Take screenshot and save as file
            File scrFile = ((TakesScreenshot) driver).getScreenshotAs(OutputType.FILE);
            FileUtils.copyFile(scrFile, new File(filePath));
            
            // Also get base64 for return value to maintain compatibility
            String base64Screenshot = ((TakesScreenshot) driver).getScreenshotAs(OutputType.BASE64);
            
            // Add to report with the image file path
            ExtentReportManager.getTest().info("📸 Screenshot: " + name,
                    MediaEntityBuilder.createScreenCaptureFromPath("screenshots/" + fileName).build());
                    
            return base64Screenshot; // Return base64 for backward compatibility
        } catch (Exception e) {
            ExtentReportManager.getTest().warning("⚠️ Failed to capture screenshot: " + e.getMessage());
            return "";
        }
    }
}