#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# @当前时间 :2024/4/11 20:12
# @Author  : TS
# @Email   : TS@gmail.com
# @File    : ts2.py
# @Software: PyCharm
"""
import json
import re

import requests

cookies = {
    'x-jupiter-uuid': '17128369586802544',
    'Hm_lvt_c36ebf0e0753eda09586ef4fb80ea125': '1712836959',
    'count-client-api_sid': 'eyJfZXhwaXJlIjoxNzE0MDQ2NTU5NjU3LCJfbWF4QWdlIjoxMjA5NjAwMDAwfQ==',
    'passport_csrf_token': '365a8f90d26f18bdea0e60a24bfd7440',
    'passport_csrf_token_default': '365a8f90d26f18bdea0e60a24bfd7440',
    'ttcid': '0d98f6b4a7134d9aae908799a745be6e36',
    'Hm_lpvt_c36ebf0e0753eda09586ef4fb80ea125': '1712837007',
    'msToken': 'UGnkXfxy8NnVRcaZFyhMjwpXflxFqXAl3Af_fZSoe97xGtQWjipkbtkbuY2iBqz0aY27FhB6Qo7VRHhp0op9pz6awjUHTRHVOxV8YR2hV6f5ceHq9n0k',
    'msToken': 'UPChvwxdFuHD1PbK_3O6KYMqu1X0Kdghh5xGRnBUa0YJ7t-lC9aHeGJ8Z1L9bW5oU8JsQ7Hvmkzn2FXU4g4Zx_iqZAtom-l63RRvd1s19LhwOa2UoUa5nNv4HR5VCg==',
    'tt_scid': '6LTK5A4pEaQDL0eOaEZKk8YdYBXAMvLEDTsrCfLT-3ZuCGcnCYN2QjNDezzXNNZYf732',
}

headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'zh-CN,zh;q=0.9',
    'cache-control': 'no-cache',
    # 'cookie': 'x-jupiter-uuid=17128369586802544; Hm_lvt_c36ebf0e0753eda09586ef4fb80ea125=1712836959; count-client-api_sid=eyJfZXhwaXJlIjoxNzE0MDQ2NTU5NjU3LCJfbWF4QWdlIjoxMjA5NjAwMDAwfQ==; passport_csrf_token=365a8f90d26f18bdea0e60a24bfd7440; passport_csrf_token_default=365a8f90d26f18bdea0e60a24bfd7440; ttcid=0d98f6b4a7134d9aae908799a745be6e36; Hm_lpvt_c36ebf0e0753eda09586ef4fb80ea125=1712837007; msToken=UGnkXfxy8NnVRcaZFyhMjwpXflxFqXAl3Af_fZSoe97xGtQWjipkbtkbuY2iBqz0aY27FhB6Qo7VRHhp0op9pz6awjUHTRHVOxV8YR2hV6f5ceHq9n0k; msToken=UPChvwxdFuHD1PbK_3O6KYMqu1X0Kdghh5xGRnBUa0YJ7t-lC9aHeGJ8Z1L9bW5oU8JsQ7Hvmkzn2FXU4g4Zx_iqZAtom-l63RRvd1s19LhwOa2UoUa5nNv4HR5VCg==; tt_scid=6LTK5A4pEaQDL0eOaEZKk8YdYBXAMvLEDTsrCfLT-3ZuCGcnCYN2QjNDezzXNNZYf732',
    'pragma': 'no-cache',
    'sec-ch-ua': '"Google Chrome";v="123", "Not:A-Brand";v="8", "Chromium";v="123"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36',
}
params = {
    'type': '1',
}
response = requests.get('https://trendinsight.oceanengine.com/arithmetic-index', params=params, cookies=cookies,
                        headers=headers).text
fdf = re.sub('\s+', '', response)
ds = re.findall('window\._SSR_DATA\=\{.*}', fdf)[0].replace('window._SSR_DATA=', '')#.rstrip(',')
json_data=json.loads(ds)
loadersData=json_data.get('data').get('loadersData').get('"8d3dc56ea10e8426b1dde2ba4b5ead84_0"').get('data')
for i in loadersData.get('current'):#抖音实时热点
    rank=i.get('rank')
    topic_name = i.get('topic_name')
    topic_index=i.get('topic_index')+'万'
    category = i.get('category')
    topic_name_url='https://trendinsight.oceanengine.com/arithmetic-index/hot?topic_name='+topic_name #热点指数链接
    print(rank,
          topic_name,
          topic_index,
          category,topic_name_url)
for j in loadersData.get('rocketing'):#抖音飙升热点
    rank=j.get('rank')
    topic_name = j.get('topic_name')
    topic_index = j.get('topic_index') + '万'
    category = j.get('category')
    topic_name_url='https://trendinsight.oceanengine.com/arithmetic-index/hot?topic_name='+topic_name
    # print(rank,
    # topic_name,
    # topic_index,
    # category)
