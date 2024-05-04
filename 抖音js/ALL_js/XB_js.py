#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# @当前时间 :2024/2/28 12:58
# @Author  : TS
# @Email   : TS@gmail.com
# @File    : ts2.py
# @Software: PyCharm
"""
import execjs
class XB_js(): #解密x_bogus
    def __init__(self):
        pass
    def def_xb(self,params=None):
        x_bogus=execjs.compile(open(r'C:\Users\Administrator\PycharmProjects\pythonProject\函数\抖音\抖音js\ALL_js\x_b.js',mode='r',encoding='utf-8').read()).call('get_dy_xb',params)
        return x_bogus
    def def_execjs(self):
        with open(r"C:\Users\Administrator\PycharmProjects\pythonProject\函数\抖音\抖音js\ALL_js\x_b.js") as f:
            js_data = f.read()
        js_compile = execjs.compile(js_data)
        return js_compile
