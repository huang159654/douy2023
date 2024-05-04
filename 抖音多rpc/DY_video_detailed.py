#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# @当前时间 :2023/11/8 2:21
# @Author  : TS
# @Email   : TS@gmail.com
# @File    : ts2.py
# @Software: PyCharm
"""
import json
import os
import pprint
import time

import pandas
import pandas as pd
import requests


class DY_video(): #视频+点赞
    def __init__(self):

        with open('info_pl.json', 'r', encoding='utf-8') as f:
            json_data = json.load(f)
            self.url = json_data['video']['url']
            self.headers = json_data['video']['ALL_headers']
            self.queries = json_data['video']["queries"]
            # print(self.url,self.ALL_headers,self.queries)
    def def_xbogus(self,awem_id):
        self.aweme_id = awem_id
        url=f'device_platform=webapp&aid=6383&channel=channel_pc_web&aweme_id={self.aweme_id}&pc_client_type=1&version_code=190500&version_name=19.5.0&cookie_enabled=true&screen_width=1280&screen_height=720&browser_language=zh-CN&browser_platform=Win32&browser_name=Chrome&browser_version=119.0.0.0&browser_online=true&engine_name=Blink&engine_version=119.0.0.0&os_name=Windows&os_version=10&cpu_core_num=8&device_memory=8&platform=PC&downlink=10&effective_type=4g&round_trip_time=0&webid=7287133158548440630&msToken=7-Xer3neNEVCuOhzJtH_bEpYOq2S47mZhOXG5av27o0SNaZiYAP16kX3PiccZKmG7s6YVgPdXINjJy1xBUPAlSTUWQeuUVQKnJ3u3A4R6vD2Y-ckVJe3YXvOWNSl'
        data = {
            "group": "test_web",
            "action": "test_xb",
            "url": url
        }
        res = requests.get("http://127.0.0.1:5612/business/invoke", params=data)
        d = res.json()
        x_b = 'https://www.douyin.com/aweme/v1/web/aweme/detail/?' + url + '&X-Bogus=' + d['data']
        response = requests.get(url=x_b, headers=self.headers).json()
        # print(response)
        return response
class Parse():
    def def_parse(self,awem_id):#解析数据
        data=DY_video().def_xbogus(awem_id)
        if data['aweme_detail']:
            preview_title=data['aweme_detail']['preview_title']#标题
            comment_count = data['aweme_detail']['statistics']['comment_count']#评论
            digg_count = data['aweme_detail']['statistics']['digg_count']  # 点赞
            collect_count = data['aweme_detail']['statistics']['collect_count']  # 收藏
            share_count = data['aweme_detail']['statistics']['share_count']  # 转发
            create = data['aweme_detail']['create_time']  # 发布日期
            timeArray = time.localtime(create)
            create_time = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
            download_addr = data['aweme_detail']['video']['play_addr']['url_list'][0] #视频地址
            # print(preview_title,comment_count,digg_count,collect_count,share_count,create_time,download_addr)
            dict={'标题':[preview_title],'评论':[comment_count],'点赞':[digg_count],'收藏':[collect_count],'转发':[share_count],'发布日期':[create_time],'视频地址':[download_addr]}
            self.def_csv(text=dict)
    def def_csv(self,text=None):
        dataframe = pd.DataFrame(data=text)
        if not os.path.exists('./american_v.csv'):
            dataframe.to_csv('./american_v.csv', index=False, )
        dataframe.to_csv('./american_v.csv', mode='a', encoding='utf_8_sig', header=False, index=False)
        print('save_access')
        self.def_dsy()
    def def_dsy(self): #数据去重
        try:
            old = pandas.read_csv('./american_v.csv')
            new = old.drop_duplicates()
            new.to_csv('./american_v.csv', index=False,encoding='utf_8_sig',)
        except Exception as e:
            print(e)
