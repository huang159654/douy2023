#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# @当前时间 :2024/2/27 16:10
# @Author  : TS
# @Email   : TS@gmail.com
# @File    : ts2.py
# @Software: PyCharm
"""
import os
import re

import requests
from 函数.抖音.抖音js.ALL_headers.headers_all import ALL_headers


class A_single_video():
    def __init__(self):
        if not os.path.exists('./video'):
            os.mkdir('./video')
    def def_headers(self):
        headers=ALL_headers().def_headers()
        return headers
    def def_url(self):
        url='https://www.douyin.com/aweme/v1/web/aweme/detail/?'
        return url
    def def_params(self):
        params=f'device_platform=webapp&aid=6383&channel=channel_pc_web&aweme_id=7307480006525996338&pc_client_type=1&version_code=190500&version_name=19.5.0&cookie_enabled=true&screen_width=1920&screen_height=1080&browser_language=zh-CN&browser_platform=Win32&browser_name=Chrome&browser_version=122.0.0.0&browser_online=true&engine_name=Blink&engine_version=122.0.0.0&os_name=Windows&os_version=10&cpu_core_num=8&device_memory=8&platform=PC&downlink=10&effective_type=4g&round_trip_time=50&webid=7339779310952203811&msToken=SDTFnJbx9Nr2S0nPQ5iO0rffvj4-qT84ZgWpiaqm7tkF0xWukC05rdJj6dUvJGPLnOnFra1vXGEiTRY0SF9Zn_d9CV_dBNgUPQUEj6X4Wx3yLQhHM7ZDFeAP4Z0dTg=='
        return params
    def def_requests(self):
        url_s=self.def_url()+self.def_params()
        response = requests.get(url=url_s,
           headers=self.def_headers()).json()
        dict={'response':response}
        yield dict
    def def_Parse(self):
        for data in self.def_requests():
            desc=data['response']['aweme_detail']['desc']
            title = re.sub(r'[\/.*":?<>|\n]', '', desc)
            url_list = data['response']['aweme_detail']['video']['play_addr']['url_list'][0]
            print('正在下载>>>>>>>>>>>>>>', title)
            video_content = requests.get(url=url_list, headers=self.def_headers()).content
            with open('video\\' + title + '.mp4', mode='wb') as f:
                # 写入数据
                f.write(video_content)
if __name__=='__main__':
    A_single_video().def_Parse()