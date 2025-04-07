# app/main.py
from fastapi import FastAPI, Request
from fastapi.responses import RedirectResponse, HTMLResponse
from app.google_auth import get_auth_url, exchange_code
from app.google_drive import get_drive_client
from app.google_sheets import get_sheets_client


app = FastAPI()

@app.get("/")
def home():
    auth_url = get_auth_url()

    # Add links to Drive and Sheets test routes
    html_content = f'''
    <h1>Google OAuth2 Demo</h1>
    <p><a href="{auth_url}">Authenticate with Google</a></p>
    <p><a href="/drive/files">Test Google Drive API</a></p>
    <p><a href="/sheets/title?sheet_id=1nT04FDDO2BbmmsZNixGolJvMyrx2tPYXZVWLPOf1FAQ">Test Google Sheets API</a></p>
    '''

    return HTMLResponse(content=html_content)

@app.get("/auth/callback")
def auth_callback(request: Request):
    code = request.query_params.get("code")
    if not code:
        return HTMLResponse("Missing code", status_code=400)
    creds = exchange_code(code)
    return HTMLResponse(f"<h2>Login successful</h2><p>Token saved.</p><p>Scopes: {creds.scopes}</p>")

@app.get("/list-drive-files")
def list_drive_files():
    drive = get_drive_client()
    results = drive.files().list(pageSize=10).execute()
    return results.get("files", [])

@app.get("/get-sheet-title")
def get_sheet_title(spreadsheet_id: str):
    sheets = get_sheets_client()
    response = sheets.spreadsheets().get(spreadsheetId=spreadsheet_id).execute()
    return {"title": response['properties']['title']}
