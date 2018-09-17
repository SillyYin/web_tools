from django.shortcuts import render
import re

# Create your views here.

def initialize(request):
    """
    加载起始页面
    :param request:
    :return:
    """

    file_name = "/Users/apple/Desktop/test_zwb.txt"
    with open(file_name, mode='r', encoding='utf-8') as f:
        datas = f.readlines()

    data_temp = list()
    data_list = list() # 以每一条数据为元素的列表
    index_list = list() # 每个数据的从句的位置
    index_temp = list()
    return_data_temp = dict() # 每一个数据的字典
    return_data = list()

    for data in datas:
        if data != '\n':
            data_temp.append(data)
        else:
            if len(data_temp) > 0:
                data_list.append(data_temp.copy())
            data_temp.clear()

    pattern = re.compile(r'（从句）')

    for data in data_list:
        for i in range(len(data)):
            if (pattern.search(data[i])):
                index_temp.append(i)
        index_list.append(index_temp.copy())
        index_temp.clear()

    for data in data_list:
        for item in data:
            item.split(' ')
        print(data)

    for i in range(len(data_list)):
        if len(index_list[i]) == 0:
            return_data_temp['name'] = data_list[i][0]
            return_data_temp['children'] = data_list[i][1]
        return_data.append(return_data_temp.copy())
        return_data_temp.clear()
    print(return_data_temp)
    print(return_data)


initialize('123')
