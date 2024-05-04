#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# @当前时间 :2024/2/4 15:43
# @Author  : TS
# @Email   : TS@gmail.com
# @File    : ts2.py
# @Software: PyCharm
"""
import json
import math
import random
import time

import requests
import urllib.parse
from DY_headers import ALL_headers
from DY_comments_requests import Comments_requests_csv
from DY_comments_requests import Comments_requests_sql


class DY_secondary_comments_sql(): #子评论数据库
    def __init__(self):
        pass
    def def_headers(self):
        headers = ALL_headers().dwf_secondary_comments_headers()
        return headers
    def def_url(self):
        url='https://www.douyin.com/aweme/v1/web/comment/list/reply/?'
        return url
    def def_queries(self,aweme_id=None,cid=None):#第一次参数
        queries = {
            'device_platform': 'webapp',
            'aid': '6383',
            'channel': 'channel_pc_web',
            'item_id': aweme_id,
            'comment_id': cid,
            'cut_version': '1',
            'cursor': '0',
            'count': '20',
            'item_type': '0',
            'pc_client_type': '1',
            'version_code': '170400',
            'version_name': '17.4.0',
            'cookie_enabled': 'true',
            'screen_width': '1920',
            'screen_height': '1080',
            'browser_language': 'zh-CN',
            'browser_platform': 'Win32',
            'browser_name': 'Chrome',
            'browser_version': '120.0.0.0',
            'browser_online': 'true',
            'engine_name': 'Blink',
            'engine_version': '120.0.0.0',
            'os_name': 'Windows',
            'os_version': '10',
            'cpu_core_num': '8',
            'device_memory': '8',
            'platform': 'PC',
            'downlink': '10',
            'effective_type': '4g',
            'round_trip_time': '100',
            'webid': '7317023263425775145',
            'msToken': 'Wyxspw5cBc2D1c1u9o4dYCI0aAOarLewCGg53NeiuPh3Lul0d4fJpuLIMFjT49Yab8yrSbo9Pe5vR-k-RLGxt-U0uizeytLJmPe4aoGmN0lqJO2bkglor3g4WRTK',
        }
        params = urllib.parse.urlencode(queries)
        return params
    def def_queries_s(self,aweme_id=None,cid=None,cursor=None):#翻页参数
        queries = {
            'device_platform': 'webapp',
            'aid': '6383',
            'channel': 'channel_pc_web',
            'item_id': aweme_id,
            'comment_id': cid,
            'cut_version': '1',
            'cursor': cursor,
            'count': '20',
            'item_type': '0',
            'pc_client_type': '1',
            'version_code': '170400',
            'version_name': '17.4.0',
            'cookie_enabled': 'true',
            'screen_width': '1920',
            'screen_height': '1080',
            'browser_language': 'zh-CN',
            'browser_platform': 'Win32',
            'browser_name': 'Chrome',
            'browser_version': '120.0.0.0',
            'browser_online': 'true',
            'engine_name': 'Blink',
            'engine_version': '120.0.0.0',
            'os_name': 'Windows',
            'os_version': '10',
            'cpu_core_num': '8',
            'device_memory': '8',
            'platform': 'PC',
            'downlink': '10',
            'effective_type': '4g',
            'round_trip_time': '100',
            'webid': '7317023263425775145',
            'msToken': 'Wyxspw5cBc2D1c1u9o4dYCI0aAOarLewCGg53NeiuPh3Lul0d4fJpuLIMFjT49Yab8yrSbo9Pe5vR-k-RLGxt-U0uizeytLJmPe4aoGmN0lqJO2bkglor3g4WRTK',
        }
        params = urllib.parse.urlencode(queries)
        return params
    def def_response(self):
        for data_s in Comments_requests_sql().def_tota_l():
            data = data_s['response']
            if data['comments']:
                for compile in data['comments']:
                    text = compile.get('text')  # 评论内容
                    cid = compile.get('cid')
                    aweme_id = compile.get('aweme_id')
                    dict = {'text': text, 'cid': cid, 'aweme_id': aweme_id, }
                    # print(dict)
                    yield dict
    def def_pagination(self):#请求得到翻页页数
        for data_a in self.def_response():
            cid = data_a['cid']
            aweme_id = data_a['aweme_id']
            text = data_a['text']
            data = {
                "group": "test_web",
                "action": "test_xb",
                "url": self.def_queries(aweme_id=aweme_id,cid=cid)
            }
            res = requests.get("http://127.0.0.1:5612/business/invoke", params=data)
            d = res.json()
            x_b = self.def_url() + self.def_queries(aweme_id=aweme_id,cid=cid) + '&X-Bogus=' + d['data']
            response = requests.get(url=x_b, headers=self.def_headers()).json()
            if response['comments'] != None:
                total=response.get('total')
                dai = total / 20
                tota_l = math.ceil(dai)
                dict = {'tota_l': [tota_l], 'aweme_id': [aweme_id], 'cid': [cid], 'text': [text]}
                yield dict
            else:
                response['comments'] = None
                with open('评论url错误链接.txt', mode='a', ) as f:
                    url = 'https://www.douyin.com/video/' + aweme_id
                    txt = url + '\n'  # 数据分行
                    f.write(txt)
    def def_def_tota_l(self):
        for data_s in self.def_pagination():
            tota_l = data_s['tota_l'][0]
            aweme_id = data_s['aweme_id'][0]
            cid = data_s['cid'][0]
            text = data_s['text'][0]
            data = {
                "group": "test_web",
                "action": "test_xb",
                "url": self.def_queries_s(aweme_id=aweme_id,cursor=tota_l,cid=cid)
            }
            res = requests.get("http://127.0.0.1:5612/business/invoke", params=data)
            d = res.json()
            x_b = self.def_url() + self.def_queries_s(aweme_id=aweme_id,cursor=tota_l,cid=cid) + '&X-Bogus=' + d['data']
            response = requests.get(url=x_b, headers=self.def_headers()).json()
            randoms = random.randint(5, 15)
            time.sleep(randoms)
            if response['comments'] != None:
                dict = {'response': response, 'text': text}
                yield dict
            else:
                response['comments'] = None
                continue

if __name__=='__main__':
    DY_secondary_comments_sql().def_def_tota_l()