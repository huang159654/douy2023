#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# @当前时间 :2024/3/1 19:53
# @Author  : TS
# @Email   : TS@gmail.com
# @File    : ts2.py
# @Software: PyCharm
"""
import os
import re

import requests
from tqdm import tqdm

from 函数.抖音.抖音js.ALL_headers.headers_all import ALL_headers
from 函数.抖音.抖音js.ALL_sql.DY_Read import Read_sql


class Single_video():#单个视频

    def __init__(self):
        if not os.path.exists(r'C:\Users\Administrator\PycharmProjects\pythonProject\函数\抖音\抖音js/video'):
            os.mkdir(r'C:\Users\Administrator\PycharmProjects\pythonProject\函数\抖音\抖音js/video')
    def def_headers(self):
        headers=ALL_headers().def_headers()
        return headers
    def def_url(self):
        url ='https://www.douyin.com/aweme/v1/web/aweme/detail/?'
        return url
    def def_params(self,aweme_id=None):
        params=f'device_platform=webapp&aid=6383&channel=channel_pc_web&aweme_id={aweme_id}&pc_client_type=1&version_code=190500&version_name=19.5.0&cookie_enabled=true&screen_width=1920&screen_height=1080&browser_language=zh-CN&browser_platform=Win32&browser_name=Chrome&browser_version=122.0.0.0&browser_online=true&engine_name=Blink&engine_version=122.0.0.0&os_name=Windows&os_version=10&cpu_core_num=8&device_memory=8&platform=PC&downlink=10&effective_type=4g&round_trip_time=50&webid=7339779310952203811&msToken=SDTFnJbx9Nr2S0nPQ5iO0rffvj4-qT84ZgWpiaqm7tkF0xWukC05rdJj6dUvJGPLnOnFra1vXGEiTRY0SF9Zn_d9CV_dBNgUPQUEj6X4Wx3yLQhHM7ZDFeAP4Z0dTg=='
        return params

    def def_requests(self):
        for aweme_id in Read_sql().def_sql():
            # print(aweme_id)
            aweme_id_s = aweme_id['id']
            url_s = self.def_url() + self.def_params(aweme_id=aweme_id_s)
            response = requests.get(url=url_s,headers=self.def_headers()).json()
            if response['aweme_detail'] != None:
                dict = {'response': response}
                yield dict
            else:
                response['comments'] = None
                with open(r'C:\Users\Administrator\PycharmProjects\pythonProject\函数\抖音\抖音js\wrong_file/url错误链接.txt', mode='a', ) as f:
                    url = 'https://www.douyin.com/video/' + aweme_id_s
                    txt = url + '\n'  # 数据分行
                    f.write(txt)

    def def_Parse(self):
        for data in self.def_requests():
            desc=data['response']['aweme_detail']['desc']
            title = re.sub(r'[\/.*":?<>|\n]', '', desc)
            url_list = data['response']['aweme_detail']['video']['play_addr']['url_list'][0]
            # print('正在下载>>>>>>>>>>>>>>', title)
            video_content = requests.get(url=url_list,stream=True, headers=self.def_headers())#.content
            # with open(r'C:\Users\Administrator\PycharmProjects\pythonProject\函数\抖音\抖音js/video' + title + '.mp4', mode='wb') as f:
            #     # 写入数据
            #     f.write(video_content)
            video_content_s = requests.get(url=url_list)#\#获取请求头字典
            length=round(int(video_content_s.headers.get('Content-Length'))/1048576,2)#\#获取到视频的大小，单位是字节若想让他以MB为单位，则需除以两个1024
            with open(r'C:\Users\Administrator\PycharmProjects\pythonProject\函数\抖音\抖音js\video\\' + title + '.mp4',mode='wb') as f:
                for data_s in tqdm(
                        iterable=video_content.iter_content(1048576),
                        ncols=120,
                        total=length,
                        unit='mb',
                        file=None,
                        desc=title):
                    f.write(data_s)



if __name__=='__main__':
    Single_video().def_Parse()