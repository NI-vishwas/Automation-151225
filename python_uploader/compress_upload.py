import os
import shutil
import google.auth
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from googleapiclient.http import MediaFileUpload
from pathlib import Path
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow

# Compression
def compress_to_zip(filepath):
    base_file = Path(filepath)
    new_file = base_file.with_suffix('.zip')
    if base_file.exists():
        shutil.make_archive(new_file.stem, 'zip', './')
        print(f"Compressed Folder {filepath} successfully to {new_file}")
    
    return base_file.with_suffix('.zip')

# Uploading
def upload_zip(filepath, folderID):
    # Reading Credentials
    creds = None
    SCOPES = ["https://www.googleapis.com/auth/drive.metadata.readonly", "https://www.googleapis.com/auth/drive.file"]
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists("token.json"):
        creds = Credentials.from_authorized_user_file("token.json", SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                "credentials.json", SCOPES
            )
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open("token.json", "w") as token:
            token.write(creds.to_json())

    # create drive api client
    service = build("drive", "v3", credentials=creds)

    file_metadata = {
        'name': os.path.basename(filepath),
        'parents': [folderID] # folderID
    }

    media = MediaFileUpload(filepath, mimetype="application/zip", resumable=True)

    file = (
        service.files()
        .create(body=file_metadata, media_body=media, fields="id")
        .execute()
    )

    print(f"Uploaded to folder! file ID:{file.get('id')}")


# Main
def main():
    # Calling compress method
    object_to_compress = input("Enter the folder name to compress: ")
    # object_to_compress = '/home/vishwas/Workspace/temp/python_uploader/summary.log'
    zipfile = compress_to_zip(object_to_compress)
    print(f'Zipfilepath is: {zipfile}')
    # Calling upload method
    folderID = input('Enter the folder ID to upload: ')
    # change the folderID here
    # folderID = '1vwtYSiodTNP4P0TXg_XzzsCyaQ32RpWO' 

    upload_zip(zipfile, folderID)


if __name__ == '__main__':
    main()
