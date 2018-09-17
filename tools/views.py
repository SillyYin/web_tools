from django.shortcuts import render
import re
import json
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt


# Create your views here.


def index(request):
    """
    页面入口
    :param request:
    :return:
    """
    return render(request, 'index.html')

@csrf_exempt
def initialize(request):
    """
    加载起始页面
    :param request:
    :return:
    """

    file_name = "/Users/apple/Desktop/pa_test_tree.txt"
    with open(file_name, mode='r', encoding='utf-8') as f:
        datas = f.read()
    data_list = datas.split('\n\n')
    for data in data_list:
        data.strip().replace('\t', '')
    print(len(data_list))
    print(data_list[0])

    return_data = {'data': data_list}

    return HttpResponse(json.dumps(return_data))

