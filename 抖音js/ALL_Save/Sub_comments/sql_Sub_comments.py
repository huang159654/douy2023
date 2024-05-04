#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# @当前时间 :2024/3/1 14:19
# @Author  : TS
# @Email   : TS@gmail.com
# @File    : ts2.py
# @Software: PyCharm
"""
import random
import time

import pymysql
import requests

from 函数.抖音.抖音js.ALL_headers.headers_all import ALL_headers
from 函数.抖音.抖音js.ALL_sql.Read_sql_comments import Read_sql_comments
from 函数.抖音.抖音js.ALL_sql.Create_database import Create_data


class Sub_comments():
    def __init__(self):
        pass
    def def_headers(self):
        headers = ALL_headers().def_headers()
        return headers

    def def_url(self):
        url = 'https://www.douyin.com/aweme/v1/web/comment/list/reply/?'
        return url
    def def_params(self,item_id=None,comment_id=None,cursor=None):
        def_params=f'device_platform=webapp&aid=6383&channel=channel_pc_web&item_id={item_id}&comment_id={comment_id}&cut_version=1&cursor={cursor}&count=10&item_type=0&pc_client_type=1&version_code=170400&version_name=17.4.0&cookie_enabled=true&screen_width=1920&screen_height=1080&browser_language=zh-CN&browser_platform=Win32&browser_name=Chrome&browser_version=122.0.0.0&browser_online=true&engine_name=Blink&engine_version=122.0.0.0&os_name=Windows&os_version=10&cpu_core_num=8&device_memory=8&platform=PC&downlink=10&effective_type=4g&round_trip_time=50&webid=7339779310952203811&msToken=cCBQfR1G85BfwNKpMswYFSqiLimO2257nGIXH2V0-1XKb2sZnaT_Lod2gAyC2J4expULnXC9cHAxL3KsImdX7t9MBNjcAjpPW_zX2wQQ2oLwMyIr8mE='
        return def_params

    def def_X_Bogus(self,):
        for data in Read_sql_comments().def_sql():
            item_id=data['id']
            comment_id = data['url_list_id']
            url_list_text=data['url_list_text']
            params = self.def_params(item_id=item_id,comment_id=comment_id)
            urls = self.def_url() + params #+ "&X-Bogus=" + xb_data
            response = requests.get(url=urls, headers=self.def_headers()).json()
            if response['comments'] != None:
                total = response['total']
                dict = {'awemes_id': item_id, 'tota_l': total,'comment_id':comment_id,'url_list_text':url_list_text}
                # print(dict)
                yield dict
            else:
                response['comments'] = None
                with open(
                        r'C:\Users\Administrator\PycharmProjects\pythonProject\函数\抖音\抖音js\wrong_file/url错误链接.txt',
                        mode='a', ) as f:
                    url = 'https://www.douyin.com/video/' + item_id +'评论id'+ comment_id
                    txt = url + '\n'  # 数据分行
                    f.write(txt)
    def def_requests(self, ):
        for cursor_sa in self.def_X_Bogus():
            item_id=cursor_sa['awemes_id']
            comment_id=cursor_sa['comment_id']
            url_list_text=cursor_sa['url_list_text']
            for cursor in range(0, cursor_sa['tota_l'],10):
                urls = self.def_url() + self.def_params(item_id=item_id,comment_id=comment_id,cursor=cursor)
                response = requests.get(url=urls, headers=self.def_headers()).json()
                randoms = random.randint(3, 10) #等待时间
                time.sleep(randoms)
                if response['comments'] is None:
                    print("字典中'comments'对应的值为None")
                    break
                else:
                    dict={'url_list_text':url_list_text,'response':response}
                    yield dict

    def def_parse(self):  # 解析数据
        for data_s in self.def_requests():
            data=data_s['response']
            text_s = data_s['url_list_text']
            if data['comments']:
                try:
                    for compile in data['comments']:
                        create = compile.get('create_time')  # 发布时间
                        timeArray = time.localtime(create)
                        create_time = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
                        nickname = compile.get('user').get('nickname')  # 用户昵称
                        text = compile.get('text')  # 评论内容
                        ip_label = compile.get('ip_label')  # ip地址
                        digg_count = compile.get('digg_count')  # 点赞数
                        reply_id = compile.get('reply_id')  # 关联id
                        aweme_id = compile.get('aweme_id')
                        awem_id = 'https://www.douyin.com/video/' + aweme_id
                        dict = [{'id': reply_id, '推广连接': awem_id, "主评论": text_s, '次评论': text,
                                 '点赞数': digg_count, 'ip地址': ip_label, '发布时间': create_time,
                                 '用户昵称': nickname, }]
                        # print(dict)
                        yield dict
                except Exception as e:
                    e
    def sql_s(self):
        db = pymysql.connect(host='localhost', user='root', password='huang159', port=3306, db='dy_creat')
        mycursor = db.cursor()
        sql = "insert into reviews (awem_id,cid,text_s,TEXT,digg_count,ip_label,create_time,nickname) VALUES (%s, %s, %s,%s, %s, %s,%s, %s);"
        for data in self.def_parse():
            values = (data[0]["推广连接"], data[0]["id"], data[0]["主评论"], data[0]["次评论"], data[0]["点赞数"],
                      data[0]["ip地址"], data[0]["发布时间"], data[0]["用户昵称"])
            mycursor.execute(sql, values)
            db.commit()
            print(f'+++++++++++++++++++{data[0]["id"]}保存到数据库+++++++++++++++++++')
    def def_main(self): #在sql中评论名称comments基础上运行的
        Create_data().def_Reviews()
        Sub_comments().sql_s()
if __name__=='__main__':
    Sub_comments().def_main()