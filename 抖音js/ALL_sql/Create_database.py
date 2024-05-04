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
    def def_Create_database(self):#创建数据库
        db = pymysql.connect(host='localhost', user='root', password='huang159', port=3306)
        cursor = db.cursor()  # 游标
        cursor.execute('SELECT VERSION()')
        data = cursor.fetchone()
        print('Database version:', data)
        cursor.execute("CREATE DATABASE dy_creat CHARACTER SET utf8mb4;")
        db.close()
    def def_url(self): #判断是数据库里面是否创建url表
        db = pymysql.connect(host='localhost', user='root', password='huang159', port=3306, db='dy_creat')
        mycursor = db.cursor()
        mycursor.execute("SHOW TABLES")
        tables = mycursor.fetchall()
        for table in tables:
            if table[0] == "url":
                print("The data table is created!")  # 数据表创建了
                break
        else:
            # 字段是可以自己添加，需要和保存的字段保持一致
            sql = 'CREATE TABLE IF NOT EXISTS url (id INTEGER NOT NULL AUTO_INCREMENT,dy_url TEXT , PRIMARY KEY (id))'
            mycursor.execute(sql)
            print("The table has already been created!")  # 表已经创建好了
    def def_Conten(self): #点赞和评论
        db = pymysql.connect(host='localhost', user='root', password='huang159', port=3306, db='dy_creat')
        mycursor = db.cursor()
        mycursor.execute("SHOW TABLES")
        tables = mycursor.fetchall()
        for table in tables:
            if table[0] == "Conten":
                print("The data table is created!")  # 数据表创建了
                break
        else:
            #字段是可以自己添加，需要和保存的字段保持一致
            sql = 'CREATE TABLE IF NOT EXISTS Conten (id INTEGER NOT NULL AUTO_INCREMENT,awem_id VARCHAR(400) NOT NULL,author VARCHAR(400) NOT NULL, create_time VARCHAR(400) NOT NULL,preview_title VARCHAR(400) NOT NULL,digg_count VARCHAR(400) NOT NULL,comment_count VARCHAR(400) NOT NULL,collect_count VARCHAR(400) NOT NULL,share_count VARCHAR(400) NOT NULL,aweme_id VARCHAR(400) NOT NULL, PRIMARY KEY (id))'
            mycursor.execute(sql)
            print("The table has already been created!")  # 表已经创建好了
    def def_comments(self): #一级评论
        db = pymysql.connect(host='localhost', user='root', password='huang159', port=3306, db='dy_creat')
        mycursor = db.cursor()
        mycursor.execute("SHOW TABLES")
        tables = mycursor.fetchall()
        for table in tables:
            if table[0] == "comments":
                print("The data table is created!")  # 数据表创建了
                break
        else:
            # 字段是可以自己添加，需要和保存的字段保持一致
            sql = 'CREATE TABLE IF NOT EXISTS comments (id INTEGER NOT NULL AUTO_INCREMENT,awem_id VARCHAR(400) NOT NULL, cid VARCHAR(400) NOT NULL,nickname TEXT,sec_uid TEXT,short_id TEXT,text_s TEXT,create_time TEXT,ip_label TEXT,reply_comment_total TEXT,aweme_url TEXT,PRIMARY KEY (id))'
            mycursor.execute(sql)
            print("The table has already been created!")  # 表已经创建好了
    def def_Reviews(self):#子评论
        db = pymysql.connect(host='localhost', user='root', password='huang159', port=3306, db='dy_creat')
        mycursor = db.cursor()
        mycursor.execute("SHOW TABLES")
        tables = mycursor.fetchall()
        for table in tables:
            if table[0] == "Reviews":
                print("The data table is created!")  # 数据表创建了
                break
        else:
            # 字段是可以自己添加，需要和保存的字段保持一致
            sql = 'CREATE TABLE IF NOT EXISTS reviews (id INTEGER NOT NULL AUTO_INCREMENT,awem_id VARCHAR(400) NOT NULL ,cid VARCHAR(400) NOT NULL, text_s TEXT,text TEXT,digg_count TEXT,ip_label TEXT,create_time TEXT,nickname TEXT, PRIMARY KEY (id))'
            mycursor.execute(sql)
            print("The table has already been created!")  # 表已经创建好了
    def def_Personal(self):#个人详情页
        db = pymysql.connect(host='localhost', user='root', password='huang159', port=3306, db='dy_creat')
        mycursor = db.cursor()
        mycursor.execute("SHOW TABLES")
        tables = mycursor.fetchall()
        for table in tables:
            if table[0] == "Personal":
                print("The data table is created!")  # 数据表创建了
                break
        else:
            # 字段是可以自己添加，需要和保存的字段保持一致
            sql = 'CREATE TABLE IF NOT EXISTS Personal (id INTEGER NOT NULL AUTO_INCREMENT,url VARCHAR(400) NOT NULL ,cid VARCHAR(400) NOT NULL, text_s TEXT,text TEXT,digg_count TEXT,ip_label TEXT,create_time TEXT,nickname TEXT, PRIMARY KEY (id))'
            mycursor.execute(sql)
            print("The table has already been created!")  # 表已经创建好了
if __name__=='__main__':
    # Create_data().def_Create_database()
    # Create_data().def_Conten()
    Create_data().def_url()
    # Create_data().def_Reviews()
    # Create_data().def_comments()
    # Create_data().def_Personal()