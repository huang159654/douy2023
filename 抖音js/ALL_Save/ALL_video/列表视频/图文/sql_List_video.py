#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# @当前时间 :2024/3/2 16:13
# @Author  : TS
# @Email   : TS@gmail.com
# @File    : ts2.py
# @Software: PyCharm
"""
import os
import re

import execjs
import requests

from 函数.抖音.抖音js.ALL_headers.headers_all import ALL_headers
from 函数.抖音.抖音js.ALL_js.XB_js import XB_js
from 函数.抖音.抖音js.ALL_sql.DY_Read import Read_sql


class List_video(): #
    def __init__(self):
        if not os.path.exists(r'C:\Users\Administrator\PycharmProjects\pythonProject\函数\抖音\抖音js/video'):
            os.mkdir(r'C:\Users\Administrator\PycharmProjects\pythonProject\函数\抖音\抖音js/video')

    def def_headers(self):
        headers = {
            'authority': 'www.douyin.com',
            'accept': 'application/json, text/plain, */*',
            'accept-language': 'zh-CN,zh;q=0.9',
            'cache-control': 'no-cache',
            'cookie': 'dy_swidth=1920; dy_sheight=1080; xgplayer_user_id=852623206467; passport_csrf_token=87388d0c0f3b2d00efe04b3e71ca8fa4; passport_csrf_token_default=87388d0c0f3b2d00efe04b3e71ca8fa4; bd_ticket_guard_client_web_domain=2; s_v_web_id=verify_lt2i6cdn_a2db2f2f_ad34_bca8_af60_acb9b7254f37; _bd_ticket_crypt_doamin=2; __security_server_data_status=1; store-region=cn-fj; store-region-src=uid; publish_badge_show_info=%220%2C0%2C0%2C1709557100840%22; volume_info=%7B%22isUserMute%22%3Afalse%2C%22isMute%22%3Atrue%2C%22volume%22%3A0.991%7D; SEARCH_RESULT_LIST_TYPE=%22single%22; pwa2=%220%7C0%7C3%7C1%22; download_guide=%221%2F20240308%2F1%22; ttwid=1%7Cb69uIT22KRguI_iI3SiLqFDLXpBJ6tdcbbJ3ySBzErk%7C1709860570%7Cd39dd4c992b38fd63f30e0a5b5ead2c74b4bf60fe2058153b6a07673489f52aa; FORCE_LOGIN=%7B%22videoConsumedRemainSeconds%22%3A180%2C%22isForcePopClose%22%3A1%7D; __live_version__=%221.1.1.8626%22; live_can_add_dy_2_desktop=%220%22; live_use_vvc=%22false%22; strategyABtestKey=%221709949336.973%22; FOLLOW_LIVE_POINT_INFO=%22MS4wLjABAAAABpiZ3d1HtcvYHvnZQ6Kke_2iTMBROJYpqmlz8x1mopQ4tDHrj6vQ_4QhUX1waRl4%2F1710000000000%2F0%2F1709950576421%2F0%22; douyin.com; device_web_cpu_core=8; device_web_memory_size=8; architecture=amd64; csrf_session_id=98213de129121f485e78a0e31fcec99a; GlobalGuideTimes=%221709951538%7C1%22; __ac_signature=_02B4Z6wo00f01yBQUlQAAIDAHflIyNRo4Q8gcFbAAK4Khtf5Rh8IqAstXy80yEclzWOieVHk1tLd7JJS2QgYZuWduPzfzCLYisWWto1-UlJUR5XoJspjp.C99Xe.5P8kAodlJr0vRSporV0Q5c; __ac_nonce=065ebe15f0055b11f1505; stream_recommend_feed_params=%22%7B%5C%22cookie_enabled%5C%22%3Atrue%2C%5C%22screen_width%5C%22%3A1920%2C%5C%22screen_height%5C%22%3A1080%2C%5C%22browser_online%5C%22%3Atrue%2C%5C%22cpu_core_num%5C%22%3A8%2C%5C%22device_memory%5C%22%3A8%2C%5C%22downlink%5C%22%3A10%2C%5C%22effective_type%5C%22%3A%5C%224g%5C%22%2C%5C%22round_trip_time%5C%22%3A50%7D%22; xg_device_score=7.3427345677051115; stream_player_status_params=%22%7B%5C%22is_auto_play%5C%22%3A0%2C%5C%22is_full_screen%5C%22%3A0%2C%5C%22is_full_webscreen%5C%22%3A0%2C%5C%22is_mute%5C%22%3A1%2C%5C%22is_speed%5C%22%3A1%2C%5C%22is_visible%5C%22%3A0%7D%22; passport_assist_user=CkFs_D0QvDy5KLYA0CUBH8PeHSEYg96gt8HTANIFqRYdxz-4HxOlPwLmqoIkTHg5emcQvdirgoulL-L94Y_jBKC0dBpKCjzfyYc3DvRN9PnUEgT5neU02j2Dorj8JvtiKfhgS0evAwuSFCXO8k39SdKGz21nZCYRkECODxbZ0LV2U2cQhrjLDRiJr9ZUIAEiAQNYxC0E; n_mh=XFBc0LpEzHCfYx5Ouxe_1FGaFhbJIkYdGUcgpBVduXw; sso_uid_tt=590cead3f5cff46dd242c5b944a0fe9b; sso_uid_tt_ss=590cead3f5cff46dd242c5b944a0fe9b; toutiao_sso_user=4f2dd29912d4b930cb8e255abc46ad23; toutiao_sso_user_ss=4f2dd29912d4b930cb8e255abc46ad23; sid_ucp_sso_v1=1.0.0-KDAyMTQ0MjI1YTU4ZDdkYTBkODhmNTE3ZTkwNzMxZTc4NGVkODFjNDEKHwiul6Ddr42pAxDKxq-vBhjvMSAMMPr0vpUGOAZA9AcaAmxxIiA0ZjJkZDI5OTEyZDRiOTMwY2I4ZTI1NWFiYzQ2YWQyMw; ssid_ucp_sso_v1=1.0.0-KDAyMTQ0MjI1YTU4ZDdkYTBkODhmNTE3ZTkwNzMxZTc4NGVkODFjNDEKHwiul6Ddr42pAxDKxq-vBhjvMSAMMPr0vpUGOAZA9AcaAmxxIiA0ZjJkZDI5OTEyZDRiOTMwY2I4ZTI1NWFiYzQ2YWQyMw; odin_tt=80e60ae4e2b033939646f684efb42343e1934734ca9cea9fc54acf87dd7a01becee85b867a9a47254599ba20cf33a8cc2a7952712ac8790db063de0a5521cf94; passport_auth_status=435f36cf960adc6e7f33bf7fa4d76366%2C51e2a69ee562075e04d5feb0048b4130; passport_auth_status_ss=435f36cf960adc6e7f33bf7fa4d76366%2C51e2a69ee562075e04d5feb0048b4130; uid_tt=861c6ac6aef41d4deceae7ef2ae23fa5; uid_tt_ss=861c6ac6aef41d4deceae7ef2ae23fa5; sid_tt=ee776d54eebdcc4d27fd4eea6a7f475a; sessionid=ee776d54eebdcc4d27fd4eea6a7f475a; sessionid_ss=ee776d54eebdcc4d27fd4eea6a7f475a; LOGIN_STATUS=1; msToken=JtgFMM-apxSy5O1kherW489fml6PdJecEqYAMMBMJA6AgTRGDoM-6Rn7kuReiwtI222N8WPH2vSkVjsGyVRkRDvIiyBVp7tXPNsn8LeGTWq3eDLvFo4=; _bd_ticket_crypt_cookie=e0d4b60e53ad200c8ae819675e7e84de; bd_ticket_guard_client_data=eyJiZC10aWNrZXQtZ3VhcmQtdmVyc2lvbiI6MiwiYmQtdGlja2V0LWd1YXJkLWl0ZXJhdGlvbi12ZXJzaW9uIjoxLCJiZC10aWNrZXQtZ3VhcmQtcmVlLXB1YmxpYy1rZXkiOiJCUG9kK044RU9EckFtdGRrZm9waGJSM2JPS1lDbjJLSDN2UFFpSHhIQlNVRnBQMjdlK3A1Y2V0SVJ5WGVXTG41WE4wOFNPN1BqL1RXNnBPSFZIYjhIakk9IiwiYmQtdGlja2V0LWd1YXJkLXdlYi12ZXJzaW9uIjoxfQ%3D%3D; sid_guard=ee776d54eebdcc4d27fd4eea6a7f475a%7C1709957966%7C5183999%7CWed%2C+08-May-2024+04%3A19%3A25+GMT; sid_ucp_v1=1.0.0-KDIzMzIwYmYyMTAzOWFiNTE1NWIzZGY1YzNmNmM5ZjZiMWEyNzRjMDUKGwiul6Ddr42pAxDOxq-vBhjvMSAMOAZA9AdIBBoCaGwiIGVlNzc2ZDU0ZWViZGNjNGQyN2ZkNGVlYTZhN2Y0NzVh; ssid_ucp_v1=1.0.0-KDIzMzIwYmYyMTAzOWFiNTE1NWIzZGY1YzNmNmM5ZjZiMWEyNzRjMDUKGwiul6Ddr42pAxDOxq-vBhjvMSAMOAZA9AdIBBoCaGwiIGVlNzc2ZDU0ZWViZGNjNGQyN2ZkNGVlYTZhN2Y0NzVh; msToken=dqSR7_JH6QEmTK-yhbxFqqz3K7A52XFjvjoScEz-aTUZ7CYPFJy14RiJZZsUrQSxRiYgFwKDIXESVy56NHcXx6PkOvX6gYuXTk_c3P-DX7jQ0nRo5rI=; FOLLOW_NUMBER_YELLOW_POINT_INFO=%22MS4wLjABAAAABpiZ3d1HtcvYHvnZQ6Kke_2iTMBROJYpqmlz8x1mopQ4tDHrj6vQ_4QhUX1waRl4%2F1710000000000%2F0%2F1709957970190%2F0%22; tt_scid=t4r9tD-qqNv1yEuZyV.lRVIeKUygU-oBqt6V0d-NuNPZb7BdXq5emtaps08zfWYQ64cd; passport_fe_beating_status=false; IsDouyinActive=true; home_can_add_dy_2_desktop=%220%22',
            'pragma': 'no-cache',
            'referer': 'https://www.douyin.com/user/MS4wLjABAAAAcMKl7JekBXRprjAc9nT8EFEvSzgK_qfToMmfnnPCHQc',
            'sec-ch-ua': '"Chromium";v="122", "Not(A:Brand";v="24", "Google Chrome";v="122"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36',
        }
        return headers

    def def_execjs(self):
        with open("x_b.js") as f:
            js_data = f.read()
        js_compile = execjs.compile(js_data)
        return js_compile
    def get_count(self, next='max_cursor=0'):
        url = "https://www.douyin.com/aweme/v1/web/aweme/post/?"
        sec_user_id = 'MS4wLjABAAAAcMKl7JekBXRprjAc9nT8EFEvSzgK_qfToMmfnnPCHQc'
        params = f'device_platform=webapp&aid=6383&channel=channel_pc_web&sec_user_id={sec_user_id}&{next}&locate_query=false&show_live_replay_strategy=1&need_time_list=1&time_list_query=0&whale_cut_token=&cut_version=1&count=18&publish_video_strategy_type=2&pc_client_type=1&version_code=170400&version_name=17.4.0&cookie_enabled=true&screen_width=1707&screen_height=1067&browser_language=zh-CN&browser_platform=Win32&browser_name=Chrome&browser_version=119.0.0.0&browser_online=true&engine_name=Blink&engine_version=119.0.0.0&os_name=Windows&os_version=10&cpu_core_num=16&device_memory=8&platform=PC&downlink=7.9&effective_type=4g&round_trip_time=50&webid=7310230678028846631&msToken=XWdh8ZPfrgSs9QombFXY3DJxXhH3HTyjw7NtYb6tpW9wYpaZqIAuhcZmOtQBu-7qgnSFswVdEZ2cKWsg6A4_WkxwyxIH3CCuMoLOUh4H6iqGBk7-ba8jaBufrmt2jw=='
        print(f'正在打印{next}')
        xb_data = self.def_execjs().call("get_dy_xb", params)
        urls = url + params + "&X-Bogus=" + xb_data
        # print(urls)
        response = requests.get(url=urls, headers=self.def_headers()).json()
        if response['max_cursor'] != 0:
            max_cursor = response['max_cursor']
            max_id = 'max_cursor=' + str(max_cursor)  # 这个递归返回
            for data_list in response['aweme_list']:
                if data_list['images']!=None:
                    for i in data_list['images']:#图文
                        desc = data_list['desc']
                        title = re.sub(r'[\/.*":?<>|\n]', '', desc)
                        url_list = i['url_list'][0]
                        dict = {'title': title, 'url_list': [url_list], 'sec_user_id': sec_user_id}
                        print(dict)
                    List_video().get_count(max_id)
                else:
                    desc = data_list['desc'] #视频
                    title = re.sub(r'[\/.*":?<>|\n]', '', desc)
                    url_list = data_list['video']['play_addr']['url_list'][0]
                    dict = {'title': title, 'url_list': url_list, 'sec_user_id': sec_user_id}
                    print(dict)
            List_video().get_count(max_id)
        else:
            response['max_cursor'] = 0
            print('结束')
if __name__=='__main__':
    # for aweme_id in Read_sql().def_sql():
    #     aweme_id_s = aweme_id['id']
    #     print(aweme_id_s)
     List_video().get_count()