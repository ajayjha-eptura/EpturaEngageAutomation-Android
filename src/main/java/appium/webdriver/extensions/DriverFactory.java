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
import java.net.URL;
import java.net.MalformedURLException;
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
    private static final String APPIUM_SERVER_URL = System.getenv().getOrDefault("APPIUM_SERVER_URL", "http://127.0.0.1:4723");
    private static final boolean USE_EXTERNAL_APPIUM = Boolean.parseBoolean(System.getenv().getOrDefault("USE_EXTERNAL_APPIUM", "false"));

    public static void startServer() {
        // Only start local server if not using external Appium
        if (USE_EXTERNAL_APPIUM) {
            System.out.println("ℹ️  Using external Appium server at: " + APPIUM_SERVER_URL);
            return;
        }
        
        if (service == null || !service.isRunning()) {
            System.out.println("🚀 Starting local Appium server...");
            service = new AppiumServiceBuilder()
                    .withIPAddress("127.0.0.1")
                    .usingPort(4723)
                    .withArgument(() -> "--session-override")
                    .withTimeout(Duration.ofSeconds(60))
                    .build();
            service.start();
            System.out.println("✅ Local Appium server started");
        }
    }

    public static void stopServer() {
        // Only stop local server if we started it
        if (!USE_EXTERNAL_APPIUM && service != null) {
            System.out.println("🛑 Stopping local Appium server...");
            service.stop();
            System.out.println("✅ Local Appium server stopped");
        }
    }

    public static void createDriver() {
        try {
            if (driver == null) {
                System.out.println("🚀 Creating new driver instance");
                
                // Start server if needed (will skip if using external)
                if (!USE_EXTERNAL_APPIUM && (service == null || !service.isRunning())) {
                    startServer();   
                }
                
                DesiredCapabilities caps = new DesiredCapabilities();
                caps.setCapability("platformName", Utility.getProperty("platformName"));
                caps.setCapability("appium:deviceName", Utility.getProperty("deviceName"));
                caps.setCapability("appium:automationName", "UiAutomator2");
                caps.setCapability("appium:appPackage", Utility.getProperty("appPackage"));
                caps.setCapability("appium:appActivity", Utility.getProperty("appActivity"));
                
                // Set app launch parameters
                caps.setCapability("appium:noReset", true);
                caps.setCapability("appium:forceAppLaunch", true);
                
                // Connect to appropriate Appium server
                URL appiumUrl;
                try {
                    if (USE_EXTERNAL_APPIUM) {
                        appiumUrl = new URL(APPIUM_SERVER_URL);
                        System.out.println("📡 Connecting to external Appium server: " + APPIUM_SERVER_URL);
                    } else {
                        appiumUrl = service.getUrl();
                        System.out.println("📡 Connecting to local Appium server: " + appiumUrl);
                    }
                } catch (MalformedURLException e) {
                    throw new RuntimeException("Invalid Appium server URL: " + APPIUM_SERVER_URL, e);
                }
                
                driver = new AndroidDriver(appiumUrl, caps);
                
                Thread.sleep(2000);
                System.out.println("✅ Driver created successfully, app launched on: " + driver.currentActivity());
            } else {
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
                        createDriver();
                    }
                } else {
                    System.out.println("✅ Driver already exists and app is running on: " + driver.currentActivity());
                }
            }
        } catch (Exception e) {
            System.out.println("❌ Error in createDriver: " + e.getMessage());
            e.printStackTrace();
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
    
    public static void restartApp() {
        if (driver != null) {
            String appPackage = Utility.getProperty("appPackage");
            String appActivity = Utility.getProperty("appActivity");
            
            try {
                boolean needsRestart = true;
                
                try {
                    String appState = driver.queryAppState(appPackage).toString();
                    String currentActivity = driver.currentActivity();
                    
                    System.out.println("Current app state: " + appState + ", activity: " + currentActivity);
                    
                    if (appState.equals("RUNNING_IN_FOREGROUND") && 
                       (currentActivity.contains("LoginActivity") || 
                        currentActivity.contains("DeskStartupActivity"))) {
                        System.out.println("✅ App is already on correct screen, skipping restart");
                        needsRestart = false;
                    }
                } catch (Exception e) {
                    System.out.println("⚠️ Could not determine app state: " + e.getMessage());
                }
                
                if (needsRestart) {
                    System.out.println("🔄 Resetting app state for next test...");
                    
                    try {
                        Map<String, Object> args = new HashMap<>();
                        args.put("packageName", appPackage);
                        args.put("activity", appActivity);
                        driver.executeScript("mobile:startActivity", args);
                        
                        Thread.sleep(2000);
                        
                        String currentActivity = driver.currentActivity();
                        if (!currentActivity.contains("LoginActivity") && !currentActivity.contains("DeskStartupActivity")) {
                            throw new Exception("Gentle reset failed, activity is: " + currentActivity);
                        }
                        
                        System.out.println("✅ App state reset successfully, now on: " + currentActivity);
                    } catch (Exception e) {
                        System.out.println("⚠️ Gentle reset failed, using full app restart: " + e.getMessage());
                        
                        driver.terminateApp(appPackage);
                        Thread.sleep(1000);
                        
                        driver.activateApp(appPackage);
                        Thread.sleep(3000);
                        
                        System.out.println("✅ App restarted via terminate/activate, now on: " + driver.currentActivity());
                    }
                }
            } catch (Exception e) {
                System.out.println("❌ Error during app restart: " + e.getMessage());
                e.printStackTrace();
                
                try {
                    System.out.println("🔄 Attempting basic recovery...");
                    driver.activateApp(appPackage);
                    Thread.sleep(2000);
                    System.out.println("✅ Basic recovery successful");
                } catch (Exception e2) {
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
            File screenshotsDir = new File("target/screenshots");
            if (!screenshotsDir.exists()) {
                screenshotsDir.mkdirs();
            }
            
            String timestamp = new SimpleDateFormat("yyyyMMdd_HHmmss").format(new Date());
            String sanitizedName = name.replaceAll("[^a-zA-Z0-9-_\\.]", "_");
            String fileName = sanitizedName + "_" + timestamp + ".png";
            String filePath = "target/screenshots/" + fileName;
            
            File scrFile = ((TakesScreenshot) driver).getScreenshotAs(OutputType.FILE);
            FileUtils.copyFile(scrFile, new File(filePath));
            
            // Get Base64 screenshot for embedding in Extent report
            String base64Screenshot = ((TakesScreenshot) driver).getScreenshotAs(OutputType.BASE64);
            
            // Use Base64 image embedding instead of file path for CI/CD compatibility
            // This ensures screenshots display correctly in pipeline reports
            ExtentReportManager.getTest().info("📸 Screenshot: " + name,
                    MediaEntityBuilder.createScreenCaptureFromBase64String(base64Screenshot).build());
                    
            return base64Screenshot;
        } catch (Exception e) {
            ExtentReportManager.getTest().warning("⚠️ Failed to capture screenshot: " + e.getMessage());
            return "";
        }
    }
}