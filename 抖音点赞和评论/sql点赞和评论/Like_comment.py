#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# @当前时间 :2024/2/26 18:03
# @Author  : TS
# @Email   : TS@gmail.com
# @File    : ts2.py
# @Software: PyCharm
"""
import json
import time
import execjs
import pymysql
import requests
import urllib.parse
from 函数.抖音.抖音js.ALL_conversion.DY_xlsx_sql import Xlsx
from 函数.抖音.抖音js.ALL_conversion.DY_xlsx_sql import Xlsx_video
from DY_Read import Read_sql
from Create_database import Create_data

class Like_comment():
    def __init__(self):
        pass

    def def_headers(self):
        with open('package.json', mode='r', encoding='utf-8') as f:
            data_json = json.load(f)
            headers = data_json['ALL_headers']
            return headers
    def def_execjs(self):
        with open("x_b.js") as f:
            js_data = f.read()
        js_compile =execjs.compile(js_data)
        return js_compile

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
    def def_url(self):
        url='https://www.douyin.com/aweme/v1/web/aweme/detail/?'
        return url
    def def_url_id(self):
        for data in Read_sql().def_sql():
            awemes_id = data['id']
            dict={'awemes_id':awemes_id}
            yield dict
    def def_xb(self):
        xb_data = self.def_execjs().call("get_dy_xb", self.def_params())
        return xb_data
    def def_url_s(self):
        for data in self.def_url_id():
            aweme_id=data['awemes_id']
            params=self.def_params(aweme_id=aweme_id)
            url=self.def_url()+params#+'&X-Bogus=' + self.def_xb()
            dict={'url':url,'aweme_id':aweme_id}
            yield dict
        # return url
    def def_requests(self):
        for data_url in self.def_url_s():
            url=data_url['url']
            response = requests.get(url=url, headers=self.def_headers()).json()
            if response['aweme_detail'] != None:
                dict ={'response':response}
                # print(self.def_headers())
                yield dict
            else:
                response['aweme_detail'] = None
                with open('评论url错误链接.txt', mode='a', ) as f:
                    url = 'https://www.douyin.com/video/' + data_url['aweme_id']
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
            author = data['aweme_detail']['music']['author']  # 昵称
            aweme_id = data['aweme_detail']['statistics']['aweme_id']
            awem_id = 'https://www.douyin.com/video/' + aweme_id
            dict = {'author': author, '推⼴链接': awem_id, '发布日期': create_time, '帖⼦名称': preview_title,
                    '点赞': digg_count, '评论': comment_count, '收藏': collect_count,
                    '转发': share_count, 'id':aweme_id}
            # list.append([author,awem_id,create_time,preview_title,digg_count,comment_count,collect_count,share_count])
            yield dict
    def sql_s(self,):  # 数据库保存
        db = pymysql.connect(host='localhost', user='root', password='huang159', port=3306, db='dy_creat')
        mycursor = db.cursor()
        sql_s = "insert into conten (author,awem_id,create_time,preview_title,digg_count,comment_count,collect_count,share_count,aweme_id) VALUES (%s, %s, %s,%s, %s, %s,%s, %s, %s);"
        for data in self.def_parse():
            #数据去重
            sql = "select * from Conten where aweme_id={}".format(data["id"])
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
                                ===================================抖音点赞和评论采集=========================================
                                A。# 读取xlsx 文件中https://v.douyin.com/iKeD74w/链接
                                ----------------------------------------------------
                                B。读取xlsx 文件中https://www.douyin.com/video/7312743380214238498链接
                                ----------------------------------------------------
                                Q。退出程序
                               =====================================================================================
                                        """
        print(menum)
        while 1:
            menum = input('请选择你要保存的文件(Q。退出程序)>>>>>>')
            if menum.upper() == 'A':
                Create_data().def_data()
                Create_data().def_Conten()
                Xlsx().def_sql_url()
                Like_comment().sql_s()
            elif menum.upper() == 'B':
                Create_data().def_data()
                Create_data().def_Conten()
                Xlsx_video().def_sql_url()
                Like_comment().sql_s()
            elif menum.upper() == 'Q':
                print("""==================结束程序=================""")
                break


if __name__=='__main__':
    Like_comment().def_main()
    # Like_comment().sql_s()