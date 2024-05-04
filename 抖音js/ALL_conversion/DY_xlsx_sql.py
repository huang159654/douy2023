#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# @当前时间 :2024/1/27 19:55
# @Author  : TS
# @Email   : TS@gmail.com
# @File    : ts2.py
# @Software: PyCharm
"""
import os

import pandas as pd
import pymysql
import requests

from 函数.抖音.抖音js.ALL_sql.Create_database import Create_data


class Xlsx():  # 读取xlsx 文件中https://v.douyin.com/iKeD74w/链接
    def __init__(self):
        self.headers = {
            'authority': 'www.douyin.com',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'accept-language': 'zh-CN,zh;q=0.9',
            'cache-control': 'no-cache',
            'cookie': 'douyin.com; webcast_local_quality=null; __ac_referer=__ac_blank; xgplayer_user_id=315442593126; n_mh=MPHRKGEs6Mdv8j9-lYQ_xItbJLeVCy02zT61y_-m6jI; __security_server_data_status=1; store-region=cn-fj; store-region-src=uid; ttwid=1%7CoUtUgD7EvPpj6Qu64gb758lvWI_SmQLFtcu0mjIFO1M%7C1692263559%7C024dd1b19b66299baf4340d40d5d48e9e9fe72690b500652b6207a85da5e35e8; douyin.com; device_web_cpu_core=8; device_web_memory_size=8; webcast_local_quality=null; bd_ticket_guard_client_data=eyJiZC10aWNrZXQtZ3VhcmQtdmVyc2lvbiI6MiwiYmQtdGlja2V0LWd1YXJkLWl0ZXJhdGlvbi12ZXJzaW9uIjoxLCJiZC10aWNrZXQtZ3VhcmQtcmVlLXB1YmxpYy1rZXkiOiJCUDFlOHB4MW92OE1DaEE3VUZVRDZHc0JEQW53NzJpUnpZSW91OVoxNVU2QVQzTnhhYlJNTjFWY1VselU2eEM2aGk5UmZicEthVHNRYVRJc05GUFAyQWM9IiwiYmQtdGlja2V0LWd1YXJkLXdlYi12ZXJzaW9uIjoxfQ==; csrf_session_id=ac094498cd866532cb97257b8848e8e0; FORCE_LOGIN=%7B%22videoConsumedRemainSeconds%22%3A180%2C%22isForcePopClose%22%3A1%7D; _bd_ticket_crypt_doamin=3; passport_csrf_token=81cbc5a38ec92a37ccbd7c177cab11ae; passport_csrf_token_default=81cbc5a38ec92a37ccbd7c177cab11ae; s_v_web_id=verify_lm7q7ttt_m2YMF4bw_zRxx_4KFM_Apqv_LulDWWRkZe0v; passport_assist_user=Cj_3Ej528MWeb0mgd6n_uL1Px2DP1vnu5HXHvuRvdZWfMBFzQ_jxpTnozD8uUEPlLi_Gd-Rsckoz2hQYfziFrvoaSgo8ySgvez2BLMYfu4NCJViB1fNY62sZH5qGUOTOWOWOPqd3S20iXHCGgbZrCYYVs9yFTH08gIfVcvzld4_tEOKbuw0Yia_WVCABIgEDah0lkw%3D%3D; sso_uid_tt=864d985e8340bdad2e94b0d01f327f9d; sso_uid_tt_ss=864d985e8340bdad2e94b0d01f327f9d; toutiao_sso_user=3904e7c884cd7dc5f38b51b9af4ffaae; toutiao_sso_user_ss=3904e7c884cd7dc5f38b51b9af4ffaae; sid_ucp_sso_v1=1.0.0-KDliOTM5NTBhYWQ2Y2FjMDNhMTdhYzZjNjNiM2UyOTQyNTBlMTYyNTgKHgjI-YDN2PQHEL_m4acGGO8xIAwwybbi-gU4BkD0BxoCaGwiIDM5MDRlN2M4ODRjZDdkYzVmMzhiNTFiOWFmNGZmYWFl; ssid_ucp_sso_v1=1.0.0-KDliOTM5NTBhYWQ2Y2FjMDNhMTdhYzZjNjNiM2UyOTQyNTBlMTYyNTgKHgjI-YDN2PQHEL_m4acGGO8xIAwwybbi-gU4BkD0BxoCaGwiIDM5MDRlN2M4ODRjZDdkYzVmMzhiNTFiOWFmNGZmYWFl; odin_tt=c7d385feb6f9217e7ff2fc43a1a027dfefa0a7a674d97c3e0397d4190f2c90b0f014c4908c71f4b8a176fea366e7aa1236973dc22050f1d7b349b636fd75a563; passport_auth_status=1294793ab7c918c625efed030993a199%2C3cc5c1ca24a0abc7bb99d904d186b483; passport_auth_status_ss=1294793ab7c918c625efed030993a199%2C3cc5c1ca24a0abc7bb99d904d186b483; uid_tt=0d5cc25b4e44f2ac50ab291a672c1407; uid_tt_ss=0d5cc25b4e44f2ac50ab291a672c1407; sid_tt=c6ad20c71e6408a172b6f0abbfbcc970; sessionid=c6ad20c71e6408a172b6f0abbfbcc970; sessionid_ss=c6ad20c71e6408a172b6f0abbfbcc970; publish_badge_show_info=%220%2C0%2C0%2C1694004040535%22; LOGIN_STATUS=1; _bd_ticket_crypt_cookie=ec95c620b10f72bcf6d1bbaafe9a7592; sid_guard=c6ad20c71e6408a172b6f0abbfbcc970%7C1694004052%7C5183982%7CSun%2C+05-Nov-2023+12%3A40%3A34+GMT; sid_ucp_v1=1.0.0-KDE5MGFiM2RlOTIwMWViOWZjNWRiNTNlYTg1ZmY3Y2YyYzE5ZGUxMTkKGgjI-YDN2PQHENTm4acGGO8xIAw4BkD0B0gEGgJsZiIgYzZhZDIwYzcxZTY0MDhhMTcyYjZmMGFiYmZiY2M5NzA; ssid_ucp_v1=1.0.0-KDE5MGFiM2RlOTIwMWViOWZjNWRiNTNlYTg1ZmY3Y2YyYzE5ZGUxMTkKGgjI-YDN2PQHENTm4acGGO8xIAw4BkD0B0gEGgJsZiIgYzZhZDIwYzcxZTY0MDhhMTcyYjZmMGFiYmZiY2M5NzA; __live_version__=%221.1.1.3635%22; live_can_add_dy_2_desktop=%221%22; pwa2=%220%7C0%7C3%7C0%22; architecture=amd64; strategyABtestKey=%221694493567.562%22; VIDEO_FILTER_MEMO_SELECT=%7B%22expireTime%22%3A1695098368651%2C%22type%22%3A1%7D; my_rd=2; SEARCH_RESULT_LIST_TYPE=%22single%22; download_guide=%223%2F20230912%2F1%22; volume_info=%7B%22isUserMute%22%3Afalse%2C%22isMute%22%3Afalse%2C%22volume%22%3A0.971%7D; __ac_nonce=06500498d006cecd6535f; __ac_signature=_02B4Z6wo00f01TTHtdgAAIDBtMVPmnGKg60057FAACg0SGqwYkFr9vFSo1RkKlU7Z2Bv2GRL0SQXjwRRQ.f1h9oeSqDZIhYLddbBmzS7BwuiMVscajRYnUy7S5fwcj8HaUAhbNU0iMjZVUkbcc; stream_recommend_feed_params=%22%7B%5C%22cookie_enabled%5C%22%3Atrue%2C%5C%22screen_width%5C%22%3A1280%2C%5C%22screen_height%5C%22%3A720%2C%5C%22browser_online%5C%22%3Atrue%2C%5C%22cpu_core_num%5C%22%3A8%2C%5C%22device_memory%5C%22%3A8%2C%5C%22downlink%5C%22%3A10%2C%5C%22effective_type%5C%22%3A%5C%224g%5C%22%2C%5C%22round_trip_time%5C%22%3A50%7D%22; FOLLOW_LIVE_POINT_INFO=%22MS4wLjABAAAABOhvAjIm3vns-R1X1jh5dt-kQ5s_ihMeO9UG_JpkDRw%2F1694534400000%2F0%2F0%2F1694518236126%22; home_can_add_dy_2_desktop=%221%22; msToken=fu_pi1jWFQq3cUGhU2M-0eV-YEpsbgNdhFG7dcVxLW3GGG5p053Nr5uwJG2hWoAeSg95JMyx7durbOozzx9HE5Nw4e_jrm427-Yt4vkUDyrKwm5ahSnz6A==; msToken=BhMnGpkrYGG0dCSEEuQ3chJ4WhkEe5TTrcSbHoNVGqH3TTb7jyFs14tfoDlQnOA4R3q01lGqlPrYs-Z6f7l_W6beWew_OjxxRmVJ5_oH2RNQlYRkB4VCyQ==; tt_scid=h.WNfkKS4-tERVRAUR6J4XanNTpP7Mk1FMutg0QHoEAi8xk.ijhpqAZiJZqn9WKIdcfb; IsDouyinActive=false; passport_fe_beating_status=false',
            'pragma': 'no-cache',
            'sec-ch-ua': '"Chromium";v="116", "Not)A;Brand";v="24", "Google Chrome";v="116"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'none',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',
        }

    def xlsx(self):
        df = pd.read_excel(r'C:\Users\Administrator\PycharmProjects\pythonProject\函数\抖音\抖音js\ALL_file\抖音推广链接.xlsx', sheet_name='Sheet1', )
        data = df.values.tolist()
        for i in data:  # 使用pandas转换xlsx数据
            try:
                value = i[3]  # i[3]，是取列表里面的第4列数据
                res = requests.get(url=value, headers=self.headers, allow_redirects=False, timeout=3)
                if res.status_code == 302:
                    _url = res.headers['location']
                    id = _url.split('/')[5]  # 提取视频id
                    a_id = 'https://www.douyin.com/video/' + id  # 视频链接
                    dict = [{"id": a_id }]
                    yield dict  # 循环数据使用yield
            except:
                # file_path = ""
                with open(r'C:\Users\Administrator\PycharmProjects\pythonProject\函数\抖音\抖音js\wrong_file/url错误链接.txt', mode='a', ) as f:
                    txt = value + '\n'  # 数据分行
                    f.write(txt)

    def def_sql_url(self):  # 保存到数据库
        Create_data().def_url()
        db = pymysql.connect(host='localhost', user='root', password='huang159', port=3306, db='dy_creat')
        mycursor = db.cursor()
        sql_s = "insert into url (dy_url) VALUES (%s);"
        for data in self.xlsx():
            # print(data[0]["id"])
            id = data[0]["id"]
            try:
                sql = "select * from url where dy_url='{}';".format(id)
                mycursor.execute(sql)
                ret = mycursor.fetchone()
                if ret:
                    print('Data duplication!')  # 数据重复
                else:
                    values = (data[0]["id"])
                    mycursor.execute(sql_s, values)
                    db.commit()
                    print("+++++++++++++++++++转换URL保存到数据库成功+++++++++++++++++++")
            except:
                with open(r'C:\Users\Administrator\PycharmProjects\pythonProject\函数\抖音\抖音js\wrong_file/url错误链接.txt', mode='a', ) as f:
                    txt = data["id"][0] + '\n'  # 数据分行
                    f.write(txt)


class Xlsx_video():  # 读取xlsx 文件中https://www.douyin.com/video/7312743380214238498 链接
    def __init__(self):
        pass

    def def_xlsx(self):
        Create_data().def_url()
        df = pd.read_excel(r'C:\Users\Administrator\PycharmProjects\pythonProject\函数\抖音\抖音js\ALL_file\抖音推广链接.xlsx', sheet_name='Sheet2', )
        data = df.values.tolist()
        for i in data:  # 使用pandas转换xlsx数据
            try:
                value = i[3]
                dict = [{"id": value}]
                yield dict  # 循环数据使用yield
            except:
                with open(r'C:\Users\Administrator\PycharmProjects\pythonProject\函数\抖音\抖音js\wrong_file/url错误链接.txt', mode='a', ) as f:
                    txt = value + '\n'  # 数据分行
                    f.write(txt)
    def def_sql_url(self):  # 保存到数据库
        db = pymysql.connect(host='localhost', user='root', password='huang159', port=3306, db='dy_creat')
        mycursor = db.cursor()
        sql_s = "insert into url (dy_url) VALUES (%s);"
        for data in self.def_xlsx():
            # print(data[0]["id"])
            id=data[0]["id"]
            try:
                sql = "select * from url where dy_url='{}';".format(id) #特殊字符需要再{}这里加上冒号''
                mycursor.execute(sql)
                ret = mycursor.fetchone()
                if ret:
                    print('Data duplication!')  # 数据重复
                else:
                    values = (data[0]["id"])
                    mycursor.execute(sql_s, values)
                    db.commit()
                    print("+++++++++++++++++++转换URL保存到数据库成功+++++++++++++++++++")
            except:
                with open(r'C:\Users\Administrator\PycharmProjects\pythonProject\函数\抖音\抖音js\wrong_file/url错误链接.txt', mode='a', ) as f:
                    txt = data["id"][0] + '\n'  # 数据分行
                    f.write(txt)

if __name__ == '__main__':
    Xlsx().def_sql_url() #保存数据库文件 https://v.douyin.com/iKeD74w/ 需要转换
    # Xlsx_video().def_sql_url()#保存数据库文件 https://www.douyin.com/video/7312743380214238498