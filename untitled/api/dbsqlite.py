"""
Copyright (c) 2019 Baidu.com, Inc. All Rights Reserved
Authors: 郭志强(guozhiqiang05@baidu.com)
Date: 2019-12-25 15:29
"""
from django.http import HttpResponse,JsonResponse
import sqlite3
import os

cursor = 'succeed'
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
dbpath = os.path.join(BASE_DIR, 'db.sqlite3')
conn = sqlite3.connect(dbpath)
c = conn.cursor()

def INSERT(taskid, ctime, title, status, content, dtime, rank):
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
    c.execute('INSERT INTO table_list (taskid, ctime, title, status, content, dtime, rank) VALUES (%s, %s, %s, %s, %s, %s, %s)' % (taskid, ctime, title, status, content, dtime, rank))


def UPDATE(taskid, key, val):
    '''
    :param taskid:
    :param kay:
    :param val:
    :return:
    '''
    c.execute("UPDATE table_list set %s  = %s where taskid = %s" % (key, val, taskid))


def DELETE(taskid):
    '''
    :param taskid:
    :return:
    '''
    c.execute("DELETE from table_list where taskid = %s;" % (taskid))


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
    # request.GET.get()
    query = request.query_params

    print('================')
    return HttpResponse('================', query)
    #
    # request(*val)
    # conn.commit()
    # conn.close()
    # return HttpResponse(cursor)
if __name__ == '__main__':
    sql(INSERT,3,2,3,4,5,6,7)
    sql(UPDATE, 'status', 3)
    sql(DELETE, 2)
    sql(SELECT)

