#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# @当前时间 :2024/1/27 19:53
# @Author  : TS
# @Email   : TS@gmail.com
# @File    : ts2.py
# @Software: PyCharm
"""
import pymysql
import pandas as pd
from DY_xlsx import Xlsx
from DY_xlsx import Xlsx_video
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
class Read_csv():#读取 101190400.csv 文件
    def __init__(self):
        pass
    def def_csv(self):
        # 指定要读取的CSV文件路径
        filepath = '101190400.csv'
        # 使用pandas的read_csv函数读取CSV文件的所有数据
        df = pd.read_csv(filepath,encoding='utf-8',)
        for row in df.values:
            # 在这里处理每一行数据
            row_url=list(row)[0].split('/')[4] #转换列表，split分割取值
            dict={'id':row_url}
            yield dict
if __name__=='__main__':
    Read_sql().def_sql() #读取数据库
#     Read_csv().def_csv()#读取csv
