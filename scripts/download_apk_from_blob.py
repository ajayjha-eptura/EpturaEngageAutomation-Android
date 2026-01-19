#!/usr/bin/env python3
"""
Script to download APK from Azure Blob Storage
This script is used in the CI/CD pipeline to fetch the latest APK for testing
Supports both SAS Token and Storage Key authentication
"""

import os
import sys
import urllib.request
import urllib.parse
from datetime import datetime

def download_apk_from_blob():
    """Download APK from Azure Blob Storage using SAS Token or Storage Key"""
    
    # Get environment variables
    storage_account = os.environ.get('AZURE_STORAGE_ACCOUNT')
    container_name = os.environ.get('AZURE_STORAGE_CONTAINER')
    blob_name = os.environ.get('APK_BLOB_NAME')
    local_path = os.environ.get('APK_LOCAL_PATH')
    
    # SAS Token authentication (preferred)
    sas_token = os.environ.get('AZURE_SAS_TOKEN')
    
    # Storage Key authentication (fallback)
    storage_key = os.environ.get('AZURE_STORAGE_KEY')
    
    # Validate required environment variables
    if not all([storage_account, container_name, blob_name, local_path]):
        print("❌ Error: Missing required environment variables")
        print("Required variables: AZURE_STORAGE_ACCOUNT, AZURE_STORAGE_CONTAINER, APK_BLOB_NAME, APK_LOCAL_PATH")
        print("Authentication: AZURE_SAS_TOKEN (preferred) or AZURE_STORAGE_KEY")
        sys.exit(1)
    
    if not sas_token and not storage_key:
        print("❌ Error: Missing authentication. Provide either AZURE_SAS_TOKEN or AZURE_STORAGE_KEY")
        sys.exit(1)
    
    try:
        print(f"📥 Connecting to Azure Blob Storage...")
        print(f"   Storage Account: {storage_account}")
        print(f"   Container: {container_name}")
        print(f"   Blob Name: {blob_name}")
        
        if sas_token:
            # Use SAS Token authentication (simpler, no SDK needed)
            print(f"   Authentication: SAS Token")
            download_with_sas_token(storage_account, container_name, blob_name, sas_token, local_path)
        else:
            # Use Storage Key authentication (requires Azure SDK)
            print(f"   Authentication: Storage Key")
            download_with_storage_key(storage_account, container_name, blob_name, storage_key, local_path)
        
        # Verify download
        if os.path.exists(local_path):
            file_size_mb = os.path.getsize(local_path) / (1024 * 1024)
            print(f"✅ APK downloaded successfully!")
            print(f"   Local Path: {local_path}")
            print(f"   Size: {file_size_mb:.2f} MB")
            return True
        else:
            print(f"❌ Error: Failed to download APK")
            sys.exit(1)
            
    except Exception as e:
        print(f"❌ Error downloading APK from Azure Blob Storage: {str(e)}")
        import traceback
        traceback.print_exc()
        sys.exit(1)


def download_with_sas_token(storage_account, container_name, blob_name, sas_token, local_path):
    """Download APK using SAS Token (no Azure SDK required)"""
    
    # Clean up SAS token (remove leading ? if present)
    sas_token = sas_token.lstrip('?')
    
    # Construct the blob URL with SAS token
    blob_url = f"https://{storage_account}.blob.core.windows.net/{container_name}/{blob_name}?{sas_token}"
    
    print(f"⬇️  Downloading APK from Azure Blob Storage...")
    
    # Create directory if it doesn't exist
    local_dir = os.path.dirname(local_path)
    if local_dir:
        os.makedirs(local_dir, exist_ok=True)
    
    # Download the file
    urllib.request.urlretrieve(blob_url, local_path)
    print(f"   Download complete!")


def download_with_storage_key(storage_account, container_name, blob_name, storage_key, local_path):
    """Download APK using Storage Key (requires Azure SDK)"""
    
    try:
        from azure.storage.blob import BlobServiceClient
    except ImportError:
        print("❌ Error: azure-storage-blob package not installed.")
        print("   Install with: pip install azure-storage-blob")
        print("   Or use SAS Token authentication instead (AZURE_SAS_TOKEN)")
        sys.exit(1)
    
    # Create connection string
    connection_string = f"DefaultEndpointsProtocol=https;AccountName={storage_account};AccountKey={storage_key};EndpointSuffix=core.windows.net"
    
    # Create BlobServiceClient
    blob_service_client = BlobServiceClient.from_connection_string(connection_string)
    
    # Get blob client
    blob_client = blob_service_client.get_blob_client(container=container_name, blob=blob_name)
    
    # Check if blob exists
    if not blob_client.exists():
        print(f"❌ Error: Blob '{blob_name}' not found in container '{container_name}'")
        sys.exit(1)
    
    # Get blob properties
    properties = blob_client.get_blob_properties()
    blob_size_mb = properties.size / (1024 * 1024)
    last_modified = properties.last_modified
    
    print(f"📦 APK Details:")
    print(f"   Size: {blob_size_mb:.2f} MB")
    print(f"   Last Modified: {last_modified}")
    
    # Download the blob
    print(f"⬇️  Downloading APK to: {local_path}")
    
    # Create directory if it doesn't exist
    local_dir = os.path.dirname(local_path)
    if local_dir:
        os.makedirs(local_dir, exist_ok=True)
    
    with open(local_path, "wb") as download_file:
        download_stream = blob_client.download_blob()
        download_file.write(download_stream.readall())


if __name__ == "__main__":
    print("=" * 60)
    print("Azure Blob Storage - APK Download Script")
    print("=" * 60)
    download_apk_from_blob()
    print("=" * 60)