from django.shortcuts import render

# Create your views here.
from django.views.decorators.csrf import csrf_exempt
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from django.http import HttpResponse
from django.http import HttpResponseServerError
import json
from . import credential

# Create your views here.

SCOPES = ['https://spreadsheets.google.com/feeds',
          'https://www.googleapis.com/auth/drive']
sheet_id = "1vaMUxom8pV_UfVf12ZQJdMwky9CYmRVnALSYJTJM7eU"
sheet_name = 'debug'


@csrf_exempt
def save_user_data(request):
    try:
        data = dict(request.POST)
        data = json.loads(data["data"][0])
        # 値をリストで保持している (MultiValueDict を継承している)
        # https://qiita.com/hfunai/items/68a81c60a7f5778b5ccd
        sheet = api_service().worksheet(sheet_name)
        sheet.append_row(list(data.values()))
    except Exception as e:
        import traceback
        traceback.print_exc()
        return HttpResponseServerError()
    return HttpResponse(status=200)


def api_service():
    """Get instance to manipulate google spread sheet
    """
    credentials = ServiceAccountCredentials.from_json_keyfile_name(credential.credential_path, SCOPES)
    gc = gspread.authorize(credentials)
    return gc.open_by_key(sheet_id)


# 実験参加者IDごとにシートを作って記録する関数
@csrf_exempt
def save_question_data(request):
    try:
        data = dict(request.POST)
        d = json.loads(data["data"][0])
        d = [list(d[i].values()) for i in range(len(d))]
        index = []
        sheet = api_service()
        ws = None
        if any([str(data["ID"][0]) == tmp.title for tmp in sheet.worksheets()]):
            ws = sheet.worksheet(str(data["ID"][0]))
        else:
            ws = sheet.add_worksheet(title=str(data["ID"][0]), rows="100", cols="20")
        # list
        for row in d:
            ws.append_row(row)
    except Exception as e:
        import traceback
        traceback.print_exc()
        return HttpResponseServerError()
    return HttpResponse(status=200)
