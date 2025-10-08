package appium.webdriver.reporting;

import com.aventstack.extentreports.ExtentReports;

import com.aventstack.extentreports.ExtentTest;

import com.aventstack.extentreports.reporter.ExtentSparkReporter;

public class ExtentReportManager {

    private static ExtentReports extent;

    private static ThreadLocal<ExtentTest> test = new ThreadLocal<>();

    public static void initReports() {
    	   if (extent == null) {
    	       ExtentSparkReporter reporter = new ExtentSparkReporter("target/Extent-report.html");
    	       reporter.config().setReportName("Eptura Engage Automation Report");
    	       reporter.config().setDocumentTitle("Automation Execution Report");
    	       extent = new ExtentReports();
    	       extent.attachReporter(reporter);
    	       extent.setSystemInfo("Project", "Eptura Engage");
    	       extent.setSystemInfo("Platform", "Android");
    	       extent.setSystemInfo("Tester", "Ajay Jha");
    	   }
    	}
    public static void createTest(String testName) {

        ExtentTest extentTest = extent.createTest(testName);

        test.set(extentTest);

    }

    public static ExtentTest getTest() {

        return test.get();

    }

    public static void flushReports() {

        if (extent != null) {

            extent.flush();

        }

    }
    

}
 