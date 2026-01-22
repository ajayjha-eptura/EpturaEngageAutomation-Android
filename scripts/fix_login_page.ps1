$filePath = "src\main\java\com\client\app\pages\LoginPage.java"
$lines = Get-Content $filePath

$newLines = @()
$skipLines = 0
$i = 0

while ($i -lt $lines.Count) {
    if ($skipLines -gt 0) {
        $skipLines--
        $i++
        continue
    }
    
    # Find the line with "Now wait for the username field"
    if ($lines[$i] -match "// Now wait for the username field to appear with a longer timeout") {
        # Add the new code instead
        $newLines += "                // Now wait for the credentials dialog to appear and become interactive"
        $newLines += "                // This is crucial because the credentials popup appears inside a dialog hierarchy"
        $newLines += "                // (android:id/parentPanel, android:id/custom, etc.) and we need to wait for it to be fully rendered"
        $newLines += '                System.out.println("Waiting for credentials dialog with waitForCredentialsDialog (60 seconds timeout)...");'
        $newLines += ""
        $newLines += "                // Use the waitForCredentialsDialog method to wait for dialog container and ensure fields are interactive"
        $newLines += "                boolean usernameFound = waitForCredentialsDialog(60);"
        
        # Skip the old lines (the manual loop - approximately 9 lines)
        $skipLines = 8
        $i++
        continue
    }
    
    $newLines += $lines[$i]
    $i++
}

$newLines | Set-Content $filePath -Encoding UTF8
Write-Host "File updated successfully!"
