#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# @当前时间 :2024/2/25 14:53
# @Author  : TS
# @Email   : TS@gmail.com
# @File    : ts2.py
# @Software: PyCharm
"""
import pymysql


class Read_sql(): #读取数据库url
    def __init__(self):
        pass
    def def_sql(self):
        db = pymysql.connect(host='localhost', user='root', password='huang159', port=3306, db='dy_creat')
        cursor = db.cursor()
        # 执行SQL查询语句
        cursor.execute('SELECT * FROM url')
        # 获取查询结果
        results = cursor.fetchall()
        # 遍历结果集
        for row in results:
            url_list=row[1].split('/')[4]
            dict = {"id": url_list, }
            # print(url_list)
            yield dict  # 循环数据使用yield