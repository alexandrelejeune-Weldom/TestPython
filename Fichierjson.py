from googleapiclient.discovery import build
from google.oauth2.credentials import Credentials
import json

creds = Credentials.from_authorized_user_file("token.json")
sheets = build("sheets", "v4", credentials=creds)

SPREADSHEET_ID = "1w9vhdELXlkfLhVLdigbP8DMrZ_1WuugTp5BHurIpqvU"
RANGE = "A:Z"  # plage à lire

result = sheets.spreadsheets().values().get(
    spreadsheetId=SPREADSHEET_ID,
    range=RANGE
).execute()

values = result.get("values", [])

with open("TestPython.json", "w", encoding="utf-8") as f:
    json.dump(values, f, indent=4, ensure_ascii=False)

print("Google Sheets exporté en JSON !")

