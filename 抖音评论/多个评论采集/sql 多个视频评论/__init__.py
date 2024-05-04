#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# @当前时间 :2024/2/25 15:05
# @Author  : TS
# @Email   : TS@gmail.com
# @File    : ts2.py
# @Software: PyCharm
"""
import pymysql


def query_data(cid,):
        db = pymysql.connect(host='localhost', user='root', password='huang159', port=3306, db='dy_creat')
        mycursor = db.cursor()
        sql = "select * from comments_s where cid={}".format(cid)
        mycursor.execute(sql)
        ret = mycursor.fetchone()
        if ret:
            print(ret)

        else:
            print(ret,'a')
query_data('117298623841848050458')