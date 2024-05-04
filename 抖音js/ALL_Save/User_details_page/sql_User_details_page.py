#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# @当前时间 :2024/3/3 11:02
# @Author  : TS
# @Email   : TS@gmail.com
# @File    : ts2.py
# @Software: PyCharm
"""
import re
import urllib.parse

import execjs
import requests

from 函数.抖音.抖音js.ALL_headers.headers_all import ALL_headers


class User_details_page(): #需要重写链接在def_requests修改
    def __init__(self):
        pass

    def def_headers(self):
        headers = ALL_headers().def_headers()
        return headers
    def def_url(self,uid_id=None):
        url =f"https://www.douyin.com/user/{uid_id}"
        return url
    def def_requests(self):
        uid_id='MS4wLjABAAAATCWOmnbr_1_DPt12CbM_RbqNujlotxACqiSHoOYJgkk'
        response = requests.get(url=self.def_url(uid_id=uid_id),headers=self.def_headers(),
        ).text
        return response
    def def_parse(self):
        da = re.sub(r'\s+', '',self.def_requests())
        followingCount = re.findall(r'\"followingCount\\\"\:(.*?)\,', da)[1]  # 关注
        mplatformFollowersCount = re.findall(r'\\\"mplatformFollowersCount\\\"\:(.*?)\,', da)[1]  # 粉丝
        totalFavorited = re.findall(r'\\\"totalFavorited\\\"\:(.*?)\,', da)[1]  # 点赞
        uniqueId = re.findall(r'\\\"uniqueId\\\"\:\\\"(.*?)\\\"\,', da)[1]  # 抖音号
        nickname = re.findall(r'\\\"nickname\\\"\:\\\"(.*?)\\\"', da)[1]  # 昵称
        desc = re.findall(r'\,\\\"desc\\\"\:\\\"(.*?)\\\"\,', da)[1].replace(r'\\n', '')  # 简介
        ipLocation = re.findall(r'\\\"ipLocation\\\"\:\\\"IP属地\：(.*?)\\\"\,', da)[0]  # IP属地
        uid = re.findall(r'\\\"uid\\\"\:\\\"(.*?)\\\"\,', da)[1]  # uid
        print(followingCount, mplatformFollowersCount, totalFavorited, uniqueId, nickname, desc, ipLocation, uid)

if __name__=='__main__':
    User_details_page().def_parse()