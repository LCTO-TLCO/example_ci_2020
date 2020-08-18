from __future__ import print_function
import pickle
import os.path
import gspread
from oauth2client.service_account import ServiceAccountCredentials

# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/spreadsheets.readonly']

# The ID and range of a sample spreadsheet.
SCOPES = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
sheet_id = "1eBYxrJvkxmnMtETaQgOAoLoDm-c-3FV6grj-9_T9qpU"
sheet_name = 'debug'
credentials_path = "./webbanditexamine2020-6d4983286987.json"


def main():
    sheet = api_service().worksheet("test")
    sheet.append_row(['やったか？' for _ in range(10)])
    # 変更の確認
    # print(sheet.acell('A1'))


def api_service():
    """Get instance to manipulate google spread sheet
    """
    credentials = ServiceAccountCredentials.from_json_keyfile_name(credentials_path, SCOPES)
    gc = gspread.authorize(credentials)
    return gc.open_by_key(sheet_id)


if __name__ == '__main__':
    main()
