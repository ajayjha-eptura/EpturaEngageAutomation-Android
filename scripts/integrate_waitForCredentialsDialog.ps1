$filePath = "src\main\java\com\client\app\pages\LoginPage.java"
$content = Get-Content $filePath -Raw

# Check if method exists first
if (-not ($content -match "waitForCredentialsDialog")) {
    Write-Host "ERROR: waitForCredentialsDialog method not found in the file. Please run add_waitForCredentialsDialog.ps1 first."
    exit 1
}

# Check if already integrated
if ($content -match "waitForCredentialsDialog\(60\)") {
    Write-Host "waitForCredentialsDialog is already integrated into perform_Forms_Login method."
    exit 0
}

# The old code pattern to find and replace
$oldPattern = @"
                // Now wait for the username field to appear with a longer timeout
                System.out.println\("Waiting for username field with explicit wait \(60 seconds timeout\)\.\.\."\);
                
                // Wait up to 60 seconds for any username locator to appear
                boolean usernameFound = false;
                for \(int waitAttempt = 0; waitAttempt < 30; waitAttempt\+\+\) \{
                    if \(isAnyUsernameLocatorPresent\(2\)\) \{
                        usernameFound = true;
                        System\.out\.println\("✅ Username field found - successfully transitioned to credentials screen"\);
                        break;
                    \}
                    Thread\.sleep\(2000\);
                \}
"@

# New code to replace it with
$newCode = @"
                // Use the dedicated method to wait for credentials dialog to be fully interactive
                System.out.println("Waiting for credentials dialog with dedicated wait method (60 seconds timeout)...");
                boolean usernameFound = waitForCredentialsDialog(60);
"@

# Try to find and replace the pattern
if ($content -match "// Now wait for the username field to appear with a longer timeout") {
    Write-Host "Found the target section. Replacing with waitForCredentialsDialog call..."
    
    # Use a simpler replacement approach - find the block and replace it
    $content = $content -replace `
        '// Now wait for the username field to appear with a longer timeout\s+System\.out\.println\("Waiting for username field with explicit wait \(60 seconds timeout\)\.\.\."\);\s+// Wait up to 60 seconds for any username locator to appear\s+boolean usernameFound = false;\s+for \(int waitAttempt = 0; waitAttempt < 30; waitAttempt\+\+\) \{\s+if \(isAnyUsernameLocatorPresent\(2\)\) \{\s+usernameFound = true;\s+System\.out\.println\("[^"]*Username field found[^"]*"\);\s+break;\s+\}\s+Thread\.sleep\(2000\);\s+\}', `
        $newCode
    
    # Also update the retry section to use waitForCredentialsDialog
    $content = $content -replace `
        'if \(!isAnyUsernameLocatorPresent\(10\)\) \{', `
        'if (!waitForCredentialsDialog(30)) {'
    
    $content | Set-Content $filePath -Encoding UTF8 -NoNewline
    Write-Host "Successfully integrated waitForCredentialsDialog into perform_Forms_Login method."
} else {
    Write-Host "Could not find the exact pattern to replace. The file may have been modified."
    Write-Host "Looking for alternative patterns..."
    
    # Try alternative: look for the explicit wait comment
    if ($content -match "Waiting for username field with explicit wait") {
        Write-Host "Found alternative pattern. Attempting replacement..."
        
        # Replace using line-by-line approach
        $lines = $content -split "`r?`n"
        $newLines = @()
        $skipUntilClosingBrace = $false
        $braceCount = 0
        
        for ($i = 0; $i -lt $lines.Count; $i++) {
            $line = $lines[$i]
            
            if ($line -match "// Now wait for the username field to appear with a longer timeout") {
                # Add the new code instead
                $newLines += "                // Use the dedicated method to wait for credentials dialog to be fully interactive"
                $newLines += '                System.out.println("Waiting for credentials dialog with dedicated wait method (60 seconds timeout)...");'
                $newLines += "                boolean usernameFound = waitForCredentialsDialog(60);"
                $newLines += ""
                
                # Skip lines until we find the closing brace of the for loop
                $skipUntilClosingBrace = $true
                $braceCount = 0
                continue
            }
            
            if ($skipUntilClosingBrace) {
                if ($line -match '\{') { $braceCount++ }
                if ($line -match '\}') { $braceCount-- }
                
                # Check if this is the closing brace of the for loop (after seeing the for loop start)
                if ($line -match 'for \(int waitAttempt') {
                    $braceCount = 1  # Reset to track the for loop
                }
                
                # Skip until we've closed the for loop
                if ($braceCount -le 0 -and $line.Trim() -eq '}') {
                    $skipUntilClosingBrace = $false
                }
                continue
            }
            
            # Replace isAnyUsernameLocatorPresent(10) with waitForCredentialsDialog(30) in retry section
            if ($line -match 'if \(!isAnyUsernameLocatorPresent\(10\)\)') {
                $line = $line -replace 'isAnyUsernameLocatorPresent\(10\)', 'waitForCredentialsDialog(30)'
            }
            
            $newLines += $line
        }
        
        $newContent = $newLines -join "`r`n"
        $newContent | Set-Content $filePath -Encoding UTF8 -NoNewline
        Write-Host "Successfully integrated waitForCredentialsDialog using line-by-line approach."
    } else {
        Write-Host "ERROR: Could not find any recognizable pattern to replace."
        Write-Host "Manual integration may be required."
        exit 1
    }
}
