#!/bin/bash
# Quick setup script for Azure Blob Storage APK management

set -e

echo "=============================================="
echo "Azure Blob Storage Setup for APK Management"
echo "=============================================="
echo ""

# Function to check if command exists
command_exists() {
    command -v "$1" >/dev/null 2>&1
}

# Check prerequisites
echo "Checking prerequisites..."
if ! command_exists python3; then
    echo "❌ Python 3 is not installed. Please install Python 3.x"
    exit 1
fi
echo "✅ Python 3 found"

# Install required packages
echo ""
echo "Installing required Python packages..."
pip3 install -r scripts/requirements.txt

echo ""
echo "✅ Setup complete!"
echo ""
echo "=============================================="
echo "Next Steps:"
echo "=============================================="
echo ""
echo "1. Create Azure Storage Account:"
echo "   - Go to https://portal.azure.com"
echo "   - Create a Storage Account"
echo "   - Create a container (e.g., 'apk-files')"
echo ""
echo "2. Set environment variables:"
echo "   export AZURE_STORAGE_ACCOUNT=\"your-storage-account\""
echo "   export AZURE_STORAGE_KEY=\"your-storage-key\""
echo "   export AZURE_STORAGE_CONTAINER=\"apk-files\""
echo ""
echo "3. Upload your APK:"
echo "   python3 scripts/upload_apk_to_blob.py --apk-path /path/to/app.apk --blob-name EpturaEngage.apk"
echo ""
echo "4. Configure Azure DevOps Pipeline:"
echo "   - Add the azure-pipelines.yml to your repo"
echo "   - Set pipeline variables (see AZURE_BLOB_SETUP.md)"
echo ""
echo "For detailed instructions, see: AZURE_BLOB_SETUP.md"
echo "=============================================="
