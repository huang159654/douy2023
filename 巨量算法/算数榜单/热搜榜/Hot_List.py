#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# @当前时间 :2024/4/11 21:46
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
    'msToken': 'b7dRcsJElp0gS61kX8_Cyi-07O9rt-MH9UnDhV1gtATxDwrd9yKSUzwnwPt-4YVe1fbDX_kcQo7XRe6AViwXlEKHuk8_HnqJJst7DofDf_wF9oPDKk8DqtT5zIoM-g==',
    'msToken': '_SCMkTogQkYc8qhAi0h2NEp02eRb1A73L8a2LGFbgtnosRfVYZu6LqKtu7V6uKRGu3nNfYsypZ16pJkrum4uQnG2WJMD2Zm2Z5r7OAA3YN_hLUNg72ppqdN1kSe49Q==',
    'tt_scid': 'OVoAcJI7WHaq0mK6rIc.KdiI4vGLRY0VlZmD-QBJVfI-0vUTN1401nuorUpxKow730b1',
    'Hm_lpvt_c36ebf0e0753eda09586ef4fb80ea125': '1712842914',
}

headers = {
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'zh-CN,zh;q=0.9',
    'appsource': 'PC',
    'cache-control': 'no-cache',
    'content-type': 'application/json',
    # 'cookie': 'x-jupiter-uuid=17128369586802544; Hm_lvt_c36ebf0e0753eda09586ef4fb80ea125=1712836959; count-client-api_sid=eyJfZXhwaXJlIjoxNzE0MDQ2NTU5NjU3LCJfbWF4QWdlIjoxMjA5NjAwMDAwfQ==; passport_csrf_token=365a8f90d26f18bdea0e60a24bfd7440; passport_csrf_token_default=365a8f90d26f18bdea0e60a24bfd7440; ttcid=0d98f6b4a7134d9aae908799a745be6e36; n_mh=XFBc0LpEzHCfYx5Ouxe_1FGaFhbJIkYdGUcgpBVduXw; passport_auth_status=e9d3e489705f1c89334ff11a69c75f8e%2C; passport_auth_status_ss=e9d3e489705f1c89334ff11a69c75f8e%2C; sso_uid_tt=690c20b0aaf41883733b975deef3d6fc; sso_uid_tt_ss=690c20b0aaf41883733b975deef3d6fc; toutiao_sso_user=c122517c40859ed3f553965a3a9f262d; toutiao_sso_user_ss=c122517c40859ed3f553965a3a9f262d; sid_ucp_sso_v1=1.0.0-KDJmYTEwY2VhYzJjOWI3ZTQwMjA2ODAwODNjNmJjZDk3NWMxMTRjMTkKFwjNjMCjqcymAxDjy9-wBhjS3BU4CEAmGgJsZiIgYzEyMjUxN2M0MDg1OWVkM2Y1NTM5NjVhM2E5ZjI2MmQ; ssid_ucp_sso_v1=1.0.0-KDJmYTEwY2VhYzJjOWI3ZTQwMjA2ODAwODNjNmJjZDk3NWMxMTRjMTkKFwjNjMCjqcymAxDjy9-wBhjS3BU4CEAmGgJsZiIgYzEyMjUxN2M0MDg1OWVkM2Y1NTM5NjVhM2E5ZjI2MmQ; uid_tt_count=6a27102db4ad79546877592c6239f7c2; uid_tt_ss_count=6a27102db4ad79546877592c6239f7c2; sid_tt_count=1961ce74288f9df0d9f14deeb890948b; sessionid_count=1961ce74288f9df0d9f14deeb890948b; sessionid_ss_count=1961ce74288f9df0d9f14deeb890948b; sid_ucp_v1_count=1.0.0-KDhiODBmYmE1ZDI1ZDg2NmIyZmE5ZTg2ZTE4Nzc4YzEzMGFiOTFjMDYKFgjNjMCjqcymAxDky9-wBhimDDgIQCYaAmxmIiAxOTYxY2U3NDI4OGY5ZGYwZDlmMTRkZWViODkwOTQ4Yg; ssid_ucp_v1_count=1.0.0-KDhiODBmYmE1ZDI1ZDg2NmIyZmE5ZTg2ZTE4Nzc4YzEzMGFiOTFjMDYKFgjNjMCjqcymAxDky9-wBhimDDgIQCYaAmxmIiAxOTYxY2U3NDI4OGY5ZGYwZDlmMTRkZWViODkwOTQ4Yg; sid_guard_count=1961ce74288f9df0d9f14deeb890948b%7C1712842212%7C5184000%7CMon%2C+10-Jun-2024+13%3A30%3A12+GMT; msToken=b7dRcsJElp0gS61kX8_Cyi-07O9rt-MH9UnDhV1gtATxDwrd9yKSUzwnwPt-4YVe1fbDX_kcQo7XRe6AViwXlEKHuk8_HnqJJst7DofDf_wF9oPDKk8DqtT5zIoM-g==; msToken=_SCMkTogQkYc8qhAi0h2NEp02eRb1A73L8a2LGFbgtnosRfVYZu6LqKtu7V6uKRGu3nNfYsypZ16pJkrum4uQnG2WJMD2Zm2Z5r7OAA3YN_hLUNg72ppqdN1kSe49Q==; tt_scid=OVoAcJI7WHaq0mK6rIc.KdiI4vGLRY0VlZmD-QBJVfI-0vUTN1401nuorUpxKow730b1; Hm_lpvt_c36ebf0e0753eda09586ef4fb80ea125=1712842914',
    'origin': 'https://trendinsight.oceanengine.com',
    'pragma': 'no-cache',
    'referer': 'https://trendinsight.oceanengine.com/arithmetic-list?type=1&appName=toutiao',
    'sec-ch-ua': '"Google Chrome";v="123", "Not:A-Brand";v="8", "Chromium";v="123"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36',
}

json_data = {
    'app': 'toutiao',
    'date': '20240410',#日期
}

response = requests.post(
    'https://trendinsight.oceanengine.com/api/v2/hotSearch/get_vsearch_overall_list?msToken=_SCMkTogQkYc8qhAi0h2NEp02eRb1A73L8a2LGFbgtnosRfVYZu6LqKtu7V6uKRGu3nNfYsypZ16pJkrum4uQnG2WJMD2Zm2Z5r7OAA3YN_hLUNg72ppqdN1kSe49Q==&X-Bogus=''&_signature=''',
    cookies=cookies,
    headers=headers,
    json=json_data,
).json()
 # 电影热搜榜
for i in response.get('data')[0].get('list')[0].get('score'):
    rank = i.get('rank')
    item_title = i.get('item_title')
    score_s = i.get('score')
    ring_ratio = i.get('ring_ratio') * 100
    rounded_number = str(round(ring_ratio, 2)) + '%'


for j in response.get('data')[1].get('list')[0].get('score'):#电视剧热搜榜
    rank = j.get('rank')
    item_title = j.get('item_title')
    score_s = j.get('score')
    ring_ratio = j.get('ring_ratio') * 100
    rounded_number = str(round(ring_ratio, 2)) + '%'

for k in response.get('data')[2].get('list')[0].get('score'):#
    rank = k.get('rank')
    item_title = k.get('item_title')
    score_s = k.get('score')
    ring_ratio = k.get('ring_ratio') * 100
    rounded_number = str(round(ring_ratio, 2)) + '%'
    print(rank,
          item_title,
          score_s,
          rounded_number)
