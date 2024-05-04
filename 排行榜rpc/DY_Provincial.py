#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# @当前时间 :2024/1/6 16:56
# @Author  : TS
# @Email   : TS@gmail.com
# @File    : ts2.py
# @Software: PyCharm
"""
from DY_backup import DY_Provincial
from DY_backup import D_Popularity

class DY_Provincia():
    def __init__(self):
        pass

    def def_Parse(self,anchor_id=None,room_id=None):
        for data in DY_Provincial().def_response(anchor_id=anchor_id,room_id=room_id):
            parse_ranks=data.get('data').get('ranks')
            for user in parse_ranks:
                id = user.get('index')
                nickname=user.get('user').get('nickname')#昵称
                display_id = user.get('user').get('display_id')#直播间id
                id_link='https://live.douyin.com/'+display_id#链接
                sec_uid = user.get('user').get('sec_uid')  # 详情页 id
                Details_page='https://www.douyin.com/user/'+sec_uid #详情页链接
                print(id, nickname,id_link,Details_page)

class DY_Popularity():#人气排行榜
    def __init__(self):
        pass
    def def_Parse(self):
        for data in D_Popularity().def_response():
            parse_ranks=data.get('data').get('ranks')
            for user in parse_ranks:
                id = user.get('rank')
                nickname=user.get('user').get('nickname')#昵称
                display_id = user.get('user').get('display_id')#直播间id
                id_link='https://live.douyin.com/'+display_id#链接
                sec_uid = user.get('user').get('sec_uid')  # 详情页 id
                Details_page='https://www.douyin.com/user/'+sec_uid #详情页链接
                print(id, nickname,id_link,Details_page)
#
# if __name__=='__main__':
    # DY_Popularity().def_Parse()
#     anchor_id = 51987175819
#     room_id = 7320953812972210981
#     DY_Provincia().def_Parse(anchor_id=anchor_id,room_id=room_id)

