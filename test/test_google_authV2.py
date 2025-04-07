import pytest
from app.google_auth import get_drive_client, get_sheets_client
from googleapiclient.errors import HttpError

def test_google_drive_client():
    """
    Test the Google Drive client authentication.
    Verifies that the client is authenticated successfully and files can be listed.
    """
    try:
        print("Starting Google Drive client authentication...")
        drive = get_drive_client(verbose=True)
        print("Drive client authenticated successfully.")

        # Try to list files in the Drive
        response = drive.files().list(pageSize=1).execute()
        
        # Assert that the response contains files
        assert 'files' in response
        print(f"Drive client working. Found {len(response['files'])} files.")
        
    except HttpError as e:
        pytest.fail(f"Google Drive authentication failed with error: {e}")
    except Exception as e:
        pytest.fail(f"Test failed: {e}")

def test_google_sheets_client():
    """
    Test the Google Sheets client authentication.
    Verifies that the client is authenticated successfully and can access a spreadsheet.
    """
    try:
        print("Starting Google Sheets client authentication...")
        sheets = get_sheets_client(verbose=True)
        print("Sheets client authenticated successfully.")
        
        # Replace with a valid test spreadsheet ID
        TEST_SPREADSHEET_ID = '1nT04FDDO2BbmmsZNixGolJvMyrx2tPYXZVWLPOf1FAQ'
        
        # Try to get the spreadsheet information
        response = sheets.spreadsheets().get(spreadsheetId=TEST_SPREADSHEET_ID).execute()

        # Assert that the response contains properties
        assert 'properties' in response
        print(f"Sheets client working. Spreadsheet title: {response['properties']['title']}")

    except HttpError as e:
        pytest.fail(f"Google Sheets authentication failed with error: {e}")
    except Exception as e:
        pytest.fail(f"Test failed: {e}")

if __name__ == "__main__":
    pytest.main()
