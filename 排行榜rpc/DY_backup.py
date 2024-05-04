#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# @当前时间 :2024/1/6 16:38
# @Author  : TS
# @Email   : TS@gmail.com
# @File    : ts2.py
# @Software: PyCharm
"""
import json
import requests

class DY_Provincial():#省排行榜
    def __init__(self):
        with open('./package.json',mode='r',encoding='utf-8')as f:
            data_json=json.load(f)
            self.url=data_json['Provincial']['url']
            self.headers = data_json['Provincial']['ALL_headers']

    def def_X_Bogus(self,anchor_id=None,room_id=None):
        url = f'aid=6383&app_name=douyin_web&live_id=1&device_platform=web&language=zh-CN&enter_from=page_refresh&cookie_enabled=true&screen_width=1920&screen_height=1080&browser_language=zh-CN&browser_platform=Win32&browser_name=Chrome&browser_version=120.0.0.0&browser_online=true&engine_name=Blink&engine_version=120.0.0.0&os_name=Windows&os_version=10&cpu_core_num=8&device_memory=8&platform=PC&downlink=10&effective_type=4g&round_trip_time=50&channel=channel_pc_web&webid=7317023263425775145&user_agent=Mozilla%2F5.0+(Windows+NT+10.0%3B+Win64%3B+x64)+AppleWebKit%2F537.36+(KHTML,+like+Gecko)+Chrome%2F120.0.0.0+Safari%2F537.36&fp=verify_lr1x5qxq_YoXn1aRt_IAHo_4mz2_BLnu_NaBEBL5bN2vQ&did=0&referer=https:%2F%2Flive.douyin.com%2F&target=&anchor_id={anchor_id}&room_id={room_id}&ranklist_type=1'
        data = {
            "group": "test_web",
            "action": "test_xb",
            "url": url
        }
        res = requests.get("http://127.0.0.1:5612/business/invoke", params=data)
        d = res.json()
        url_xb='https://live.douyin.com/webcast/ranklist/hour_detail/?' + url + '&X-Bogus=' + d['data']
        yield url_xb
    def def_response(self,anchor_id=None,room_id=None):
        for url in self.def_X_Bogus(anchor_id=anchor_id,room_id=room_id):
            response =requests.get(url=url,headers=self.headers).json()
            # print(response)
            yield response


class D_Popularity():
    def __init__(self):
        with open('./package.json', mode='r', encoding='utf-8') as f:
            data_json = json.load(f)
            self.url = data_json['Popularity']['url']
            self.headers = data_json['Popularity']['ALL_headers']
    def def_X_Bogus(self,anchor_id=None,room_id=None):
        url = 'aid=6383&app_name=douyin_web&live_id=1&device_platform=web&language=zh-CN&enter_from=web_live&cookie_enabled=true&screen_width=1920&screen_height=1080&browser_language=zh-CN&browser_platform=Win32&browser_name=Chrome&browser_version=120.0.0.0&browser_online=true&engine_name=Blink&engine_version=120.0.0.0&os_name=Windows&os_version=10&cpu_core_num=8&device_memory=8&platform=PC&downlink=10&effective_type=4g&round_trip_time=50&channel=channel_pc_web&webid=7317023263425775145&user_agent=Mozilla%2F5.0+(Windows+NT+10.0%3B+Win64%3B+x64)+AppleWebKit%2F537.36+(KHTML,+like+Gecko)+Chrome%2F120.0.0.0+Safari%2F537.36&fp=&did=0&referer=https:%2F%2Flive.douyin.com%2Fcategory%2F3_10000_2_2726&target=&anchor_id=62781009263&room_id=7320886645417429812&msToken=nm9TvxBSixf5qsd3FGT97X_BM5rB-awNlcO9nx6P3Hedk4r_kSSsQZKFteYfX2-q81Ryu8LboRLeuDXDkgdFh5cU5lmNrR2OdEl6twIIiC7DYyY309vv'
        data = {
            "group": "test_web",
            "action": "test_xb",
            "url": url
        }
        res = requests.get("http://127.0.0.1:5612/business/invoke", params=data)
        d = res.json()
        url_xb='https://live.douyin.com/webcast/ranklist/popularity/?' + url + '&X-Bogus=' + d['data']
        yield url_xb
    def def_response(self,anchor_id=None,room_id=None):
        for url in self.def_X_Bogus():
            response =requests.get(url=url,headers=self.headers).json()
            # print(response)
            yield response

if __name__=='__main__':
    D_Popularity().def_response()