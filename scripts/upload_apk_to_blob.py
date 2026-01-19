#!/usr/bin/env python3
"""
Script to upload APK to Azure Blob Storage
Use this script to upload your APK file to Azure Blob Storage for CI/CD pipeline access
"""

import os
import sys
import argparse
from azure.storage.blob import BlobServiceClient, ContentSettings
from datetime import datetime

def upload_apk_to_blob(apk_path, storage_account, storage_key, container_name, blob_name=None, overwrite=True):
    """Upload APK to Azure Blob Storage"""
    
    # Validate APK file exists
    if not os.path.exists(apk_path):
        print(f"❌ Error: APK file not found at: {apk_path}")
        sys.exit(1)
    
    # Use filename as blob name if not specified
    if blob_name is None:
        blob_name = os.path.basename(apk_path)
    
    try:
        print(f"📤 Uploading APK to Azure Blob Storage...")
        print(f"   APK File: {apk_path}")
        print(f"   Storage Account: {storage_account}")
        print(f"   Container: {container_name}")
        print(f"   Blob Name: {blob_name}")
        
        # Get file size
        file_size_mb = os.path.getsize(apk_path) / (1024 * 1024)
        print(f"   File Size: {file_size_mb:.2f} MB")
        
        # Create connection string
        connection_string = f"DefaultEndpointsProtocol=https;AccountName={storage_account};AccountKey={storage_key};EndpointSuffix=core.windows.net"
        
        # Create BlobServiceClient
        blob_service_client = BlobServiceClient.from_connection_string(connection_string)
        
        # Create container if it doesn't exist
        container_client = blob_service_client.get_container_client(container_name)
        try:
            container_client.create_container()
            print(f"✅ Container '{container_name}' created")
        except Exception as e:
            if "ContainerAlreadyExists" in str(e):
                print(f"ℹ️  Container '{container_name}' already exists")
            else:
                raise
        
        # Get blob client
        blob_client = blob_service_client.get_blob_client(container=container_name, blob=blob_name)
        
        # Check if blob exists
        if blob_client.exists() and not overwrite:
            print(f"⚠️  Warning: Blob '{blob_name}' already exists. Use --overwrite to replace it.")
            sys.exit(1)
        
        # Upload the file
        print(f"⬆️  Uploading... This may take a few minutes for large files.")
        
        # Set content type for APK
        content_settings = ContentSettings(content_type='application/vnd.android.package-archive')
        
        with open(apk_path, "rb") as data:
            blob_client.upload_blob(
                data,
                overwrite=overwrite,
                content_settings=content_settings,
                metadata={
                    'upload_date': datetime.now().isoformat(),
                    'file_name': os.path.basename(apk_path)
                }
            )
        
        # Get blob URL
        blob_url = blob_client.url
        
        print(f"✅ APK uploaded successfully!")
        print(f"   Blob URL: {blob_url}")
        print(f"   Blob Name: {blob_name}")
        print(f"\n📋 Use these values in your Azure Pipeline variables:")
        print(f"   AZURE_STORAGE_ACCOUNT: {storage_account}")
        print(f"   AZURE_STORAGE_CONTAINER: {container_name}")
        print(f"   APK_BLOB_NAME: {blob_name}")
        print(f"   (AZURE_STORAGE_KEY should be set as a secret variable)")
        
        return True
        
    except Exception as e:
        print(f"❌ Error uploading APK to Azure Blob Storage: {str(e)}")
        import traceback
        traceback.print_exc()
        sys.exit(1)

def main():
    parser = argparse.ArgumentParser(
        description='Upload APK to Azure Blob Storage',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Upload APK with environment variables
  python upload_apk_to_blob.py --apk-path /path/to/app.apk
  
  # Upload APK with explicit parameters
  python upload_apk_to_blob.py --apk-path /path/to/app.apk \\
    --storage-account mystorageaccount \\
    --storage-key "your-key-here" \\
    --container mycontainer \\
    --blob-name EpturaEngage.apk

Environment Variables:
  AZURE_STORAGE_ACCOUNT: Azure Storage account name
  AZURE_STORAGE_KEY: Azure Storage account key
  AZURE_STORAGE_CONTAINER: Container name (default: apk-files)
  APK_BLOB_NAME: Name for the blob (default: filename from apk-path)
        """
    )
    
    parser.add_argument('--apk-path', required=True, help='Path to the APK file')
    parser.add_argument('--storage-account', help='Azure Storage account name (or set AZURE_STORAGE_ACCOUNT env var)')
    parser.add_argument('--storage-key', help='Azure Storage account key (or set AZURE_STORAGE_KEY env var)')
    parser.add_argument('--container', help='Container name (or set AZURE_STORAGE_CONTAINER env var, default: apk-files)')
    parser.add_argument('--blob-name', help='Name for the blob in storage (or set APK_BLOB_NAME env var)')
    parser.add_argument('--overwrite', action='store_true', default=True, help='Overwrite existing blob (default: True)')
    parser.add_argument('--no-overwrite', action='store_false', dest='overwrite', help='Do not overwrite existing blob')
    
    args = parser.parse_args()
    
    # Get values from args or environment variables
    storage_account = args.storage_account or os.environ.get('AZURE_STORAGE_ACCOUNT')
    storage_key = args.storage_key or os.environ.get('AZURE_STORAGE_KEY')
    container_name = args.container or os.environ.get('AZURE_STORAGE_CONTAINER', 'apk-files')
    blob_name = args.blob_name or os.environ.get('APK_BLOB_NAME')
    
    # Validate required parameters
    if not storage_account:
        print("❌ Error: Azure Storage account name not provided")
        print("   Use --storage-account or set AZURE_STORAGE_ACCOUNT environment variable")
        sys.exit(1)
    
    if not storage_key:
        print("❌ Error: Azure Storage key not provided")
        print("   Use --storage-key or set AZURE_STORAGE_KEY environment variable")
        sys.exit(1)
    
    print("=" * 70)
    print("Azure Blob Storage - APK Upload Script")
    print("=" * 70)
    
    upload_apk_to_blob(
        apk_path=args.apk_path,
        storage_account=storage_account,
        storage_key=storage_key,
        container_name=container_name,
        blob_name=blob_name,
        overwrite=args.overwrite
    )
    
    print("=" * 70)

if __name__ == "__main__":
    main()
