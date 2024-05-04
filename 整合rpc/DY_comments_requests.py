#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# @当前时间 :2024/1/30 11:09
# @Author  : TS
# @Email   : TS@gmail.com
# @File    : ts2.py
# @Software: PyCharm
"""
import math
import time
import random

import requests

from DY_headers import ALL_headers
from DY_Read import Read_sql
from DY_Read import Read_csv

class Comments_requests_sql():
    def __init__(self):
        pass

    def def_headers(self):
        headers=ALL_headers().def_comments_headers()
        return headers
    def def_url(self):
        url='https://www.douyin.com/aweme/v1/web/comment/list/?'
        return url
    def def_queries(self,aweme_id=None,cursor=None):
        queries=f'device_platform=webapp&aid=6383&channel=channel_pc_web&aweme_id={aweme_id}&cursor={cursor}&count=20&item_type=0&whale_cut_token=&cut_version=1&rcFT=&pc_client_type=1&version_code=170400&version_name=17.4.0&cookie_enabled=true&screen_width=1920&screen_height=1080&browser_language=zh-CN&browser_platform=Win32&browser_name=Chrome&browser_version=120.0.0.0&browser_online=true&engine_name=Blink&engine_version=120.0.0.0&os_name=Windows&os_version=10&cpu_core_num=8&device_memory=8&platform=PC&downlink=10&effective_type=4g&round_trip_time=50&webid=7317023263425775145&msToken=k0zT6tQfYBzxBl_fuj_uWtB23cRXcVn3dXonl_MdBkPS4ZqXrvzcJH-GkfyfDBlrzZ2aQgD_z7wu-bYRpakeJmnhUXiOHWDc7aENI8qotgDpsMteqao='
        return queries
    def def_requests(self):
        for data_s in Read_sql().def_sql():
            aweme_id = data_s['id']
            data = {
                "group": "test_web",
                "action": "test_xb",
                "url": self.def_queries(aweme_id=aweme_id)
            }
            res = requests.get("http://127.0.0.1:5612/business/invoke", params=data)
            d = res.json()
            x_b = self.def_url() + self.def_queries(aweme_id=aweme_id) + '&X-Bogus=' + d['data']
            response = requests.get(url=x_b, headers=self.def_headers()).json()
            if response['comments'] != None:
                total = response['total']
                dai = total / 20
                tota_l = math.ceil(dai)
                dict = {'tota_l': [tota_l],'aweme_id':[aweme_id]}
                yield dict
            else:
                response['comments'] = None
                with open('评论url错误链接.txt', mode='a', ) as f:
                    url = 'https://www.douyin.com/video/' + aweme_id
                    txt = url + '\n'  # 数据分行
                    f.write(txt)
    def def_tota_l(self):
        for data_s in self.def_requests():
            data = data_s['tota_l'][0]
            aweme_id = data_s['aweme_id'][0]
            for coun in range(0, data):
                cursor = coun * 20
                print(f'正在采集{cursor, }页评论')
                data = {
                    "group": "test_web",
                    "action": "test_xb",
                    "url": self.def_queries(aweme_id=aweme_id,cursor=cursor)
                }
                res = requests.get("http://127.0.0.1:5612/business/invoke", params=data)
                d = res.json()
                x_b = self.def_url() + self.def_queries(aweme_id=aweme_id,cursor=cursor) + '&X-Bogus=' + d['data']
                response = requests.get(url=x_b, headers=self.def_headers()).json()
                randoms = random.randint(5, 15)
                time.sleep(randoms)
                if response['comments'] != None:
                    dict = {'response': response, }
                    yield dict
                else:
                    response['comments'] = None
                    break
class Comments_requests_csv():#csv文件
    def __init__(self):
        pass
    def def_headers(self):
        headers=ALL_headers().def_comments_headers()
        return headers
    def def_url(self):
        url='https://www.douyin.com/aweme/v1/web/comment/list/?'
        return url
    def def_queries(self,aweme_id=None,cursor=None):
        queries=f'device_platform=webapp&aid=6383&channel=channel_pc_web&aweme_id={aweme_id}&cursor={cursor}&count=20&item_type=0&whale_cut_token=&cut_version=1&rcFT=&pc_client_type=1&version_code=170400&version_name=17.4.0&cookie_enabled=true&screen_width=1920&screen_height=1080&browser_language=zh-CN&browser_platform=Win32&browser_name=Chrome&browser_version=120.0.0.0&browser_online=true&engine_name=Blink&engine_version=120.0.0.0&os_name=Windows&os_version=10&cpu_core_num=8&device_memory=8&platform=PC&downlink=10&effective_type=4g&round_trip_time=50&webid=7317023263425775145&msToken=k0zT6tQfYBzxBl_fuj_uWtB23cRXcVn3dXonl_MdBkPS4ZqXrvzcJH-GkfyfDBlrzZ2aQgD_z7wu-bYRpakeJmnhUXiOHWDc7aENI8qotgDpsMteqao='
        return queries
    def def_requests(self):
        for data_s in Read_csv().def_csv():
            aweme_id = data_s['id']
            data = {
                "group": "test_web",
                "action": "test_xb",
                "url": self.def_queries(aweme_id=aweme_id)
            }
            res = requests.get("http://127.0.0.1:5612/business/invoke", params=data)
            d = res.json()
            x_b = self.def_url() + self.def_queries(aweme_id=aweme_id) + '&X-Bogus=' + d['data']
            response = requests.get(url=x_b, headers=self.def_headers()).json()
            if response['comments'] != None:
                total = response['total']
                dai = total / 20
                tota_l = math.ceil(dai)
                dict = {'tota_l': [tota_l],'aweme_id':[aweme_id],'response':response}
                yield dict
            else:
                response['comments'] = None
                with open('评论url错误链接.txt', mode='a', ) as f:
                    url = 'https://www.douyin.com/video/' + aweme_id
                    txt = url + '\n'  # 数据分行
                    f.write(txt)
    def def_tota_l(self):
        for data_s in self.def_requests():
            data = data_s['tota_l'][0]
            aweme_id = data_s['aweme_id'][0]
            for coun in range(0, data):
                cursor = coun * 20
                print(f'正在采集{cursor,aweme_id }页评论')
                data = {
                    "group": "test_web",
                    "action": "test_xb",
                    "url": self.def_queries(aweme_id=aweme_id,cursor=cursor)
                }
                res = requests.get("http://127.0.0.1:5612/business/invoke", params=data)
                d = res.json()
                x_b = self.def_url() + self.def_queries(aweme_id=aweme_id,cursor=cursor) + '&X-Bogus=' + d['data']
                response = requests.get(url=x_b, headers=self.def_headers()).json()
                # randoms = random.randint(5, 15)
                # time.sleep(randoms)
                if response['comments'] != None:
                    dict = {'response': response,'tota_l': [data],'aweme_id':[aweme_id], }
                    yield dict
                else:
                    response['comments'] = None
                    break

if __name__=='__main__':
    Comments_requests_sql().def_tota_l()
    # Comments_requests_csv().def_tota_l()