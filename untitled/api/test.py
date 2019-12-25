"""
Copyright (c) 2019 Baidu.com, Inc. All Rights Reserved
Authors: 郭志强(guozhiqiang05@baidu.com)
Date: 2019-12-18 16:02
"""
from django.http import HttpResponse,JsonResponse

def hello(request):
    return HttpResponse(str(request)+'hello world123')  #返回普通文本数据
    # return JsonResponse({'data':'response'})  //返回json格式数据