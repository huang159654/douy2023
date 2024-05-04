#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# @当前时间 :2023/11/20 21:12
# @Author  : TS
# @Email   : TS@gmail.com
# @File    : ts2.py
# @Software: PyCharm
"""
import json
import os
import urllib.parse
import  pandas as pd

import requests


class DY_Personal():#个人详细
    def __init__(self):

        with open('info_pl.json', 'r', encoding='utf-8') as f:
            json_data=json.load(f)
            self.url=json_data['Personal_details']['url']
            self.headers = json_data['Personal_details']['ALL_headers']
            self.queries = json_data['Personal_details']['queries']
    def def_xb(self,url=None,sec_user_id=None):
        url = urllib.parse.urlencode(self.queries)
        data = {
            "group": "test_web",
            "action": "test_xb",
            "url": url
        }
        res = requests.get("http://127.0.0.1:5612/business/invoke", params=data)
        d = res.json()
        X_Bogus=d['data']
        return X_Bogus
    def def_parse(self,sec_user_id):
        self.queries['sec_user_id']=sec_user_id #搜索参数传递
        params = self.queries
        params_string = urllib.parse.urlencode(params)
        params["X-Bogus"] = self.def_xb(url=params_string)
        return params
    def def_headers(self,sec_user_id):
        params = self.def_parse(sec_user_id)
        headers = self.headers
        search_url = self.url
        response = requests.get(url=search_url, params=params, headers=headers).json()
        return response
class DY_parses():
    def __init__(self):
        pass
    def def_response(self,sec_user_id):
        response=DY_Personal().def_headers(sec_user_id)
        self.def_parse(data=response)
    def def_parse(self,data=None):
        dict= {}
        if data['user']:
            ip_location=data['user']['ip_location'] #ip地址
            nickname = data['user']['nickname']  # 昵称
            max_follower_count = data['user']['max_follower_count']  # 粉丝
            total_favorited = data['user']['total_favorited']  # 获赞
            unique_id = data['user']['unique_id']  # 抖音号
            uid = data['user']['uid']  # 用户uid
            signature = data['user']['signature'].replace('\n','')  # 作者简介
            dict={'昵称':[nickname],'ip地址':[ip_location],'粉丝':[max_follower_count],'获赞':[total_favorited],'抖音号':[unique_id],'用户uid':[uid],'作者简介':[signature]}
        self.def_save(data=dict)
    def def_save(self,data=None):
        dataframe = pd.DataFrame(data=data)
        if not os.path.exists('101190400.csv'):
            dataframe.to_csv('./101190400.csv', index=False, )
        dataframe.to_csv('./101190400.csv',  encoding='utf_8_sig', header=True, index=False)
        print('save_access')
