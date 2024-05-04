#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# @当前时间 :2023/12/21 19:51
# @Author  : TS
# @Email   : TS@gmail.com
# @File    : ts2.py
# @Software: PyCharm
"""
import pymysql
class Sql_data():
    def __init__(self):
        pass
    def sql_create(self):
        db = pymysql.connect(host='localhost',user='root', password='huang159', port=3306)
        cursor = db.cursor()   # 游标
        cursor.execute('SELECT VERSION()')
        data = cursor.fetchone()
        print('Database version:', data)
        cursor.execute("CREATE DATABASE dy_creat DEFAULT CHARACTER SET utf8")
        db.close()

    def sql_table(self):
        # db = pymysql.connect(host='localhost', user='root', password='huang159', port=3306, db='dy_creat')
        # cursor = db.cursor()
        # sql = 'CREATE TABLE IF NOT EXISTS comments_s (id INTEGER NOT NULL AUTO_INCREMENT,awem_id VARCHAR(400) NOT NULL, cid VARCHAR(400) NOT NULL,nickname TEXT,sec_uid TEXT,short_id TEXT,text_s TEXT,create_time TEXT,ip_label TEXT,reply_comment_total TEXT,aweme_url TEXT,PRIMARY KEY (id))'
        # cursor.execute(sql)
        # db = pymysql.connect(host='localhost', user='root', password='huang159', port=3306, db='dy_creat')
        # cursor = db.cursor()
        # sql = 'CREATE TABLE IF NOT EXISTS Conten (id INTEGER NOT NULL AUTO_INCREMENT,awem_id VARCHAR(400) NOT NULL,author VARCHAR(400) NOT NULL, create_time VARCHAR(400) NOT NULL,preview_title VARCHAR(400) NOT NULL,digg_count VARCHAR(400) NOT NULL,comment_count VARCHAR(400) NOT NULL,collect_count VARCHAR(400) NOT NULL,share_count VARCHAR(400) NOT NULL, PRIMARY KEY (id))'
        # cursor.execute(sql)
        # db = pymysql.connect(host='localhost', user='root', password='huang159', port=3306, db='dy_creat')
        # cursor = db.cursor()
        # sql = 'CREATE TABLE IF NOT EXISTS reviews (id INTEGER NOT NULL AUTO_INCREMENT,awem_id VARCHAR(400) NOT NULL ,cid VARCHAR(400) NOT NULL, text_s TEXT,text TEXT,digg_count TEXT,ip_label TEXT,create_time TEXT,nickname TEXT, PRIMARY KEY (id))'
        # cursor.execute(sql)
        #保存抖音URL
        db = pymysql.connect(host='localhost', user='root', password='huang159', port=3306, db='dy_creat')
        cursor = db.cursor()
        sql = 'CREATE TABLE IF NOT EXISTS url (id INTEGER NOT NULL AUTO_INCREMENT,dy_url TEXT , PRIMARY KEY (id))'
        cursor.execute(sql)
        #
        # db = pymysql.connect(host='localhost', user='root', password='huang159', port=3306, db='dy_creat')#微博
        # cursor = db.cursor()
        # sql = 'CREATE TABLE IF NOT EXISTS wb (id INTEGER NOT NULL AUTO_INCREMENT,nickname TEXT,Released TEXT,content TEXT,  PRIMARY KEY (id))'
        # cursor.execute(sql)
if __name__=='__main__':
    # Sql_data().sql_create()
    Sql_data().sql_table()
