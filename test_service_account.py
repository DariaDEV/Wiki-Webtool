import os

import gspread
from google.oauth2.service_account import Credentials

SCOPES = [
    "https://www.googleapis.com/auth/spreadsheets.readonly",
    "https://www.googleapis.com/auth/drive.readonly",
]

credentials = Credentials.from_service_account_file(
    "service-account.json",
    scopes=SCOPES,
)

client = gspread.authorize(credentials)

for url in [
    os.environ["ACTIVITY_SHEET_URL"],
    os.environ["VOD_URL"]
]:
    spreadsheet = client.open_by_url(url)
    print("Success:", spreadsheet.title)