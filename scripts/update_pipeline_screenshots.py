#!/usr/bin/env python3
"""
Script to update azure-pipelines.yml to ensure screenshots are captured 
for both passed and failed test cases and published as artifacts.
"""

import os

def update_pipeline():
    pipeline_file = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'azure-pipelines.yml')
    
    with open(pipeline_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 1. Update the Collect Test Reports script to include screenshot handling
    old_collect_reports = """          - script: |
              echo "📊 Collecting test execution reports..."
              
              # Create reports directory
              REPORTS_DIR="$(Build.SourcesDirectory)/test-reports"
              mkdir -p $REPORTS_DIR
              
              # Copy surefire reports"""
    
    new_collect_reports = """          - script: |
              echo "📊 Collecting test execution reports and screenshots..."
              
              # Create reports directory
              REPORTS_DIR="$(Build.SourcesDirectory)/test-reports"
              mkdir -p $REPORTS_DIR
              
              # Ensure screenshots directory exists for artifact publishing
              SCREENSHOTS_DIR="$(Build.SourcesDirectory)/target/screenshots"
              mkdir -p $SCREENSHOTS_DIR
              
              # If no screenshots exist, create a placeholder file to ensure artifact publishing doesn't fail
              if [ -z "$(ls -A $SCREENSHOTS_DIR 2>/dev/null)" ]; then
                echo "No test screenshots were captured during this run." > "$SCREENSHOTS_DIR/README.txt"
                echo "Screenshots are captured after each test case (passed or failed)." >> "$SCREENSHOTS_DIR/README.txt"
                echo "Timestamp: $(date)" >> "$SCREENSHOTS_DIR/README.txt"
              fi
              
              # Count and list screenshots
              SCREENSHOT_COUNT=$(find $SCREENSHOTS_DIR -name "*.png" 2>/dev/null | wc -l)
              echo "📸 Found $SCREENSHOT_COUNT test screenshots"
              
              if [ "$SCREENSHOT_COUNT" -gt 0 ]; then
                echo ""
                echo "📸 Test Screenshots Summary:"
                echo "================================"
                PASSED_COUNT=$(find $SCREENSHOTS_DIR -name "Passed_*.png" 2>/dev/null | wc -l)
                FAILED_COUNT=$(find $SCREENSHOTS_DIR -name "Failed_*.png" 2>/dev/null | wc -l)
                echo "✅ PASSED Test Screenshots: $PASSED_COUNT"
                ls -la $SCREENSHOTS_DIR/Passed_*.png 2>/dev/null | head -20 || true
                echo ""
                echo "❌ FAILED Test Screenshots: $FAILED_COUNT"
                ls -la $SCREENSHOTS_DIR/Failed_*.png 2>/dev/null | head -20 || true
                echo "================================"
              fi
              
              # Copy surefire reports"""
    
    content = content.replace(old_collect_reports, new_collect_reports)
    
    # 2. Update the Publish Test Screenshots task
    old_publish_screenshots = """          - task: PublishPipelineArtifact@1
            displayName: 'Publish Test Screenshots'
            inputs:
              targetPath: '$(Build.SourcesDirectory)/target/screenshots'
              artifact: 'TestScreenshots'
              publishLocation: 'pipeline'
            condition: succeededOrFailed()
            continueOnError: true"""
    
    new_publish_screenshots = """          - task: PublishPipelineArtifact@1
            displayName: 'Publish Test Screenshots (Passed and Failed)'
            inputs:
              targetPath: '$(Build.SourcesDirectory)/target/screenshots'
              artifact: 'TestScreenshots'
              publishLocation: 'pipeline'
            condition: always()"""
    
    content = content.replace(old_publish_screenshots, new_publish_screenshots)
    
    # 3. Update the Collect Test Reports displayName
    content = content.replace(
        "displayName: 'Collect Test Reports'",
        "displayName: 'Collect Test Reports and Screenshots'"
    )
    
    with open(pipeline_file, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print("✅ Pipeline updated successfully!")
    print("   - Added screenshot directory creation and validation")
    print("   - Added screenshot summary in pipeline logs")
    print("   - Updated Publish Test Screenshots to always run")
    print("   - Screenshots for both PASSED and FAILED tests will be published as artifacts")

if __name__ == '__main__':
    update_pipeline()
