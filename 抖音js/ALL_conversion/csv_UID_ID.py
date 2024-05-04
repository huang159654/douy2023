#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# @当前时间 :2024/3/1 18:04
# @Author  : TS
# @Email   : TS@gmail.com
# @File    : ts2.py
# @Software: PyCharm
"""
import pandas as pd


class Read_csv():#读取 101190400.csv 文件
    def __init__(self):
        pass
    def def_csv(self):
        # 指定要读取的CSV文件路径
        filepath = r'C:\Users\Administrator\PycharmProjects\pythonProject\函数\抖音\抖音js\ALL_csv\抖音评论.csv'
        # 使用pandas的read_csv函数读取CSV文件的所有数据
        df = pd.read_csv(filepath,encoding='utf-8',)
        for row in df.values:
            row_url=row[0] #转换列表，split分割取值
            row_url_id =row[1]  # 转换列表，split分割取值
            url_list_text = row[5]
            dict = {"id": row_url, 'url_list_id':row_url_id,'url_list_text':url_list_text}
            # print(dict)
            yield dict
if __name__=='__main__':
    # Read_sql().def_sql() #读取数据库
    Read_csv().def_csv()#读取csv
