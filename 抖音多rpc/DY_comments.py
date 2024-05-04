#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# @当前时间 :2023/11/6 22:11
# @Author  : TS
# @Email   : TS@gmail.com
# @File    : ts2.py
# @Software: PyCharm
"""
import datetime
import json
import os
import time
import math
import timeit
import pandas
import requests
import  pandas as pd

class D_pl(): #评论
    def __init__(self,):
        self.dict={}
        self.dict_1=[]
        self.dict_2=[]
        self.dict_3 = []
        self.dict_4 = []
        self.dict_5 = []
        self.dict_6 = []
        with open('info_pl.json', 'r', encoding='utf-8') as f:
            json_data = json.load(f)
            self.url = json_data['pl']['url']
            self.headers = json_data['pl']['headers']
            self.queries = json_data['pl']["queries"]
    def def_pagination(self,awem_id):
        self.aweme_id = awem_id
        url = f'device_platform=webapp&aid=6383&channel=channel_pc_web&aweme_id={self.aweme_id}&cursor=0&count=20&item_type=0&whale_cut_token=&cut_version=1&rcFT=&pc_client_type=1&version_code=170400&version_name=17.4.0&cookie_enabled=true&screen_width=1280&screen_height=720&browser_language=zh-CN&browser_platform=Win32&browser_name=Chrome&browser_version=119.0.0.0&browser_online=true&engine_name=Blink&engine_version=119.0.0.0&os_name=Windows&os_version=10&cpu_core_num=8&device_memory=8&platform=PC&downlink=10&effective_type=4g&round_trip_time=100&webid=7287133158548440630&msToken=FegqJMAlY4vEABum5EBpEKM97UDHaw3XpkpEgTH4uodE3QtKOfdjWkUkUvjRMrMqrXz4HEDFCBgTG7f7pV5kLgD_BlL3ZBcMKt-mqouPIgrH72fhdHA='
        data = {
            "group": "test_web",
            "action": "test_xb",
            "url": url
        }
        res = requests.get("http://127.0.0.1:5612/business/invoke", params=data)
        d = res.json()
        x_b = 'https://www.douyin.com/aweme/v1/web/comment/list/?' + url + '&X-Bogus=' + d['data']
        response = requests.get(url=x_b, headers=self.headers).json()
        self.def_total(data=response)
    def def_total(self,data=None):
        total=data['total']
        dai=total/20
        self.tota_l=math.ceil(dai)
        self.def_xbogus()
    def def_xbogus(self,):
        for coun in range(self.tota_l):
            cursor = coun * 20
            # print(f'正在采集{cursor}页评论')
            url = f'device_platform=webapp&aid=6383&channel=channel_pc_web&aweme_id={self.aweme_id}&cursor={cursor}&count=20&item_type=0&whale_cut_token=&cut_version=1&rcFT=&pc_client_type=1&version_code=170400&version_name=17.4.0&cookie_enabled=true&screen_width=1280&screen_height=720&browser_language=zh-CN&browser_platform=Win32&browser_name=Chrome&browser_version=119.0.0.0&browser_online=true&engine_name=Blink&engine_version=119.0.0.0&os_name=Windows&os_version=10&cpu_core_num=8&device_memory=8&platform=PC&downlink=10&effective_type=4g&round_trip_time=100&webid=7287133158548440630&msToken=FegqJMAlY4vEABum5EBpEKM97UDHaw3XpkpEgTH4uodE3QtKOfdjWkUkUvjRMrMqrXz4HEDFCBgTG7f7pV5kLgD_BlL3ZBcMKt-mqouPIgrH72fhdHA='
            data = {
                "group": "test_web",
                "action": "test_xb",
                "url": url
            }
            res = requests.get("http://127.0.0.1:5612/business/invoke", params=data)
            d = res.json()
            # x_b = 'https://www.douyin.com/aweme/v1/web/comment/list/?' + url + '&X-Bogus=' + d['data']
            # return x_b
            self.x_b = 'https://www.douyin.com/aweme/v1/web/comment/list/?' + url + '&X-Bogus=' + d['data']
            self.get_requests()
        # self.def_dsy() #调用去重函数
    def get_requests(self): #请求数据
        # x_b=D_pl().def_pagination()
        # print(x_b)
        self.response_s= requests.get(url=self.x_b, headers=self.headers).json()
        self.def_parse()
    def def_parse(self):#解析数据
        if self.response_s['comments']:
            for compile in self.response_s['comments']:
                create = compile['create_time']  # 发布时间
                timeArray = time.localtime(create)
                create_time = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
                nickname = compile['user']['nickname']  # 用户昵称
                ip_label = compile['ip_label']  # 用户ip
                text = compile['text']  # 评论内容
                sec_uid = compile['user']['sec_uid']  # 用户详情页
                # short_id = compile['user']['short_id']  # 抖音号
                # print(text, ip_label, nickname, sec_uid, short_id, create_time)
                self.dict_1.append(create_time)
                self.dict_2.append(nickname)
                self.dict_3.append(ip_label)
                self.dict_4.append(text)
                self.dict_5.append(sec_uid)
                # self.dict_6.append(short_id)
            #创建字典，数据保存到字典
            dict = {'发布时间': self.dict_1,
                    '用户昵称': self.dict_2,
                    '用户ip': self.dict_3,
                    '评论内容': self.dict_4,
                    '用户详情页': self.dict_5,
                    # '抖音号': self.dict_6
                    }
            self.def_csv(data=dict)
    def def_csv(self,data=None):#保存数据
        dataframe = pd.DataFrame(data=data)
        if not os.path.exists('101190400.csv'):
            dataframe.to_csv('./101190400.csv', index=False, )
        dataframe.to_csv('./101190400.csv',  encoding='utf_8_sig', header=True, index=False)
        current_time = datetime.datetime.now()
        print("现在时间是: " + str(current_time),'save_access')

    # def def_dsy(self): #数据去重
    #     try:
    #         old = pandas.read_csv('./101190400.csv')
    #         new = old.drop_duplicates()
    #         new.to_csv('./101190400.csv', index=False,encoding='utf_8_sig',)
    #     except Exception as e:
    #         print(e)
