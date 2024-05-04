#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# @当前时间 :2023/11/13 23:05
# @Author  : TS
# @Email   : TS@gmail.com
# @File    : ts2.py
# @Software: PyCharm
"""
import json
import os
import pprint
import urllib.parse
import requests


class DY_videos(): #个人视频列表
    def __init__(self):
        with open('info_pl.json', 'r', encoding='utf-8')as f:
            json_data=json.load(f)
            self.headers=json_data['user_videos']['ALL_headers']

    def def_xbogus(self, sec_user_id,wef='max_cursor=''' ):
        #max_cursor 翻页
        url=f'device_platform=webapp&aid=6383&channel=channel_pc_web&sec_user_id={sec_user_id}&max_cursor=&locate_query=false&show_live_replay_strategy=1&need_time_list=0&time_list_query=0&whale_cut_token=&cut_version=1&count=18&publish_video_strategy_type=2&pc_client_type=1&version_code=170400&version_name=17.4.0&cookie_enabled=true&screen_width=1280&screen_height=720&browser_language=zh-CN&browser_platform=Win32&browser_name=Chrome&browser_version=119.0.0.0&browser_online=true&engine_name=Blink&engine_version=119.0.0.0&os_name=Windows&os_version=10&cpu_core_num=8&device_memory=8&platform=PC&downlink=10&effective_type=4g&round_trip_time=0&webid=7299807302318671401&msToken=HdSJPR5exk51OL11EbgcbZxjZHZm5SGLYQt5xaFG80ptAD7Gm0I2RC09_hZgQM7jTpbE8ttgu0_sE1F_N7j4Efp4bzF0TdePbRE3XbeJSHrOaWm5c_yhvhuXcVOe'
        # print(url)
        data = {
            "group": "test_web",
            "action": "test_xb",
            "url":url
        }
        res = requests.get("http://127.0.0.1:5612/business/invoke", params=data, )
        d = res.json()
        x_b = 'https://www.douyin.com/aweme/v1/web/aweme/post/?' + url + '&X-Bogus=' + d['data']
        response = requests.get(url=x_b, headers=self.headers).json()
        return response
class DY_parse():#解析
    def __init__(self):
        with open('info_pl.json', 'r', encoding='utf-8') as f:
            json_data = json.load(f)
            self.headers = json_data['user_videos']['ALL_headers']
    def def_data(self,sec_user_id):
        list_data=DY_videos().def_xbogus(sec_user_id)
        self.def_aweme_list(data=list_data)
    def def_aweme_list(self,data=None):
        list = []
        list_1 = []
        if data['aweme_list']:
            for aweme_list in data['aweme_list']:
                desc=aweme_list['desc']#标题
                url_list=aweme_list['video']['play_addr']['url_list'][0]
                list.append(desc)
                list_1.append(url_list)
            dict = {'视频标题': list, '视频url': list_1}
            print(dict)
            self.def_url(data=dict)
    def def_url(self,data=None,):
        if not os.path.exists('../video'):
            os.mkdir('../video')
        dict_vide = data['视频url']
        dict_titie = data['视频标题']
        for titie, video in zip(dict_titie, dict_vide):
            url_video = video
            url_titie = titie
            video_content = requests.get(url=url_video, headers=self.headers).content
            with open('video\\' + url_titie + '.mp4', mode='wb') as f:
                # 写入数据
                f.write(video_content)
            print('正在下载', url_titie)

if __name__=='__main__':
    sec_user_id='MS4wLjABAAAAjxQvkDxvEAbwZiHVHhteEMNtGHNVN_olrDvH-FNE8RE4t-X3OKlCzCPJrdWwTooy'
    DY_parse().def_data(sec_user_id)