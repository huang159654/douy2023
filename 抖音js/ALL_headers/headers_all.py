#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# @当前时间 :2024/2/27 16:13
# @Author  : TS
# @Email   : TS@gmail.com
# @File    : ts2.py
# @Software: PyCharm
"""
import json


class ALL_headers():
    def __init__(self):
        pass
    def def_headers(self):
        with open(r'C:\Users\Administrator\PycharmProjects\pythonProject\函数\抖音\抖音js\ALL_headers\package.json', mode='r', encoding='utf-8')as f:
            data=json.load(f)
            headers= data['headers']
            # print(headers)
            return headers

if __name__=='__main__':
    ALL_headers().def_headers()