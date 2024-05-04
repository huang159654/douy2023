#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# @当前时间 :2023/11/26 15:18
# @Author  : TS
# @Email   : TS@gmail.com
# @File    : ts2.py
# @Software: PyCharm
"""
import json
import urllib.parse

import requests


class DY_core():#单个视频核心

    def __init__(self):
        with open('info_pl.json', 'r', encoding='utf-8') as f:
            data_json = json.load(f)
            self.url = data_json['single']['url']
            self.headers = data_json['single']['ALL_headers']
            self.queries = data_json['single']['queries']
    def def_xb(self,url=None):
        queries=self.queries
        url = urllib.parse.urlencode(queries)
        data = {
            "group": "test_web",
            "action": "test_xb",
            "url": url
        }
        res = requests.get("http://127.0.0.1:5612/business/invoke", params=data)
        d = res.json()
        X_Bogus = d['data']
        return X_Bogus

    def def_queries(self,aweme_id):
        self.queries['aweme_id']=aweme_id
        params=self.queries
        params_string = urllib.parse.urlencode(params)
        params["X-Bogus"] = self.def_xb(url=params_string)
        return params
    def def_headers(self,):
        headers = self.headers
        return headers
    def def_url(self):
        url=self.url
        return url



# if __name__=="__main__":
    # DY_core().def_headers()