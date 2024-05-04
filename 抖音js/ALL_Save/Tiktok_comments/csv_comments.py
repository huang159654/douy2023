#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# @当前时间 :2024/2/29 13:27
# @Author  : TS
# @Email   : TS@gmail.com
# @File    : ts2.py
# @Software: PyCharm
"""
import os
import random
import time

import pandas as pd
import pymysql
import requests

from 函数.抖音.抖音js.ALL_conversion.DY_Read import Read_csv
from 函数.抖音.抖音js.ALL_conversion.DY_xlsx_csv import Xlsx, Xlsx_video

from 函数.抖音.抖音js.ALL_headers.headers_all import ALL_headers
from 函数.抖音.抖音js.ALL_js.XB_js import XB_js
from 函数.抖音.抖音js.ALL_sql.Create_database import Create_data

class CSV_comments(): #评论
    def __init__(self):
        pass
    def def_headers(self):
        headers=ALL_headers().def_headers()
        return headers
    def def_url(self):
        url = "https://www.douyin.com/aweme/v1/web/comment/list/?"
        return url
    def def_params(self, awemes_id=None, cursor=None):
        params = f'device_platform=webapp&aid=6383&channel=channel_pc_web&aweme_id={awemes_id}&cursor={cursor}&count=20&item_type=0&whale_cut_token=&cut_version=1&rcFT=&pc_client_type=1&version_code=170400&version_name=17.4.0&cookie_enabled=true&screen_width=1920&screen_height=1080&browser_language=zh-CN&browser_platform=Win32&browser_name=Chrome&browser_version=121.0.0.0&browser_online=true&engine_name=Blink&engine_version=121.0.0.0&os_name=Windows&os_version=10&cpu_core_num=8&device_memory=8&platform=PC&downlink=10&effective_type=4g&round_trip_time=50&webid=7317023263425775145&msToken=Y5ky0EBdSM1YZp3j_FDy6Kj-n3ax6dWWhVLvV9m008gWBhQKjBiKCNFKCaqmjKFW9dLqT92HiD56pJNsNm7TU-PqDMlxCe-y2k5VrcGxvlCndLCeFTiD-Lflzb4COg=='
        return params
    def def_xb_s(self):
        for url_dict in Read_csv().def_csv():#从数据库提取url的id
            aweme_id=url_dict['id']
            params=self.def_params(awemes_id=aweme_id)
            xb_data=XB_js().def_xb(params=params)
            urls = self.def_url() + self.def_params(awemes_id=aweme_id) + "&X-Bogus=" + xb_data
            response = requests.get(url=urls, headers=self.def_headers()).json()
            if response['comments'] != None:
                total = response['total']
                dict = {'awemes_id': aweme_id, 'tota_l': total}
                # print(dict)
                yield dict
            else:
                response['comments'] = None
                with open(r'C:\Users\Administrator\PycharmProjects\pythonProject\函数\抖音\抖音js\wrong_file/url错误链接.txt', mode='a', ) as f:
                    url = 'https://www.douyin.com/video/' + aweme_id
                    txt = url + '\n'  # 数据分行
                    f.write(txt)
    def def_requests(self, ):
        for cursor_sa in self.def_xb_s():
            awemes_id=cursor_sa['awemes_id']
            for cursor in range(0, cursor_sa['tota_l'],20):
                data = self.def_params(awemes_id=awemes_id, cursor=cursor)
                xb_data = XB_js().def_xb(params=data)
                urls = self.def_url() + self.def_params(awemes_id=awemes_id, cursor=cursor) + "&X-Bogus=" + xb_data
                response = requests.get(url=urls, headers=self.def_headers()).json()
                # print(response['comments'])
                randoms = random.randint(3, 10) #等待时间
                time.sleep(randoms)
                if response['comments'] is None:
                    print("字典中'comments'对应的值为None")
                    break
                else:
                    yield response

    def def_parse(self, ):  # 解析数据
        for data_list in self.def_requests():
            print('---------------------------------------------------------------------------------------------------------------')
            try:
                for data in data_list['comments']:
                    nickname = data.get('user').get('nickname')  # 用户昵称
                    sec_uid = data.get('user').get('sec_uid')  # 用户详情页id
                    short_id = data.get('user').get('short_id')  # 用户抖音号
                    text_s = data.get('text')  # 评论文本
                    create = data.get('create_time')  # 发布时间
                    timeArray = time.localtime(create)
                    create_time = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)  # 发布时间
                    ip_label = data.get('ip_label')  # ip地址
                    reply_comment_total = data.get('reply_comment_total')  # 回复数
                    cid = data.get('cid')  # 主键id
                    aweme_id = data.get('aweme_id')  # 视频id
                    aweme_url = 'https://www.douyin.com/video/' + aweme_id  # 视频链接
                    dict = [{'视频id': aweme_id, 'cid': cid, '用户昵称': nickname, '用户详情页id': sec_uid,
                             '用户抖音号': short_id,
                             '评论文本': text_s, '发布时间': create_time, '用户ip地址': ip_label,
                             '用户评论回复数': reply_comment_total,
                             '视频链接': aweme_url}]

                    yield dict
            except :
                 continue

    def def_csv(self):#保存csv
        for data in self.def_parse():
            dataframe = pd.DataFrame(data)
            if not os.path.exists(r'C:\Users\Administrator\PycharmProjects\pythonProject\函数\抖音\抖音js\ALL_csv\抖音评论.csv'):
                dataframe.to_csv(r'C:\Users\Administrator\PycharmProjects\pythonProject\函数\抖音\抖音js\ALL_csv\抖音评论.csv', mode='a',encoding='utf_8_sig',index=False, )
            dataframe.to_csv(r'C:\Users\Administrator\PycharmProjects\pythonProject\函数\抖音\抖音js\ALL_csv\抖音评论.csv', mode='a',encoding='utf_8_sig', header=False, index=False)
            # current_time = datetime.datetime.now()
            print('Comment collection completed')#评论采集完毕
            df = pd.read_csv(r'C:\Users\Administrator\PycharmProjects\pythonProject\函数\抖音\抖音js\ALL_csv\抖音评论.csv')
            # 删除重复项
            df = df.drop_duplicates()
            # 保存修改后的DataFrame对象到新的CSV文件
            df.to_csv(r'C:\Users\Administrator\PycharmProjects\pythonProject\函数\抖音\抖音js\ALL_csv\抖音评论.csv', index=False)
    #
    #
    def def_main(self):
        menum = """
                        ===================================抖音评论采集=========================================
                        A。# 读取xlsx 文件中https://v.douyin.com/iKeD74w/链接
                        ----------------------------------------------------
                        B。读取xlsx 文件中https://www.douyin.com/video/7312743380214238498链接
                        ----------------------------------------------------
                        Q。结束选择文件操作
                       =====================================================================================
                                """
        print(menum)
        while 1:
            menum = input('请选择你要保存的文件>>>>>>')
            if menum.upper() == 'A':
                Xlsx().def_csv()
                CSV_comments().def_csv()
            elif menum.upper() == 'B':
                Xlsx_video().def_csv()
                CSV_comments().def_csv()
            elif menum.upper() == 'Q':
                print("""==================结束程序=================""")
                break

if __name__=='__main__':
    CSV_comments().def_main()