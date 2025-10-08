package appium.webdriver.extensions;

import io.appium.java_client.service.local.AppiumDriverLocalService;

import io.appium.java_client.service.local.AppiumServiceBuilder;

import io.appium.java_client.service.local.flags.GeneralServerFlag;

import java.io.File;

public class AppiumServerManager {

    private static AppiumDriverLocalService service;

    /**

     * Start Appium server programmatically

     */

    public static void startServer() {

        if (service == null || !service.isRunning()) {

            service = new AppiumServiceBuilder()

                    // ✅ Path to Appium main.js

                    .withAppiumJS(new File(System.getenv("APPIUM_PATH") != null ?

                            System.getenv("APPIUM_PATH") :

                            "C:\\Users\\AjayJha\\AppData\\Roaming\\npm\\node_modules\\appium\\build\\lib\\main.js"))

                    .withIPAddress("127.0.0.1")   // localhost

                    .usingPort(4723)              // default Appium port

                    .withArgument(GeneralServerFlag.SESSION_OVERRIDE) 

                    .withArgument(GeneralServerFlag.LOG_LEVEL, "info") 

                    .build();

            service.start();

            System.out.println("✅ Appium server started at: " + service.getUrl());

        }

    }

    /**

     * Stop Appium server

     */

    public static void stopServer() {

        if (service != null && service.isRunning()) {

            service.stop();

            System.out.println("🛑 Appium server stopped");

        }

    }

    /**

     * Get the service URL (to use in DriverFactory)

     */

    public static String getServiceUrl() {

        if (service != null) {

            return service.getUrl().toString();

        }

        throw new IllegalStateException("❌ Appium service not running. Start it first!");

    }

    /**

     * Get Appium service instance

     */

    public static AppiumDriverLocalService getService() {

        return service;

    }

}
 