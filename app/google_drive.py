from googleapiclient.discovery import build
from app.google_auth import get_credentials

def get_drive_client():
    creds = get_credentials()
    return build('drive', 'v3', credentials=creds)
