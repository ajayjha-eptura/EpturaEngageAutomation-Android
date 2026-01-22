$filePath = "src\main\java\com\client\app\pages\LoginPage.java"
$content = Get-Content $filePath -Raw

# Check if method already exists
if ($content -match "waitForCredentialsDialog") {
    Write-Host "Method waitForCredentialsDialog already exists in the file."
    exit 0
}

# The new method to add
$newMethod = @"

   /**
    * Wait for the credentials dialog to appear and become interactive.
    * This is crucial because the credentials popup appears inside a dialog hierarchy
    * (android:id/parentPanel, android:id/custom, etc.) and we need to wait for it to be fully rendered.
    * @param timeoutSeconds Maximum time to wait for the dialog
    * @return true if the credentials dialog is found and interactive, false otherwise
    */
   private boolean waitForCredentialsDialog(int timeoutSeconds) {
       System.out.println("Waiting for credentials dialog to appear and become interactive...");
       
       long startTime = System.currentTimeMillis();
       long endTime = startTime + (timeoutSeconds * 1000L);
       
       By dialogParentPanel = By.id("android:id/parentPanel");
       By dialogCustom = By.id("android:id/custom");
       By dialogContent = By.id("android:id/content");
       
       int attemptCount = 0;
       
       while (System.currentTimeMillis() < endTime) {
           attemptCount++;
           try {
               System.out.println("  Attempt " + attemptCount + " - Checking for credentials dialog...");
               
               boolean dialogFound = false;
               try {
                   if (Utility.isElementPresent(dialogParentPanel, 1)) {
                       System.out.println("    Found dialog parent panel");
                       dialogFound = true;
                   } else if (Utility.isElementPresent(dialogCustom, 1)) {
                       System.out.println("    Found dialog custom container");
                       dialogFound = true;
                   } else if (Utility.isElementPresent(dialogContent, 1)) {
                       System.out.println("    Found dialog content container");
                       dialogFound = true;
                   }
               } catch (Exception e) { }
               
               if (isAnyUsernameLocatorPresent(2)) {
                   WebElement usernameField = findUsernameField();
                   if (usernameField != null) {
                       boolean isDisplayed = usernameField.isDisplayed();
                       boolean isEnabled = usernameField.isEnabled();
                       
                       System.out.println("    Username field found - displayed: " + isDisplayed + ", enabled: " + isEnabled);
                       
                       if (isDisplayed && isEnabled) {
                           try {
                               String bounds = usernameField.getAttribute("bounds");
                               System.out.println("    Username field bounds: " + bounds);
                               
                               if (bounds != null && !bounds.isEmpty()) {
                                   System.out.println("  Credentials dialog is fully loaded and interactive!");
                                   Thread.sleep(500);
                                   return true;
                               }
                           } catch (Exception boundsEx) {
                               System.out.println("  Credentials dialog appears ready");
                               Thread.sleep(500);
                               return true;
                           }
                       }
                   }
               }
               
               Thread.sleep(2000);
               
           } catch (InterruptedException ie) {
               Thread.currentThread().interrupt();
               System.out.println("  Wait interrupted");
               return false;
           } catch (Exception e) {
               System.out.println("    Check failed: " + e.getMessage());
               try {
                   Thread.sleep(2000);
               } catch (InterruptedException ie) {
                   Thread.currentThread().interrupt();
                   return false;
               }
           }
       }
       
       long elapsedSeconds = (System.currentTimeMillis() - startTime) / 1000;
       System.out.println("  Credentials dialog not found after " + elapsedSeconds + " seconds");
       return false;
   }
"@

# Replace the final closing brace with the new method + closing brace
$content = $content -replace '\r?\n\}\s*$', "`r`n$newMethod`r`n}"

$content | Set-Content $filePath -Encoding UTF8 -NoNewline
Write-Host "Successfully added waitForCredentialsDialog method to LoginPage.java"
