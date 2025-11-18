package appium.webdriver.extensions;
import appium.webdriver.reporting.ExtentReportManager;
import io.cucumber.java.*;
import java.util.concurrent.atomic.AtomicInteger;

public class Hooks {
   private static boolean isLastTest = false;
   private static final AtomicInteger scenarioCounter = new AtomicInteger(0);
   private static final AtomicInteger completedScenarios = new AtomicInteger(0);
   private static boolean appStarted = false;
   
   @BeforeAll
   public static void beforeAll() {
       ExtentReportManager.initReports();
       DriverFactory.startServer();   // ✅ Start Appium server once
       scenarioCounter.set(0);
       completedScenarios.set(0);
       appStarted = false;
   }
   
   @Before
   public void beforeScenario(Scenario scenario) throws Exception {
       // Count scenarios to better manage app lifecycle
       int currentScenario = scenarioCounter.incrementAndGet();
       System.out.println("📊 Starting scenario #" + currentScenario + ": " + scenario.getName());
       
       // Create a new test report entry
       ExtentReportManager.createTest(scenario.getName());
       ExtentReportManager.getTest().info("🚀 Starting scenario: " + scenario.getName());
       
       try {
           // Only create a driver once for all tests
           DriverFactory.createDriver();
           
           // Track that we've started the app at least once
           if (!appStarted) {
               appStarted = true;
               System.out.println("📱 App started for the first time");
           }
           
           // Short wait for UI to stabilize
           Thread.sleep(1000);
       } catch (Exception e) {
           // Log the exception
           ExtentReportManager.getTest().fail("❌ Driver initialization failed: " + e.getMessage());
           // Mark scenario as failed
           scenario.log("Driver initialization failed: " + e.getMessage());
           scenario.attach(e.getMessage().getBytes(), "text/plain", "Error Details");
           throw e; // Re-throw to ensure TestNG marks the test as failed
       }
   }
   
   @After
   public void afterScenario(Scenario scenario) {
       try {
           // Count completed scenarios
           int completed = completedScenarios.incrementAndGet();
           boolean isActuallyLastScenario = completed >= scenarioCounter.get() || isLastTest;
           
           System.out.println("📊 Completed scenario #" + completed + " out of " + scenarioCounter.get());
           
           // Only attempt to capture screenshot if driver was initialized
           if (DriverFactory.isDriverInitialized()) {
               String screenshotName = scenario.isFailed() ? "Failed_" + scenario.getName() : "Passed_" + scenario.getName();
               // Our updated captureScreenshot method now saves the file and adds it to the report automatically
               DriverFactory.captureScreenshot(screenshotName);
               
               if (scenario.isFailed()) {
                   ExtentReportManager.getTest().fail("❌ Scenario Failed: " + scenario.getName());
               } else {
                   // Log a passing message
                   ExtentReportManager.getTest().pass("✅ Scenario Passed: " + scenario.getName());
               }
               
               // Only restart app if this is not the last scenario and we have more tests to run
               if (!isActuallyLastScenario) {
                   // Restart the app for next test with retry logic
                   ExtentReportManager.getTest().info("🔄 Preparing app for next test...");
                   restartAppWithRetry(1);  // Reduced retry count to minimize restarts
               } else {
                   ExtentReportManager.getTest().info("✅ Final test completed, skipping app restart");
                   System.out.println("✅ All tests completed, skipping app restart");
               }
           } else if (!scenario.isFailed()) {
               // If driver is not initialized but scenario is not marked as failed, mark it as failed
               ExtentReportManager.getTest().fail("❌ Scenario Failed: Driver was never initialized");
               scenario.log("Driver was never initialized");
           }
       } catch (Exception e) {
           ExtentReportManager.getTest().fail("❌ Error during cleanup: " + e.getMessage());
           e.printStackTrace(); // Print stack trace for better debugging
           // If app restart fails even after retries, quit driver and create a new one
           try {
               System.out.println("🔄 Final fallback: Quitting driver and creating new session");
               DriverFactory.quitDriver();
               // Don't create a new driver here as it will be created in the next @Before
           } catch (Exception e2) {
               System.out.println("❌ Final cleanup failed: " + e2.getMessage());
           }
       }
   }

   /**
    * Attempt to restart the app with retry logic
    *
    */
   private void restartAppWithRetry(int maxRetries) {
       int retryCount = 0;
       boolean success = false;
       
       while (!success && retryCount < maxRetries) {
           try {
               ExtentReportManager.getTest().info("🔄 Restarting app for next test... (Attempt " + (retryCount + 1) + ")");
               DriverFactory.restartApp();
               success = true;
           } catch (Exception e) {
               retryCount++;
               System.out.println("❌ App restart attempt " + retryCount + " failed: " + e.getMessage());
               if (retryCount >= maxRetries) {
                   System.out.println("⚠️ Max restarts reached, continuing without restart");
                   break;  // Continue execution instead of throwing exception
               }
               
               try {
                   // Wait before next retry
                   Thread.sleep(1000);
               } catch (InterruptedException ie) {
                   Thread.currentThread().interrupt();
               }
           }
       }
   }

   // Method to be called from TestRunner to indicate when we're on the last test
   public static void setLastTest(boolean isLast) {
       isLastTest = isLast;
       if (isLast) {
           System.out.println("🏁 Final test execution phase marked");
       }
   }

   @AfterAll
   public static void afterAll() {
       // Reset counters
       scenarioCounter.set(0);
       completedScenarios.set(0);
       
       // Clean up resources
       System.out.println("🧹 Cleaning up resources and quitting driver");
       if (DriverFactory.isDriverInitialized()) {
           DriverFactory.quitDriver();
       }
       DriverFactory.stopServer();   // ✅ Stop Appium service
       ExtentReportManager.flushReports();
   }
}