import pytest
from app.google_auth import get_drive_client, get_sheets_client

def test_google_drive_client():
    drive = get_drive_client()
    response = drive.files().list(pageSize=1).execute()
    assert 'files' in response
    print(f"Drive client working. Found {len(response['files'])} files.")

def test_google_sheets_client():
    sheets = get_sheets_client()

    # Replace with a valid test spreadsheet ID
    TEST_SPREADSHEET_ID = '1nT04FDDO2BbmmsZNixGolJvMyrx2tPYXZVWLPOf1FAQ'
    response = sheets.spreadsheets().get(spreadsheetId=TEST_SPREADSHEET_ID).execute()
    assert 'properties' in response
    print(f"Sheets client working. Spreadsheet title: {response['properties']['title']}")

if __name__ == "__main__":
    pytest.main()
