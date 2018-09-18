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

    # file_name = "/Users/apple/Desktop/pa_test_tree的副本.txt"
    file_name = "/Users/apple/Desktop/pa_test_tree.txt"
    bool_list = list()

    try:
        with open(file_name, mode='r', encoding='utf-8') as f:
            datas = f.read()
    except Exception as e:
        print("Exceptin: ", e)
        return_data = {'status': 'FAIL'}
        return HttpResponse(json.dumps(return_data))

    data_list = datas.split('\n\n')

    for i in range(len(data_list)):
        bool_list.append("true")

    return_data = {'data': data_list, 'status': 'SUCCESS', 'bool': bool_list}

    return HttpResponse(json.dumps(return_data))

@csrf_exempt
def save(request):
    """
    重写文件
    :param request:
    :return:
    """

    right_list = list()
    false_list = list()

    parameter = request.POST['bool_list']
    bool_list = parameter[1:-1].split(',')

    print(type(parameter))
    print(bool_list)

    for index in range(len(bool_list)):
        if bool_list[index] == '\"true\"':
            right_list.append(index)
        elif bool_list[index] == '\"false\"':
            false_list.append(index)

    file_name = "/Users/apple/Desktop/pa_test_tree.txt"

    try:
        with open(file_name, mode='r', encoding='utf-8') as f:
            datas = f.read()
    except Exception as e:
        print("Exceptin: ", e)
        return_data = {'status': 'FAIL'}
        return HttpResponse(json.dumps(return_data))

    data_list = datas.split('\n\n')

    right_file_name = "/Users/apple/Desktop/pa_test_tree_right.txt"
    false_file_name = "/Users/apple/Desktop/pa_test_tree_false.txt"
    write_file_name = ""

    try:
        for index in range(len(data_list)):
            if index in right_list:
                write_file_name = right_file_name
            if index in false_list:
                write_file_name = false_file_name
            with open(write_file_name, mode='a', encoding='utf-8') as f:
                f.write(data_list[index] + '\n\n')
    except Exception as e:
        print("Exception: ", e)
        return_data = {'status': 'FAIL'}
        return  HttpResponse(json.dumps(return_data))

    return_data = {'status': 'SUCCESS'}
    return HttpResponse(json.dumps(return_data))

