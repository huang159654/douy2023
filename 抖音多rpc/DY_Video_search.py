#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# @当前时间 :2023/11/10 14:29
# @Author  : TS
# @Email   : TS@gmail.com
# @File    : ts2.py
# @Software: PyCharm
"""
import re
import json
import urllib
import requests


class Video(): #搜索视频最新发布
    def __init__(self):
        with open('info_pl.json', 'r', encoding='utf-8') as f:
            json_data = json.load(f)
            self.headers = json_data['Video_search']['headers']

    def def_xbogus(self, keyword):
        key_word = urllib.parse.quote(keyword)  # 转换网址中文编码格式
        url = f'device_platform=webapp&aid=6383&channel=channel_pc_web&search_channel=aweme_video_web&sort_type=2&publish_time=0&keyword={key_word}&search_source=tab_search&query_correct_type=1&is_filter_search=1&from_group_id=&offset=20&count=10&search_id=20231110141008F7C6F0C85AA29F84257D&pc_client_type=1&version_code=170400&version_name=17.4.0&cookie_enabled=true&screen_width=1280&screen_height=720&browser_language=zh-CN&browser_platform=Win32&browser_name=Chrome&browser_version=119.0.0.0&browser_online=true&engine_name=Blink&engine_version=119.0.0.0&os_name=Windows&os_version=10&cpu_core_num=8&device_memory=8&platform=PC&downlink=10&effective_type=4g&round_trip_time=50&webid=7287133158548440630&msToken=6qt1RxeREAL0_rv1pwXcvA5CCGwPjhxSPS53qjR6fH5aDGtSv4YLpodkia0wRwgIhoIKQ7hKPYmerctksRwFZYI_WDh6dPNNXYkmru9kl045fZZW1Ow='
        data = {
            "group": "test_web",
            "action": "test_xb",
            "url": url
        }
        res = requests.get("http://127.0.0.1:5612/business/invoke", params=data)
        d = res.json()
        x_b = 'https://www.douyin.com/aweme/v1/web/search/item/?' + url + '&X-Bogus=' + d['data']
        response = requests.get(url=x_b, headers=self.headers).json()
        return response

class D_reques():

    def def_request(self, keyword):
        da_ta = Video().def_xbogus(keyword)
        self.def_data(data=da_ta)

    def def_data(self, data=None):
        if data['data']:
            for da_ta in data['data']:
                desc = da_ta['aweme_info']['desc']
                print(desc)


# if __name__ == '__main__':
#     while 1:
#         keyword = input('请输入你要搜索的关键字:')
#         if re.match(r'[0-9]+$', keyword) or re.match(r'^[@_!#$%^&*()<>?/\|}{~:+,-;=.。、]$', keyword) or re.match(
#                 r'^[0-9]+\.[0-9]+$', keyword) or re.match(r'[0-9a-zA-Z\_]', keyword) or re.match(r'^\s*$', keyword):
#             print("你输入的是数字，请重新输入!")
#         else:
#             D_reques().def_request(keyword)
#             break
    # elif re.match(r'^[0-9]+\.[0-9]+$', keyword):
    #     print("你输入的是涂点数字，请重新输入!")
    # elif re.match(r'[0-9a-zA-Z\_]',keyword):
    #     print("你输入不正确，请重新输入!")
    # elif re.match(r'^[@_!#$%^&*()<>?/\|}{~:+,-;=.。、]$',keyword):
    #     print("你输入不正确，请重新输入!")
    # elif re.match(r'^\s*$',keyword):
    #     print("你输入不正确，请重新输入!")
