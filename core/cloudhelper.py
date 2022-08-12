from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from googleapiclient.http import MediaFileUpload
from pathlib import Path


class GoogleDrive:

    def __init__(self, secrects_file='token.json'):
        self.SCOPES = ['https://www.googleapis.com/auth/drive']
        self.creds = None
        self.secrects_file = secrects_file
    
    def authHandler(self):
        creds_file = Path('token.json')
        if creds_file.exists():
            self.creds = Credentials.from_authorized_user_file(self.secrects_file, self.SCOPES)
        if not self.creds or not self.creds.valid:
            if self.creds and self.creds.expired and self.creds.refresh_token:
                self.creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(
                    'Credentials.json',
                    self.SCOPES)
                self.creds = flow.run_local_server(port=0)
        with open('token.json', 'w') as token:
            token.write(self.creds.to_json())
    
    def uploadFile(self,file):
        filetbu = Path(file)
        try:
            service = build('drive', 'v3', credentials=self.creds)
            response = service.files().list(
                q="name='B1k1' and mimeType='application/vnd.google-apps.folder'",
                spaces='drive'
                ).execute()
            
            if not response.get('files'):
                file_metadata = {
                    "name":"B1k1",
                    "mimeType":"application/vnd.google-apps.folder"
                }

                file = service.files().create(body=file_metadata, fields="id").execute()

                dir_id = file.get('id')	
            else:
                dir_id = response['files'][0]['id']

            file_metadata = {
                "name": filetbu.name,
                "parents": [dir_id]
            }
            media = MediaFileUpload(file)
            upload_file = service.files().create(body=file_metadata,media_body=media,fields="id").execute()
        except HttpError as err:
            print(f'Error: {str(err)}')