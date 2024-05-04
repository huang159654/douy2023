#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# @当前时间 :2024/1/29 16:25
# @Author  : TS
# @Email   : TS@gmail.com
# @File    : ts2.py
# @Software: PyCharm
"""
import os
import time

import pandas as pd
import pymysql

from DY_retweet_requests import DY_retweet_sql
from DY_retweet_requests import DY_retweet_csv
from DY_comments_requests import Comments_requests_sql
from DY_comments_requests import Comments_requests_csv
from DY_secondary_comments_requests import  DY_secondary_comments_sql

class Retweet_parse_list():  # 点赞和转发 sql数据解析
    def __init__(self):
        pass
    def def_parse_response(self):
        for data_s in DY_retweet_sql().def_requests():
            data = data_s['response'][0]
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
            dict = {'昵称': [author], '推⼴链接': [awem_id], '发布日期': [create_time], '帖⼦名称': [preview_title],
                    '点赞': [digg_count], '评论': [comment_count], '收藏': [collect_count],
                    '转发': [share_count], }
            yield dict

    def sql_s(self):#保存sql
        db = pymysql.connect(host='localhost', user='root', password='huang159', port=3306, db='dy_creat')
        mycursor = db.cursor()
        sql = "insert into conten (awem_id,author,create_time,preview_title,digg_count,comment_count,collect_count,share_count) VALUES (%s, %s, %s,%s, %s, %s,%s, %s);"
        for data in self.def_parse_response():
            print(data["推⼴链接"], data["昵称"], data["发布日期"], data["帖⼦名称"], data["点赞"], data["评论"],
                  data["收藏"], data["转发"])
            # 提取字典中的值
            values = (data["推⼴链接"], data["昵称"], data["发布日期"], data["帖⼦名称"], data["点赞"], data["评论"],
                      data["收藏"], data["转发"])
            # 执行SQL插入语句enen
            mycursor.execute(sql, values)
            db.commit()
    def def_parse_responses(self):
        for data_s in DY_retweet_sql().def_requests_csv():
            data = data_s['response'][0]
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
            dict = {'昵称': [author], '推⼴链接': [awem_id], '发布日期': [create_time], '帖⼦名称': [preview_title],
                    '点赞': [digg_count], '评论': [comment_count], '收藏': [collect_count],
                    '转发': [share_count], }
            yield dict

    def def_csv(self):#保存csv
        for data in self.def_parse_responses():
            dataframe = pd.DataFrame(data)
            if not os.path.exists('点赞和转发.csv'):
                dataframe.to_csv('./点赞和转发.csv', mode='a',encoding='utf_8_sig',index=False, )
            dataframe.to_csv('./点赞和转发.csv', mode='a',encoding='utf_8_sig', header=False, index=False)
            # current_time = datetime.datetime.now()
            print(data,'保存完毕！')

class Comments_parse_sql():#一级评论
    def __init__(self):
        pass
    def def_parse_response(self):#解析的数据
        for dara_s in Comments_requests_sql().def_tota_l():
            # print(dara_s)
            data=dara_s['response']
            if data['comments']:
                for compile in data['comments']:
                    create = compile.get('create_time')  # 发布时间
                    timeArray = time.localtime(create)
                    create_time = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
                    nickname = compile.get('user').get('nickname')  # 用户昵称
                    text_s = compile.get('text')  # 评论内容
                    ip_label = compile.get('ip_label')  # ip地址
                    digg_count = compile.get('digg_count')  # 点赞数
                    reply_comment_total = compile.get('reply_comment_total')  # 回复数
                    cid = compile.get('cid')  # 主键id
                    sec_uid = compile.get('user').get('sec_uid')  # 用户详情页
                    aweme_id = compile.get('aweme_id')  # 视频id
                    awem_id = 'https://www.douyin.com/video/' + aweme_id
                    dict = {'id': [cid], '推广链接': [awem_id], '评论内容': [text_s], '点赞数': [digg_count],
                             '回复数': [reply_comment_total], 'ip地址': [ip_label], '发布时间': [create_time],
                             '用户昵称': [nickname]}
                    # print(dict)
                    yield dict
    def def_sql(self):#保存sql
        db = pymysql.connect(host='localhost', user='root', password='huang159', port=3306, db='dy_creat')
        mycursor = db.cursor()
        sql = "insert into comments (awem_id,cid,text_s,digg_count,reply_comment_total,ip_label,create_time,nic_kname) VALUES (%s, %s, %s,%s, %s, %s,%s, %s);"
        for data in self.def_parse_response():
            # print(data["推广链接"][0])
            values = (
                data["推广链接"], data["id"], data["评论内容"], data["点赞数"], data["回复数"],
                data["ip地址"],
                data["发布时间"], data["用户昵称"])
            mycursor.execute(sql, values)
            db.commit()
            print('采集完毕！', values,)
    def def_parse_response_csv(self):#解析的数据
        for dara_s in Comments_requests_csv().def_tota_l():
            data=dara_s['response']
            if data['comments']:
                for compile in data['comments']:
                    create = compile.get('create_time')  # 发布时间
                    timeArray = time.localtime(create)
                    create_time = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
                    nickname = compile.get('user').get('nickname')  # 用户昵称
                    text_s = compile.get('text')  # 评论内容
                    ip_label = compile.get('ip_label')  # ip地址
                    digg_count = compile.get('digg_count')  # 点赞数
                    reply_comment_total = compile.get('reply_comment_total')  # 回复数
                    cid = compile.get('cid')  # 主键id
                    sec_uid = compile.get('user').get('sec_uid')  # 用户详情页
                    aweme_id = compile.get('aweme_id')  # 视频id
                    awem_id = 'https://www.douyin.com/video/' + aweme_id
                    dict = {'id': [cid], '推广链接': [awem_id], '评论内容': [text_s], '点赞数': [digg_count],
                             '回复数': [reply_comment_total], 'ip地址': [ip_label], '发布时间': [create_time],
                             '用户昵称': [nickname]}
                    # print(dict)
                    yield dict
    def def_csv(self):#保存csv
        for data in self.def_parse_response_csv():
            dataframe = pd.DataFrame(data)
            if not os.path.exists('./评论.csv'):
                dataframe.to_csv('./评论.csv', mode='a',encoding='utf-8-sig',index=False, )
            dataframe.to_csv('./评论.csv', mode='a',encoding='utf-8-sig', header=False, index=False)
            print(data,'保存完毕！')

class Secondary_comments_list():
    def __init__(self):
        pass

    def def_secondary_comments(self):
        for data_s in DY_secondary_comments_sql().def_def_tota_l():
            data = data_s['response']
            text_s = data_s['text']
            if data['comments']:
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
                    dict = [{'id': reply_id, '推广连接': awem_id,"主评论": text_s, '次评论': text,
                             '点赞数': digg_count, 'ip地址': ip_label, '发布时间': create_time,
                             '用户昵称': nickname, }]
                    print(dict)
                    # yield dict


if __name__=='__main__':
    # Retweet_parse_list().sql_s()
    # Retweet_parse_list().def_csv()#点赞保存
    # Comments_parse_sql().def_sql()#评论保存
    # Comments_parse_sql().def_csv() #评论保存
    Secondary_comments_list().def_secondary_comments()