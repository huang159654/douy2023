#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# @当前时间 :2024/2/27 13:25
# @Author  : TS
# @Email   : TS@gmail.com
# @File    : ts2.py
# @Software: PyCharm
"""
import pymysql
class Create_data():
    def __init__(self):
        pass
    def def_data(self):
        db = pymysql.connect(host='localhost', user='root', password='huang159', port=3306, db='dy_creat')
        mycursor = db.cursor()
        mycursor.execute("SHOW TABLES")
        tables = mycursor.fetchall()
        for table in tables:
            if table[0] == "url":
                print("The data table is created!")  # 数据表创建了
                break
        else:
            sql = 'CREATE TABLE IF NOT EXISTS url (id INTEGER NOT NULL AUTO_INCREMENT,dy_url TEXT , PRIMARY KEY (id))'
            mycursor.execute(sql)
            print("The table has already been created!")  # 表已经创建好了
    def def_Conten(self):
        db = pymysql.connect(host='localhost', user='root', password='huang159', port=3306, db='dy_creat')
        mycursor = db.cursor()
        mycursor.execute("SHOW TABLES")
        tables = mycursor.fetchall()
        for table in tables:
            if table[0] == "Conten":
                print("The data table is created!")  # 数据表创建了
                break
        else:
            sql = 'CREATE TABLE IF NOT EXISTS Conten (id INTEGER NOT NULL AUTO_INCREMENT,awem_id VARCHAR(400) NOT NULL,author VARCHAR(400) NOT NULL, create_time VARCHAR(400) NOT NULL,preview_title VARCHAR(400) NOT NULL,digg_count VARCHAR(400) NOT NULL,comment_count VARCHAR(400) NOT NULL,collect_count VARCHAR(400) NOT NULL,share_count VARCHAR(400) NOT NULL,aweme_id VARCHAR(400) NOT NULL, PRIMARY KEY (id))'
            mycursor.execute(sql)
            print("The table has already been created!")  # 表已经创建好了