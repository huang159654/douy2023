#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# @当前时间 :2023/11/11 0:04
# @Author  : TS
# @Email   : TS@gmail.com
# @File    : ts2.py
# @Software: PyCharm
"""
import json
import os
import pprint
import re
import urllib

import requests


class D_Thumbs():#搜索视频点赞
    def __init__(self):

        with open('info_pl.json', 'r', encoding='utf-8')as f:
            json_data=json.load(f)
            self.cookies=json_data['Thumbs']['cookies']
            self.headers = json_data['Thumbs']['ALL_headers']
    def def_xbogus(self,keyword):
        key_word = urllib.parse.quote(keyword)  # 转换网址中文编码格式
        url = f'https://www.douyin.com/aweme/v1/web/search/item/?device_platform=webapp&aid=6383&channel=channel_pc_web&search_channel=aweme_video_web&sort_type=1&publish_time=0&keyword={key_word}&search_source=tab_search&query_correct_type=1&is_filter_search=1&from_group_id=&offset=0&count=10&pc_client_type=1&version_code=170400&version_name=17.4.0&cookie_enabled=true&screen_width=1280&screen_height=720&browser_language=zh-CN&browser_platform=Win32&browser_name=Chrome&browser_version=119.0.0.0&browser_online=true&engine_name=Blink&engine_version=119.0.0.0&os_name=Windows&os_version=10&cpu_core_num=8&device_memory=8&platform=PC&downlink=10&effective_type=4g&round_trip_time=50&webid=7299807302318671401&msToken=tfeHErmk3UFzdVgTVA7ceaPjCgR_AGESOcOm-3QQ_jFcBWXuIQns7u3dy7GfA_3sqsSsA7DDSHG8heW-1dp_c2Q46-9iYUimVihC7o3QWIFmpo9jUsXRWTmwPLY9'
        data = {
            "group": "test_web",
            "action": "test_xb",
            "url": url
        }
        res = requests.get("http://127.0.0.1:5612/business/invoke", params=data)
        d = res.json()
        x_b = 'https://www.douyin.com/aweme/v1/web/search/item/?' + url + '&X-Bogus=' + d['data']
        response = requests.get(url=x_b, headers=self.headers,cookies=self.cookies).json()
        return response

class D_requess():
    def __init__(self):
        with open('info_pl.json', 'r', encoding='utf-8') as f:
            json_data = json.load(f)
            self.headers = json_data['Video_search']['ALL_headers']
    def def_request(self, keyword):
        da_ta = D_Thumbs().def_xbogus(keyword)
        self.def_data(data=da_ta)
    def def_data(self, data=None):
        list = []
        list_1 = []
        if data['data']:
            for da_ta in data['data']:
                desc_q = da_ta['aweme_info']['desc']
                desc = re.sub(r'[\/.*":?<>|\n]', '', desc_q)
                play_addr=da_ta['aweme_info']['video']['play_addr']['url_list'][0]
                list.append(desc)
                list_1.append(play_addr)
            dict= {'视频标题': list, '视频url':list_1}
            self.def_video(data=dict)
    def def_video(self,data=None):
        if not os.path.exists('../video'):
            os.mkdir('../video')
        dict_vide=data['视频url']
        dict_titie=data['视频标题']
        for titie,video in zip(dict_titie,dict_vide):
            url_video=video
            url_titie=titie
            video_content = requests.get(url=url_video, headers=self.headers).content
            with open('video\\' + url_titie + '.mp4', mode='wb') as f:
                # 写入数据
                f.write(video_content)
            print('正在下载',url_titie)



