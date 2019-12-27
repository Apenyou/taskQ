"""
Copyright (c) 2019 Baidu.com, Inc. All Rights Reserved
Authors: 郭志强(guozhiqiang05@baidu.com)
Date: 2019-12-18 16:02
"""
from django.http import HttpResponse,JsonResponse

# def hello(request):
#     # return HttpResponse('hello world123')  #返回普通文本数据
#     ret = request.get()
#     return JsonResponse({'data':'response'})  #返回json格式数据


from django.shortcuts import HttpResponse, render, redirect


# Create your views here.


def hello(request):
    result = ""
    for k, v in request.GET.items():
        result += k + " --> " + v
        result += ","
    return HttpResponse("从Request中获取Value的值是{0}".format(result))
