from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    try:
        return render(request, 'index.html')
    except Exception as e:
        print(e)


def trans_test(request):
    try:
        return render(request, 'senni_test.html')
    except Exception as e:
        print(e)


def send(request):
    try:
        return render(request, 'datasend_test.html')
    except Exception as e:
        print(e)
