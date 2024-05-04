#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# @当前时间 :2024/4/11 22:19
# @Author  : TS
# @Email   : TS@gmail.com
# @File    : ts2.py
# @Software: PyCharm
"""
import requests

cookies = {
    'x-jupiter-uuid': '17128369586802544',
    'Hm_lvt_c36ebf0e0753eda09586ef4fb80ea125': '1712836959',
    'count-client-api_sid': 'eyJfZXhwaXJlIjoxNzE0MDQ2NTU5NjU3LCJfbWF4QWdlIjoxMjA5NjAwMDAwfQ==',
    'passport_csrf_token': '365a8f90d26f18bdea0e60a24bfd7440',
    'passport_csrf_token_default': '365a8f90d26f18bdea0e60a24bfd7440',
    'ttcid': '0d98f6b4a7134d9aae908799a745be6e36',
    'n_mh': 'XFBc0LpEzHCfYx5Ouxe_1FGaFhbJIkYdGUcgpBVduXw',
    'passport_auth_status': 'e9d3e489705f1c89334ff11a69c75f8e%2C',
    'passport_auth_status_ss': 'e9d3e489705f1c89334ff11a69c75f8e%2C',
    'sso_uid_tt': '690c20b0aaf41883733b975deef3d6fc',
    'sso_uid_tt_ss': '690c20b0aaf41883733b975deef3d6fc',
    'toutiao_sso_user': 'c122517c40859ed3f553965a3a9f262d',
    'toutiao_sso_user_ss': 'c122517c40859ed3f553965a3a9f262d',
    'sid_ucp_sso_v1': '1.0.0-KDJmYTEwY2VhYzJjOWI3ZTQwMjA2ODAwODNjNmJjZDk3NWMxMTRjMTkKFwjNjMCjqcymAxDjy9-wBhjS3BU4CEAmGgJsZiIgYzEyMjUxN2M0MDg1OWVkM2Y1NTM5NjVhM2E5ZjI2MmQ',
    'ssid_ucp_sso_v1': '1.0.0-KDJmYTEwY2VhYzJjOWI3ZTQwMjA2ODAwODNjNmJjZDk3NWMxMTRjMTkKFwjNjMCjqcymAxDjy9-wBhjS3BU4CEAmGgJsZiIgYzEyMjUxN2M0MDg1OWVkM2Y1NTM5NjVhM2E5ZjI2MmQ',
    'uid_tt_count': '6a27102db4ad79546877592c6239f7c2',
    'uid_tt_ss_count': '6a27102db4ad79546877592c6239f7c2',
    'sid_tt_count': '1961ce74288f9df0d9f14deeb890948b',
    'sessionid_count': '1961ce74288f9df0d9f14deeb890948b',
    'sessionid_ss_count': '1961ce74288f9df0d9f14deeb890948b',
    'sid_ucp_v1_count': '1.0.0-KDhiODBmYmE1ZDI1ZDg2NmIyZmE5ZTg2ZTE4Nzc4YzEzMGFiOTFjMDYKFgjNjMCjqcymAxDky9-wBhimDDgIQCYaAmxmIiAxOTYxY2U3NDI4OGY5ZGYwZDlmMTRkZWViODkwOTQ4Yg',
    'ssid_ucp_v1_count': '1.0.0-KDhiODBmYmE1ZDI1ZDg2NmIyZmE5ZTg2ZTE4Nzc4YzEzMGFiOTFjMDYKFgjNjMCjqcymAxDky9-wBhimDDgIQCYaAmxmIiAxOTYxY2U3NDI4OGY5ZGYwZDlmMTRkZWViODkwOTQ4Yg',
    'sid_guard_count': '1961ce74288f9df0d9f14deeb890948b%7C1712842212%7C5184000%7CMon%2C+10-Jun-2024+13%3A30%3A12+GMT',
    'msToken': 'bcJOwjytgDkMQfImNvcw9O_5juMDf5f4eStWoHdesk8aBmgc5SCcmAigqj0Zb-W1dDsvpT4BYwpVhdMqR04cU_QP4lhtF2wUkWjQ-sO0CJiw8rbGhkwbGTmuxAo71g==',
    'msToken': 'yeuJPj6C1zobGJtpDK-xgRD3LeC5jrRnPjh4xGgpVJUzYAT8VQF-Fch5XahUDsfIWNUl9Z1094PVVNsD3ZSkHbTBrjUqQ3grcqqmc0avf_UUkcpMlSAOO-SwVGNXVQ==',
    'tt_scid': '6XMqY6j2CalTI399VePZ4xCDU7raZMOt6zoMqj.iCH4vc2cL7msCZdySSvFbM-MPf181',
    'Hm_lpvt_c36ebf0e0753eda09586ef4fb80ea125': '1712845414',
}

headers = {
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'zh-CN,zh;q=0.9',
    'appsource': 'PC',
    'cache-control': 'no-cache',
    'content-type': 'application/json',
    # 'cookie': 'x-jupiter-uuid=17128369586802544; Hm_lvt_c36ebf0e0753eda09586ef4fb80ea125=1712836959; count-client-api_sid=eyJfZXhwaXJlIjoxNzE0MDQ2NTU5NjU3LCJfbWF4QWdlIjoxMjA5NjAwMDAwfQ==; passport_csrf_token=365a8f90d26f18bdea0e60a24bfd7440; passport_csrf_token_default=365a8f90d26f18bdea0e60a24bfd7440; ttcid=0d98f6b4a7134d9aae908799a745be6e36; n_mh=XFBc0LpEzHCfYx5Ouxe_1FGaFhbJIkYdGUcgpBVduXw; passport_auth_status=e9d3e489705f1c89334ff11a69c75f8e%2C; passport_auth_status_ss=e9d3e489705f1c89334ff11a69c75f8e%2C; sso_uid_tt=690c20b0aaf41883733b975deef3d6fc; sso_uid_tt_ss=690c20b0aaf41883733b975deef3d6fc; toutiao_sso_user=c122517c40859ed3f553965a3a9f262d; toutiao_sso_user_ss=c122517c40859ed3f553965a3a9f262d; sid_ucp_sso_v1=1.0.0-KDJmYTEwY2VhYzJjOWI3ZTQwMjA2ODAwODNjNmJjZDk3NWMxMTRjMTkKFwjNjMCjqcymAxDjy9-wBhjS3BU4CEAmGgJsZiIgYzEyMjUxN2M0MDg1OWVkM2Y1NTM5NjVhM2E5ZjI2MmQ; ssid_ucp_sso_v1=1.0.0-KDJmYTEwY2VhYzJjOWI3ZTQwMjA2ODAwODNjNmJjZDk3NWMxMTRjMTkKFwjNjMCjqcymAxDjy9-wBhjS3BU4CEAmGgJsZiIgYzEyMjUxN2M0MDg1OWVkM2Y1NTM5NjVhM2E5ZjI2MmQ; uid_tt_count=6a27102db4ad79546877592c6239f7c2; uid_tt_ss_count=6a27102db4ad79546877592c6239f7c2; sid_tt_count=1961ce74288f9df0d9f14deeb890948b; sessionid_count=1961ce74288f9df0d9f14deeb890948b; sessionid_ss_count=1961ce74288f9df0d9f14deeb890948b; sid_ucp_v1_count=1.0.0-KDhiODBmYmE1ZDI1ZDg2NmIyZmE5ZTg2ZTE4Nzc4YzEzMGFiOTFjMDYKFgjNjMCjqcymAxDky9-wBhimDDgIQCYaAmxmIiAxOTYxY2U3NDI4OGY5ZGYwZDlmMTRkZWViODkwOTQ4Yg; ssid_ucp_v1_count=1.0.0-KDhiODBmYmE1ZDI1ZDg2NmIyZmE5ZTg2ZTE4Nzc4YzEzMGFiOTFjMDYKFgjNjMCjqcymAxDky9-wBhimDDgIQCYaAmxmIiAxOTYxY2U3NDI4OGY5ZGYwZDlmMTRkZWViODkwOTQ4Yg; sid_guard_count=1961ce74288f9df0d9f14deeb890948b%7C1712842212%7C5184000%7CMon%2C+10-Jun-2024+13%3A30%3A12+GMT; msToken=bcJOwjytgDkMQfImNvcw9O_5juMDf5f4eStWoHdesk8aBmgc5SCcmAigqj0Zb-W1dDsvpT4BYwpVhdMqR04cU_QP4lhtF2wUkWjQ-sO0CJiw8rbGhkwbGTmuxAo71g==; msToken=yeuJPj6C1zobGJtpDK-xgRD3LeC5jrRnPjh4xGgpVJUzYAT8VQF-Fch5XahUDsfIWNUl9Z1094PVVNsD3ZSkHbTBrjUqQ3grcqqmc0avf_UUkcpMlSAOO-SwVGNXVQ==; tt_scid=6XMqY6j2CalTI399VePZ4xCDU7raZMOt6zoMqj.iCH4vc2cL7msCZdySSvFbM-MPf181; Hm_lpvt_c36ebf0e0753eda09586ef4fb80ea125=1712845414',
    'origin': 'https://trendinsight.oceanengine.com',
    'pragma': 'no-cache',
    'referer': 'https://trendinsight.oceanengine.com/arithmetic-list?type=2&appName=aweme',
    'sec-ch-ua': '"Google Chrome";v="123", "Not:A-Brand";v="8", "Chromium";v="123"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36',
}

json_data = {
    'list_ids': [
        '2000014415',
        '2007514415',
        '2000714415',
        '2008114415',
        '2011114415',
        '2004414415',
    ],
    'app': 'aweme',
    'date': '20230303',#日期
}

response = requests.post(
    'https://trendinsight.oceanengine.com/api/v2/ecom/get_ecom_overall_list?msToken=bcJOwjytgDkMQfImNvcw9O_5juMDf5f4eStWoHdesk8aBmgc5SCcmAigqj0Zb-W1dDsvpT4BYwpVhdMqR04cU_QP4lhtF2wUkWjQ-sO0CJiw8rbGhkwbGTmuxAo71g==&X-Bogus=''&_signature=_02B4Z6wo00001LUpnJQAAIDDiICGCMw8IRi1KZgAAEtiJLTtMcXaDjoOk7ElaWT34s7FukV-OtxeDuHUqHONBUzOCLfB8c1E0eNsUeTyiXMcZqUXas1UI5YfNMNpqogvHrT79c8YnetW5NhJa7',
    cookies=cookies,
    headers=headers,
    json=json_data,
).json()
# print(response.get('data')[0].get('item_score_list'))
for i in response.get('data')[0].get('item_score_list'): #3C数码配件爆款榜
    rank=i.get('rank')
    item_name=i.get('item_name')
    sell_num = i.get('sell_num')+'万'
    item_img = i.get('item_img')
    print(rank,
          item_name,
          sell_num,
          item_img)
