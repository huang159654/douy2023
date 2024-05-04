#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# @当前时间 :2024/3/1 15:07
# @Author  : TS
# @Email   : TS@gmail.com
# @File    : ts2.py
# @Software: PyCharm
"""
import pymysql


class Read_sql_comments(): #读取数据库comments 评论里面的id和uid
    def __init__(self):
        pass
    def def_sql(self):
        db = pymysql.connect(host='localhost', user='root', password='huang159', port=3306, db='dy_creat')
        cursor = db.cursor()
        # 执行SQL查询语句
        cursor.execute('SELECT * FROM comments')
        # 获取查询结果
        results = cursor.fetchall()
        # 遍历结果集
        for row in results:
            # print(row)
            url_list=row[1]
            url_list_id = row[2]
            url_list_text = row[6]
            # print(url_list_text)
            dict = {"id": url_list, 'url_list_id':url_list_id,'url_list_text':url_list_text}

            yield dict  # 循环数据使用yield

if __name__=='__main__':
    Read_sql_comments().def_sql()