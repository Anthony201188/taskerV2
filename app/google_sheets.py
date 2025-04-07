from googleapiclient.discovery import build
from app.google_auth import get_credentials

def get_sheets_client():
    creds = get_credentials()
    return build('sheets', 'v4', credentials=creds)
