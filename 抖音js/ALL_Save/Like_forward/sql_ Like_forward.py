#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# @当前时间 :2024/2/29 19:29
# @Author  : TS
# @Email   : TS@gmail.com
# @File    : ts2.py
# @Software: PyCharm
"""
import time
import urllib.parse

import pymysql
import requests

from 函数.抖音.抖音js.ALL_conversion.DY_xlsx_sql import Xlsx, Xlsx_video
from 函数.抖音.抖音js.ALL_headers.headers_all import ALL_headers
from 函数.抖音.抖音js.ALL_sql.Create_database import Create_data
from 函数.抖音.抖音js.ALL_sql.DY_Read import Read_sql


class Like_forward():
    def __init__(self):
        pass
    def def_url(self):
        url='https://www.douyin.com/aweme/v1/web/aweme/detail/?'
        return url
    def def_headers(self):
        headers=ALL_headers().def_headers()
        return headers
    def def_params(self,aweme_id=None):
        params = {
            'device_platform': 'webapp',
            'aid': '6383',
            'channel': 'channel_pc_web',
            'aweme_id': aweme_id,
            'pc_client_type': '1',
            'version_code': '190500',
            'version_name': '19.5.0',
            'cookie_enabled': 'true',
            'screen_width': '1920',
            'screen_height': '1080',
            'browser_language': 'zh-CN',
            'browser_platform': 'Win32',
            'browser_name': 'Chrome',
            'browser_version': '122.0.0.0',
            'browser_online': 'true',
            'engine_name': 'Blink',
            'engine_version': '122.0.0.0',
            'os_name': 'Windows',
            'os_version': '10',
            'cpu_core_num': '8',
            'device_memory': '8',
            'platform': 'PC',
            'downlink': '10',
            'effective_type': '4g',
            'round_trip_time': '50',
            'webid': '7339779310952203811',
            'msToken': 'ujicZ5n3Ir6UPEigDDMiU15wQ8-zWtWKz3K6jb5Di6LrCgQPBwgijAJAZ__8U0tq0TIZvwHfuZEikiEFuMNivXct3kvwUdsREsGpbAUe1Fx3kNzvWEgIhYuUZsoj',
        }
        params_string = urllib.parse.urlencode(params)
        return params_string
    def def_requests(self):
        for url_dict in Read_sql().def_sql():  # 从数据库提取url的id
            aweme_id = url_dict['id']
            urls = self.def_url() + self.def_params(aweme_id=aweme_id)
            response = requests.get(url=urls, headers=self.def_headers()).json()
            if response['aweme_detail'] != None:
                dict = {'response': response}
                yield dict
            else:
                response['aweme_detail'] = None
                with open(r'C:\Users\Administrator\PycharmProjects\pythonProject\函数\抖音\抖音js\wrong_file\url错误链接.txt', mode='a', ) as f:
                    url = 'https://www.douyin.com/video/' + aweme_id
                    txt = url + '\n'  # 数据分行
                    f.write(txt)
    def def_parse(self):
        for data_s in self.def_requests():
            data=data_s['response']
            preview_title = data['aweme_detail']['preview_title']  # 标题
            comment_count = data['aweme_detail']['statistics']['comment_count']  # 评论
            digg_count = data['aweme_detail']['statistics']['digg_count']  # 点赞
            collect_count = data['aweme_detail']['statistics']['collect_count']  # 收藏
            share_count = data['aweme_detail']['statistics']['share_count']  # 转发
            create = data['aweme_detail']['create_time']  # 发布日期
            timeArray = time.localtime(create)
            create_time = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
            author = data['aweme_detail']['author']['nickname']  # 昵称
            aweme_id = data['aweme_detail']['statistics']['aweme_id']
            awem_id = 'https://www.douyin.com/video/' + aweme_id
            dict = {'author': author, '推⼴链接': awem_id, '发布日期': create_time, '帖⼦名称': preview_title,
                    '点赞': digg_count, '评论': comment_count, '收藏': collect_count,
                    '转发': share_count, 'id':aweme_id}
            # print(dict)
            yield dict
    def sql_s(self,):  # 数据库保存
        db = pymysql.connect(host='localhost', user='root', password='huang159', port=3306, db='dy_creat')
        mycursor = db.cursor()
        sql_s = "insert into conten (author,awem_id,create_time,preview_title,digg_count,comment_count,collect_count,share_count,aweme_id) VALUES (%s, %s, %s,%s, %s, %s,%s, %s, %s);"
        for data in self.def_parse():
            #数据去重
            sql = "select * from conten where aweme_id={}".format(data["id"])
            mycursor.execute(sql)
            ret = mycursor.fetchone()
            if ret:
                print('Data duplication!') #数据重复
            else:#没有数据则插入
                values = (data["推⼴链接"], data["author"], data["发布日期"], data["帖⼦名称"], data["点赞"], data["评论"],
                data["收藏"], data["转发"],data["id"])
                # print(values)
                mycursor.execute(sql_s, values)
                db.commit()
                print(f'+++++++++++++++++++{data["id"]}保存到数据库+++++++++++++++++++')
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
                Create_data().def_Conten()
                Xlsx().def_sql_url()
                Like_forward().sql_s()
            elif menum.upper() == 'B':
                Create_data().def_Conten()
                Xlsx_video().def_sql_url()
                Like_forward().sql_s()
            elif menum.upper() == 'Q':
                print("""==================结束程序=================""")
                break
if __name__=='__main__':
    Like_forward().def_main()