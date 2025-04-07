# app/google_auth.py
import os
import pickle
from google_auth_oauthlib.flow import Flow
from google.oauth2.credentials import Credentials

SCOPES = [
    'https://www.googleapis.com/auth/drive',
    'https://www.googleapis.com/auth/spreadsheets'
]

CREDENTIALS_FILE = 'credentials.json'
TOKEN_FILE = 'token.pickle'

# Global state — ideally store in DB/session
flow = Flow.from_client_secrets_file(
    CREDENTIALS_FILE,
    scopes=SCOPES,
    redirect_uri='https://localhost:8000/auth/callback'
)

def get_auth_url():
    return flow.authorization_url(prompt='consent')[0]

def exchange_code(code):
    flow.fetch_token(code=code)
    creds = flow.credentials
    with open(TOKEN_FILE, 'wb') as token:
        pickle.dump(creds, token)
    return creds
