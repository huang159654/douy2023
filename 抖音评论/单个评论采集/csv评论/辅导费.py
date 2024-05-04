#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# @当前时间 :2024/2/26 12:31
# @Author  : TS
# @Email   : TS@gmail.com
# @File    : ts2.py
# @Software: PyCharm
"""
import pymysql


def sql_table():
    db = pymysql.connect(host='localhost', user='root', password='huang159', port=3306, db='dy_creat')
    mycursor = db.cursor()
    mycursor.execute("SHOW TABLES")
    tables = mycursor.fetchall()
    for table in tables:
        if table[0] == "comments_s":
            print("The data table is created!")#数据表创建了
            break
    else:
        sql = 'CREATE TABLE IF NOT EXISTS comments_s (id INTEGER NOT NULL AUTO_INCREMENT,awem_id VARCHAR(400) NOT NULL, cid VARCHAR(400) NOT NULL,nickname TEXT,sec_uid TEXT,short_id TEXT,text_s TEXT,create_time TEXT,ip_label TEXT,reply_comment_total TEXT,aweme_url TEXT,PRIMARY KEY (id))'
        mycursor.execute(sql)
        print("The table has already been created!")#表已经创建好了
sql_table()