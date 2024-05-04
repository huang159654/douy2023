#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# @当前时间 :2024/1/29 14:50
# @Author  : TS
# @Email   : TS@gmail.com
# @File    : ts2.py
# @Software: PyCharm
"""
import requests
from DY_Read import Read_sql
from DY_Read import Read_csv
from DY_headers import ALL_headers
class DY_retweet_sql():#点赞和转发sql
    def __init__(self):
        pass
    def def_headers(self):
        headers=ALL_headers().def_retweet_headers()
        return headers
    def def_url(self):
        url = 'https://www.douyin.com/aweme/v1/web/aweme/detail/?'
        return url
    def def_queries(self,aweme_id=None):
        queries = f'device_platform=webapp&aid=6383&channel=channel_pc_web&aweme_id={aweme_id}&pc_client_type=1&version_code=190500&version_name=19.5.0&cookie_enabled=true&screen_width=1920&screen_height=1080&browser_language=zh-CN&browser_platform=Win32&browser_name=Chrome&browser_version=120.0.0.0&browser_online=true&engine_name=Blink&engine_version=120.0.0.0&os_name=Windows&os_version=10&cpu_core_num=8&device_memory=8&platform=PC&downlink=10&effective_type=4g&round_trip_time=50&webid=7317023263425775145&msToken=xjM8LvEblV6EJpZ4UAxxmdicTifzLGCqRtKbM-c1T1VCbz_fk5YUkaoH0vRBiumYmSvWZxBcRiVeaTSLov4D11ZFLjAq7DLOhuEba5QFJBQiT_YEtlg6AWMlw8sW'
        return queries
    def def_requests(self,):
        for data_s in Read_sql().def_sql():
            aweme_id=data_s['id']
            data = {
                "group": "test_web",
                "action": "test_xb",
                "url": self.def_queries(aweme_id=aweme_id)
            }
            res = requests.get("http://127.0.0.1:5612/business/invoke", params=data)
            d = res.json()
            x_b = self.def_url() + self.def_queries(aweme_id=aweme_id) + '&X-Bogus=' + d['data']
            response =requests.get(url=x_b,headers=self.def_headers()).json()
            if response['aweme_detail']!=None:
                dict = {'response': [response], }
                yield dict
            else:
                response['aweme_detail'] = None
                with open('点赞和转发url错误链接.txt', mode='a', ) as f:
                    url='https://www.douyin.com/video/'+aweme_id
                    txt = url + '\n'  # 数据分行
                    f.write(txt)
    def def_requests_csv(self,):
        for data_s in Read_csv().def_csv():
            aweme_id=data_s['id']
            data = {
                "group": "test_web",
                "action": "test_xb",
                "url": self.def_queries(aweme_id=aweme_id)
            }
            res = requests.get("http://127.0.0.1:5612/business/invoke", params=data)
            d = res.json()
            x_b = self.def_url() + self.def_queries(aweme_id=aweme_id) + '&X-Bogus=' + d['data']
            response =requests.get(url=x_b,headers=self.def_headers()).json()
            if response['aweme_detail']!=None:
                dict = {'response': [response], }
                yield dict
            else:
                response['aweme_detail'] = None
                with open('点赞和转发url错误链接.txt', mode='a', ) as f:
                    url='https://www.douyin.com/video/'+aweme_id
                    txt = url + '\n'  # 数据分行
                    f.write(txt)
class DY_retweet_csv():#点赞和转发csv
    def __init__(self):
        pass
    def def_headers(self):
        headers=ALL_headers().def_retweet_headers()
        return headers
    def def_url(self):
        url = 'https://www.douyin.com/aweme/v1/web/aweme/detail/?'
        return url
    def def_queries(self,aweme_id=None):
        queries = f'device_platform=webapp&aid=6383&channel=channel_pc_web&aweme_id={aweme_id}&pc_client_type=1&version_code=190500&version_name=19.5.0&cookie_enabled=true&screen_width=1920&screen_height=1080&browser_language=zh-CN&browser_platform=Win32&browser_name=Chrome&browser_version=120.0.0.0&browser_online=true&engine_name=Blink&engine_version=120.0.0.0&os_name=Windows&os_version=10&cpu_core_num=8&device_memory=8&platform=PC&downlink=10&effective_type=4g&round_trip_time=50&webid=7317023263425775145&msToken=xjM8LvEblV6EJpZ4UAxxmdicTifzLGCqRtKbM-c1T1VCbz_fk5YUkaoH0vRBiumYmSvWZxBcRiVeaTSLov4D11ZFLjAq7DLOhuEba5QFJBQiT_YEtlg6AWMlw8sW'
        return queries
    def def_requests(self,):
        for data_s in Read_csv().def_csv():
            aweme_id=data_s['id']
            data = {
                "group": "test_web",
                "action": "test_xb",
                "url": self.def_queries(aweme_id=aweme_id)
            }
            res = requests.get("http://127.0.0.1:5612/business/invoke", params=data)
            d = res.json()
            x_b = self.def_url() + self.def_queries(aweme_id=aweme_id) + '&X-Bogus=' + d['data']
            response =requests.get(url=x_b,headers=self.def_headers()).json()
            if response['aweme_detail']!=None:
                dict = {'response': [response], }
                yield dict
            else:
                response['aweme_detail'] = None
                with open('点赞和转发url错误链接.txt', mode='a', ) as f:
                    url='https://www.douyin.com/video/'+aweme_id
                    txt = url + '\n'  # 数据分行
                    f.write(txt)

if __name__=='__main__':
    DY_retweet_sql().def_requests()
    # DY_retweet_csv().def_requests()
    # DY_retweet()