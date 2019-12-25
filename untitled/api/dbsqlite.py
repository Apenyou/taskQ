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
    c.execute('INSERT INTO table_list (taskid, ctime, title, status, content, dtime, rank) VALUES (%s, %s, %s, %s, %s, %s, %s)'%(taskid, ctime, title, status, content, dtime, rank))


def UPDATE(taskid, kay, val):
    c.execute("UPDATE table_list set status = 25 where taskid=1")


def DELETE(taskid):
    c.execute("DELETE from table_list where taskid=2;")


def SELECT():
    cursor = c.execute("SELECT taskid, ctime, title, status, content, dtime, rank from table_list")
    return cursor

def sql(request, *val):
    print('================')
    return HttpResponse('================', val)
    #
    # request(*val)
    # conn.commit()
    # conn.close()
    # return HttpResponse(cursor)
if __name__ == '__main__':
    sql(INSERT,3,2,3,4,5,6,7)

