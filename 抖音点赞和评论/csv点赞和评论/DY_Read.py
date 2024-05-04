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

class Read_csv():#读取 101190400.csv 文件
    def __init__(self):
        pass
    def def_csv(self):
        # 指定要读取的CSV文件路径
        filepath = '点赞和评论url.csv'
        # 使用pandas的read_csv函数读取CSV文件的所有数据
        df = pd.read_csv(filepath,encoding='utf-8',)
        for row in df.values:
            # 在这里处理每一行数据
            row_url=list(row)[0].split('/')[4] #转换列表，split分割取值
            dict={'id':row_url}
            # print(dict)
            # print('Collecting comments. Please wait！')
            yield dict
if __name__=='__main__':
    # Read_sql().def_sql() #读取数据库
    Read_csv().def_csv()#读取csv
