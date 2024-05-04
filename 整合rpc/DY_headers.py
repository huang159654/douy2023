#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# @当前时间 :2024/1/29 15:59
# @Author  : TS
# @Email   : TS@gmail.com
# @File    : ts2.py
# @Software: PyCharm
"""
import json


class ALL_headers():
    def def_retweet_headers(self):#点赞和转发
        with open('./package.json',mode='r',encoding='utf-8')as f:
            data=json.load(f)
            headers=data['Like_retweet']['ALL_headers']
            return headers

    def def_comments_headers(self): #一级评论
        with open('./package.json',mode='r',encoding='utf-8')as f:
            data=json.load(f)
            headers=data['comments']['ALL_headers']
            return headers
    def dwf_secondary_comments_headers(self):
        with open('./package.json',mode='r',encoding='utf-8')as f:
            data=json.load(f)
            headers=data['secondary_comments']['ALL_headers']
            # print(ALL_headers)
            return headers



if __name__=='__main__':
    ALL_headers().dwf_secondary_comments_headers()