import gspread
from oauth2client.service_account import ServiceAccountCredentials
import os

# Use python-dotenv to load creds path
CREDS_PATH = os.getenv("GOOGLE_CREDS_PATH", "creds.json")
SHEET_NAME = os.getenv("SHEET_NAME", "Expenses")  # Default sheet name

def get_sheet():
    """
    Authenticates with Google Sheets using a service account.
    Returns the first worksheet.
    """
    scope = [
        "https://spreadsheets.google.com/feeds",
        "https://www.googleapis.com/auth/drive"
    ]

    creds = ServiceAccountCredentials.from_json_keyfile_name(CREDS_PATH, scope)
    client = gspread.authorize(creds)
    sheet = client.open(SHEET_NAME).sheet1
    return sheet

def append_expense(expense: dict):
    """
    Appends a single expense to the Google Sheet.
    Expects a dict with keys: amount, merchant, raw.
    """
    sheet = get_sheet()
    sheet.append_row([
        expense["merchant"],
        expense["amount"],
        expense["raw"]
    ])