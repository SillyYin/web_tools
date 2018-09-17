from django.shortcuts import render
import re
import json
from django.http import HttpResponse


# Create your views here.

def index(request):
    """
    页面入口
    :param request:
    :return:
    """
    return render(request, 'index.html')

def initialize(request):
    """
    加载起始页面
    :param request:
    :return:
    """

    file_name = "/Users/apple/Desktop/pa_test_tree.txt"
    with open(file_name, mode='r', encoding='utf-8') as f:
        datas = f.read()

    return_data = {'data': datas}

    return HttpResponse(json.dumps(return_data))

