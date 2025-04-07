import os
import pickle
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient.discovery import build

SCOPES = [
    'https://www.googleapis.com/auth/drive',
    'https://www.googleapis.com/auth/spreadsheets'
]

TOKEN_FILE = 'token.json'
CREDENTIALS_FILE = 'credentials.json'

def get_credentials(verbose: bool = True):
    """
    Authenticates the user via OAuth2 and returns valid credentials.
    If verbose is True, prints status messages.
    """
    creds = None

    try:
        if os.path.exists(TOKEN_FILE):
            with open(TOKEN_FILE, 'rb') as token:
                creds = pickle.load(token)
            if verbose:
                print("Loaded credentials from token file.")

        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
                if verbose:
                    print("Refreshed expired credentials.")
            else:
                if not os.path.exists(CREDENTIALS_FILE):
                    raise FileNotFoundError("Missing credentials.json")
                flow = InstalledAppFlow.from_client_secrets_file(CREDENTIALS_FILE, SCOPES)
                creds = flow.run_local_server(port=8080)
                if verbose:
                    print("Logged in via browser and obtained new credentials.")

            with open(TOKEN_FILE, 'wb') as token:
                pickle.dump(creds, token)
                if verbose:
                    print("Saved new credentials to token file.")
        
        return creds

    except Exception as e:
        if verbose:
            print(f"Authentication failed: {e}")
        raise

def get_drive_client(verbose: bool = True):
    try:
        creds = get_credentials(verbose)
        drive_service = build('drive', 'v3', credentials=creds)
        if verbose:
            print("Google Drive client initialized.")
        return drive_service
    except Exception as e:
        if verbose:
            print(f"Failed to create Google Drive client: {e}")
        raise

def get_sheets_client(verbose: bool = True):
    try:
        creds = get_credentials(verbose)
        sheets_service = build('sheets', 'v4', credentials=creds)
        if verbose:
            print("Google Sheets client initialized.")
        return sheets_service
    except Exception as e:
        if verbose:
            print(f"Failed to create Google Sheets client: {e}")
        raise
