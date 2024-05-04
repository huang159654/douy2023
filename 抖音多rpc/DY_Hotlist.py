#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# @当前时间 :2023/11/21 1:28
# @Author  : TS
# @Email   : TS@gmail.com
# @File    : ts2.py
# @Software: PyCharm
"""
import json
import urllib.parse

import requests


class DY_Hotlist():#热榜
    def __init__(self):
        with open('info_pl.json', 'r', encoding='utf-8')as f:
            json_data=json.load(f)
            self.url=json_data['Hotlist']['url']
            self.headers = json_data['Hotlist']['ALL_headers']
            self.queries = json_data['Hotlist']['queries']

    def def_xb(self,url=None):
        url = urllib.parse.urlencode(self.queries)
        data = {
            "group": "test_web",
            "action": "test_xb",
            "url": url
        }
        res = requests.get("http://127.0.0.1:5612/business/invoke", params=data)
        d = res.json()
        X_Bogus = d['data']
        return X_Bogus
    def def_parse(self):
        params = self.queries
        params_string = urllib.parse.urlencode(params)
        params["X-Bogus"] = self.def_xb(url=params_string)
        return params
    def def_headers(self):
        params = self.def_parse()
        headers = self.headers
        search_url = self.url
        response = requests.get(url=search_url, params=params, headers=headers).json()
        return response

class DY_Hotlis():
    def __init__(self):
        pass
    def def_Hresponse(self):
        response = DY_Hotlist().def_headers()
        self.def_Hparse(data=response)
    def def_Hparse(self,data=None):
        if data['data']['word_list']:
            for list_data in data['data']['word_list']:
                sentence_id=list_data['sentence_id']
                word=list_data['word']
                key_word = urllib.parse.quote(word)
                res='https://douyin.com/hot/'+sentence_id+'/'+key_word
                print(res)
    def def_Hsave(self):
        pass

if __name__ == '__main__':
    DY_Hotlis().def_Hresponse()