"""
Copyright (c) 2019 Baidu.com, Inc. All Rights Reserved
Authors: 郭志强(guozhiqiang05@baidu.com)
Date: 2019-12-25 15:29
"""
from django.http import HttpResponse,JsonResponse

from django.db import connection
c = connection.cursor()

cursor = 'succeed'
def INSERT(params):
    # print(type(params))
    # print(len(params))
    '''
    :param taskid:
    :param ctime:
    :param title:
    :param status:
    :param content:
    :param dtime:
    :param rank:
    :return:
    '''

    taskid, ctime, title, status, content, dtime, rank = [x for x in params]
    sqllint = 'INSERT INTO table_list (taskid, ctime, title, status, content, dtime, rank) VALUES (%s, %s, %s, %s, %s, %s, %s)' %(taskid, ctime, title, status, content, dtime, rank)
    c.execute(sqllint)
    return cursor

def UPDATE(params):
    '''
    :param taskid:
    :param kay:
    :param val:
    :return:
    '''
    taskid, key, val = [x for x in params]
    sqllint = "UPDATE table_list set %s  = %s where taskid = %s" %(key, val, taskid)
    c.execute(sqllint)
    return cursor

def DELETE(params):
    '''
    :param taskid:
    :return:
    '''
    taskid = [x for x in params]
    sqllint = "DELETE from table_list where taskid = %s" %(taskid[0])
    c.execute(sqllint)
    return cursor

def SELECT():
    '''
    :return: all list
    '''
    cursor = c.execute("SELECT taskid, ctime, title, status, content, dtime, rank from table_list")
    return cursor

def sql(request, *val):
    '''
    :param request:  perform SQL funciton
    :param val: param
    :return:
    '''
    return(request(*val))

def control(request):
    '''
    :param request:
    :return:
    '''
    k = list(request.GET.items())
    funname = k[0][1]
    params = k[1][1].split(',')
    return HttpResponse(globals()[funname](params))

if __name__ == '__main__':
    pass
    # sql(INSERT,3,2,3,4,5,6,7)
    # sql(UPDATE, 'status', 3)
    # sql(DELETE, 2)
    # sql(SELECT)

