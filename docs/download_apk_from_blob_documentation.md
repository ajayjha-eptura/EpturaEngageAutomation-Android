# Download APK from Azure Blob Storage - Documentation

## Overview

The `download_apk_from_blob.py` script is designed to download APK files from Azure Blob Storage for use in the CI/CD pipeline. It supports two authentication methods and includes robust error handling with helpful diagnostics.

---

## Table of Contents

1. [Purpose](#purpose)
2. [Prerequisites](#prerequisites)
3. [Environment Variables](#environment-variables)
4. [Authentication Methods](#authentication-methods)
5. [Script Workflow](#script-workflow)
6. [Functions Reference](#functions-reference)
7. [Error Handling](#error-handling)
8. [Usage Examples](#usage-examples)

---

## Purpose

This script is used in the Azure DevOps CI/CD pipeline to:
- Fetch the latest APK from Azure Blob Storage
- Support automated testing without manual APK uploads
- Provide flexibility with two authentication options

---

## Prerequisites

| Requirement | Details |
|-------------|---------|
| Python | Version 3.x |
| Network Access | Access to Azure Blob Storage endpoints |
| Azure SDK (optional) | Only required if using Storage Key authentication |

**Install Azure SDK (if needed):**
```bash
pip install azure-storage-blob
```

---

## Environment Variables

The script requires the following environment variables to be set:

### Required Variables

| Variable | Description | Example |
|----------|-------------|---------|
| `AZURE_STORAGE_ACCOUNT` | Name of the Azure Storage Account | `entstorage` |
| `AZURE_STORAGE_CONTAINER` | Name of the blob container | `mobilebuilds` |
| `APK_BLOB_NAME` | Path/name of the APK blob | `Engage/Android/EpturaEngage.apk` |
| `APK_LOCAL_PATH` | Local path to save the downloaded APK | `./app.apk` |

### Authentication Variables (One Required)

| Variable | Description | Priority |
|----------|-------------|----------|
| `AZURE_SAS_TOKEN` | Shared Access Signature token | **Preferred** |
| `AZURE_STORAGE_KEY` | Storage account access key | Fallback |

---

## Authentication Methods

### 1. SAS Token Authentication (Recommended)

**Advantages:**
- No Azure SDK required (uses built-in `urllib`)
- More secure (limited permissions and expiration)
- Simpler setup

**How it works:**
1. Constructs a direct URL to the blob with the SAS token appended
2. Uses `urllib.request` to download the file
3. URL format: `https://{account}.blob.core.windows.net/{container}/{blob}?{sas_token}`

### 2. Storage Key Authentication

**Advantages:**
- Full access to storage account
- No token expiration concerns

**Requirements:**
- Requires `azure-storage-blob` Python package
- Uses the Azure SDK's `BlobServiceClient`

---

## Script Workflow

```
┌─────────────────────────────────────────────────────────────┐
│                        START                                │
└─────────────────────────────────────────────────────────────┘
                            │
                            ▼
┌─────────────────────────────────────────────────────────────┐
│  Step 1: Load Environment Variables                         │
│  - AZURE_STORAGE_ACCOUNT                                    │
│  - AZURE_STORAGE_CONTAINER                                  │
│  - APK_BLOB_NAME                                            │
│  - APK_LOCAL_PATH                                           │
│  - AZURE_SAS_TOKEN or AZURE_STORAGE_KEY                     │
└─────────────────────────────────────────────────────────────┘
                            │
                            ▼
┌─────────────────────────────────────────────────────────────┐
│  Step 2: Validate Required Variables                        │
│  - Check all required variables are present                 │
│  - Check at least one authentication method is available    │
│  - Exit with error if validation fails                      │
└─────────────────────────────────────────────────────────────┘
                            │
                            ▼
┌─────────────────────────────────────────────────────────────┐
│  Step 3: Select Authentication Method                       │
│  - If AZURE_SAS_TOKEN exists → Use SAS Token method         │
│  - Else → Use Storage Key method                            │
└─────────────────────────────────────────────────────────────┘
                            │
              ┌─────────────┴─────────────┐
              ▼                           ▼
┌──────────────────────────┐  ┌──────────────────────────┐
│  SAS Token Path          │  │  Storage Key Path        │
│                          │  │                          │
│  1. Check blob exists    │  │  1. Create connection    │
│     (HEAD request)       │  │     string               │
│  2. If not found:        │  │  2. Create BlobClient    │
│     - List available     │  │  3. Check blob exists    │
│       blobs              │  │  4. If not found:        │
│     - Show suggestions   │  │     - List available     │
│  3. Download via URL     │  │       blobs              │
│                          │  │  5. Download blob        │
└──────────────────────────┘  └──────────────────────────┘
              │                           │
              └─────────────┬─────────────┘
                            ▼
┌─────────────────────────────────────────────────────────────┐
│  Step 4: Create Local Directory (if needed)                 │
│  - Extract directory path from APK_LOCAL_PATH               │
│  - Create directory with os.makedirs()                      │
└─────────────────────────────────────────────────────────────┘
                            │
                            ▼
┌─────────────────────────────────────────────────────────────┐
│  Step 5: Verify Download                                    │
│  - Check file exists at local path                          │
│  - Calculate and display file size                          │
│  - Exit with success or failure                             │
└─────────────────────────────────────────────────────────────┘
                            │
                            ▼
┌─────────────────────────────────────────────────────────────┐
│                         END                                 │
└─────────────────────────────────────────────────────────────┘
```

---

## Functions Reference

### `download_apk_from_blob()`
**Main entry point function**

| Aspect | Description |
|--------|-------------|
| Purpose | Orchestrates the entire download process |
| Returns | `True` on success, exits with code 1 on failure |
| Actions | Loads env vars, validates, selects auth method, verifies download |

---

### `check_blob_exists(storage_account, container_name, blob_name, sas_token)`
**Checks if a blob exists using HTTP HEAD request**

| Parameter | Type | Description |
|-----------|------|-------------|
| `storage_account` | str | Azure storage account name |
| `container_name` | str | Blob container name |
| `blob_name` | str | Name/path of the blob |
| `sas_token` | str | SAS token for authentication |

| Returns | Description |
|---------|-------------|
| `True` | Blob exists |
| `False` | Blob not found (404) |
| Raises | Other HTTP errors |

---

### `list_available_blobs(storage_account, container_name, sas_token)`
**Lists blobs in a container for diagnostic purposes**

| Parameter | Type | Description |
|-----------|------|-------------|
| `storage_account` | str | Azure storage account name |
| `container_name` | str | Blob container name |
| `sas_token` | str | SAS token for authentication |

| Returns | Description |
|---------|-------------|
| `list` | List of blob names (up to first 10 displayed) |
| `[]` | Empty list if unable to list or no blobs found |

> **Note:** Requires "list" permission in SAS token to work properly.

---

### `download_with_sas_token(storage_account, container_name, blob_name, sas_token, local_path)`
**Downloads APK using SAS Token authentication**

| Step | Action |
|------|--------|
| 1 | Clean SAS token (remove leading `?` if present) |
| 2 | Check if blob exists |
| 3 | If not found, list available blobs and exit |
| 4 | Construct blob URL with SAS token |
| 5 | Create local directory if needed |
| 6 | Download file using `urllib.request.urlretrieve()` |

---

### `download_with_storage_key(storage_account, container_name, blob_name, storage_key, local_path)`
**Downloads APK using Storage Key authentication**

| Step | Action |
|------|--------|
| 1 | Import Azure SDK (exit if not installed) |
| 2 | Create connection string |
| 3 | Create `BlobServiceClient` |
| 4 | Get `BlobClient` for the specific blob |
| 5 | Check if blob exists |
| 6 | Display blob properties (size, last modified) |
| 7 | Create local directory if needed |
| 8 | Download blob content to local file |

---

## Error Handling

The script provides comprehensive error handling with helpful messages:

### Missing Environment Variables
```
❌ Error: Missing required environment variables
Required variables: AZURE_STORAGE_ACCOUNT, AZURE_STORAGE_CONTAINER, APK_BLOB_NAME, APK_LOCAL_PATH
```

### Missing Authentication
```
❌ Error: Missing authentication. Provide either AZURE_SAS_TOKEN or AZURE_STORAGE_KEY
```

### Blob Not Found
```
❌ Error: Blob 'path/to/file.apk' not found in container 'container-name'

💡 Possible causes:
   1. The APK file hasn't been uploaded to blob storage yet
   2. The blob name is incorrect (check for typos or path)
   3. The container name is incorrect
   4. The SAS token doesn't have permission to access this blob

📋 Listing available blobs in container...
💡 Found APK files in container:
   - Engage/Android/OtherApp.apk
```

### Missing Azure SDK
```
❌ Error: azure-storage-blob package not installed.
   Install with: pip install azure-storage-blob
   Or use SAS Token authentication instead (AZURE_SAS_TOKEN)
```

---

## Usage Examples

### Running Locally

**Set environment variables (Windows CMD):**
```cmd
set AZURE_STORAGE_ACCOUNT=entstorage
set AZURE_STORAGE_CONTAINER=mobilebuilds
set APK_BLOB_NAME=Engage/Android/EpturaEngage.apk
set APK_LOCAL_PATH=./app.apk
set AZURE_SAS_TOKEN=sv=2022-11-02&ss=b&srt=o&sp=r...
python scripts/download_apk_from_blob.py
```

**Set environment variables (PowerShell):**
```powershell
$env:AZURE_STORAGE_ACCOUNT = "entstorage"
$env:AZURE_STORAGE_CONTAINER = "mobilebuilds"
$env:APK_BLOB_NAME = "Engage/Android/EpturaEngage.apk"
$env:APK_LOCAL_PATH = "./app.apk"
$env:AZURE_SAS_TOKEN = "sv=2022-11-02&ss=b&srt=o&sp=r..."
python scripts/download_apk_from_blob.py
```

**Set environment variables (Linux/Mac):**
```bash
export AZURE_STORAGE_ACCOUNT=entstorage
export AZURE_STORAGE_CONTAINER=mobilebuilds
export APK_BLOB_NAME=Engage/Android/EpturaEngage.apk
export APK_LOCAL_PATH=./app.apk
export AZURE_SAS_TOKEN="sv=2022-11-02&ss=b&srt=o&sp=r..."
python scripts/download_apk_from_blob.py
```

### In Azure DevOps Pipeline

The script is called in the pipeline using the `PythonScript@0` task:

```yaml
- task: PythonScript@0
  displayName: 'Download APK from Blob Storage'
  inputs:
    scriptSource: 'filePath'
    scriptPath: '$(Build.SourcesDirectory)/scripts/download_apk_from_blob.py'
  env:
    AZURE_STORAGE_ACCOUNT: $(AZURE_STORAGE_ACCOUNT)
    AZURE_STORAGE_CONTAINER: $(AZURE_STORAGE_CONTAINER)
    AZURE_SAS_TOKEN: $(AZURE_SAS_TOKEN)  # Set as SECRET variable
    APK_BLOB_NAME: $(APK_BLOB_NAME)
    APK_LOCAL_PATH: $(APK_LOCAL_PATH)
```

---

## Expected Output

### Successful Download
```
============================================================
Azure Blob Storage - APK Download Script
============================================================
📥 Connecting to Azure Blob Storage...
   Storage Account: entstorage
   Container: mobilebuilds
   Blob Name: Engage/Android/EpturaEngage.apk
   Authentication: SAS Token
🔍 Checking if blob exists...
   ✅ Blob exists!
⬇️  Downloading APK from Azure Blob Storage...
   Download complete!
✅ APK downloaded successfully!
   Local Path: ./app.apk
   Size: 45.32 MB
============================================================
```

---

## Security Considerations

| Consideration | Recommendation |
|---------------|----------------|
| SAS Token Storage | Store as a **secret variable** in Azure DevOps |
| Token Permissions | Grant minimum required permissions (read only) |
| Token Expiration | Set appropriate expiration dates |
| Storage Key | Avoid using in pipelines; prefer SAS tokens |

---

## Troubleshooting

| Issue | Solution |
|-------|----------|
| "Blob not found" | Verify `APK_BLOB_NAME` path is correct; check if file was uploaded |
| "Missing authentication" | Ensure `AZURE_SAS_TOKEN` is set as a pipeline variable |
| "Unable to list blobs" | SAS token may not have "list" permission (not critical for download) |
| Download timeout | Check network connectivity; verify storage account endpoint |
| Azure SDK import error | Install with `pip install azure-storage-blob` or switch to SAS token |

---

## Related Files

| File | Purpose |
|------|---------|
| `azure-pipelines.yml` | CI/CD pipeline that calls this script |
| `upload_apk_to_blob.py` | Companion script for uploading APKs |
| `setup_azure_blob.sh` | Shell script for Azure Blob setup |
| `setup_azure_blob.bat` | Windows batch script for Azure Blob setup |

---

*Last Updated: January 19, 2026*
