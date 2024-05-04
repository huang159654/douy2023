#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# @当前时间 :2024/2/23 15:28
# @Author  : TS
# @Email   : TS@gmail.com
# @File    : ts2.py
# @Software: PyCharm
"""
import json
import os
import re
import urllib.parse

import execjs
import requests


class DY_Personal_list_video():#视频下载
    def __init__(self):
        if not os.path.exists('../video'):
            os.mkdir('../video')
    def def_headers(self):
        headers = {
            'authority': 'www.douyin.com',
            'accept': 'application/json, text/plain, */*',
            'accept-language': 'zh-CN,zh;q=0.9',
            'cache-control': 'no-cache',
            'cookie': 's_v_web_id=verify_lqmvn9pl_5bBUs5Dp_Y2xv_4bzn_8p3u_tycDOYXCGcjm; passport_csrf_token=e9e5a6feab6c80ed7b35fe7ac03db4d1; passport_csrf_token_default=e9e5a6feab6c80ed7b35fe7ac03db4d1; bd_ticket_guard_client_web_domain=2; passport_assist_user=CkHnMSDW_cBlzgmetlUMer5M2uwjk3VDJCh5pHXgZJCcufgdXlZB4dq-pJccLGx5y_TmvV4FekfsNz5Zzpjox_dvyRpKCjwuKNRGKmg1v6M9VmV3iwrvewPHmpQGV5adilWTIxKDmpXC-EoBAPkcWVDBdVRAGqUyEGbst-NQ-A7Q8rQQi4HFDRiJr9ZUIAEiAQNLfC5S; n_mh=XFBc0LpEzHCfYx5Ouxe_1FGaFhbJIkYdGUcgpBVduXw; sso_uid_tt=651c878dbe66cbe1447c4ceac7f82b8c; sso_uid_tt_ss=651c878dbe66cbe1447c4ceac7f82b8c; toutiao_sso_user=d5b3ffa80e5eead1a3f9f9ebf6da77d3; toutiao_sso_user_ss=d5b3ffa80e5eead1a3f9f9ebf6da77d3; LOGIN_STATUS=1; _bd_ticket_crypt_doamin=2; _bd_ticket_crypt_cookie=59f5c51dffb9dcb48478499df50292d7; __security_server_data_status=1; store-region=cn-fj; store-region-src=uid; live_use_vvc=%22false%22; xgplayer_user_id=235710559159; my_rd=2; ttwid=1%7CQnYzszOwlFXUjuLPdaaRwhmmoHtf5LMtB_o57eVgfso%7C1705213591%7C7a4dc85add904fb99ba74c70222b6fef99c6b7bc4f32d0c859f2248ab27cc0e1; sid_ucp_sso_v1=1.0.0-KGUwMTM0MjZhYjFlOGQ2NGMwMDEzMWNmMDg3NDE1ODU0MzMzNWUyMmQKHwiul6Ddr42pAxD8stOtBhjvMSAMMPr0vpUGOAZA9AcaAmxxIiBkNWIzZmZhODBlNWVlYWQxYTNmOWY5ZWJmNmRhNzdkMw; ssid_ucp_sso_v1=1.0.0-KGUwMTM0MjZhYjFlOGQ2NGMwMDEzMWNmMDg3NDE1ODU0MzMzNWUyMmQKHwiul6Ddr42pAxD8stOtBhjvMSAMMPr0vpUGOAZA9AcaAmxxIiBkNWIzZmZhODBlNWVlYWQxYTNmOWY5ZWJmNmRhNzdkMw; sid_guard=002c187fbb005f16b45326c0dc4aaf10%7C1706350972%7C5184000%7CWed%2C+27-Mar-2024+10%3A22%3A52+GMT; uid_tt=e857bf5d3d1b1e24a3d7deed6ccd51a9; uid_tt_ss=e857bf5d3d1b1e24a3d7deed6ccd51a9; sid_tt=002c187fbb005f16b45326c0dc4aaf10; sessionid=002c187fbb005f16b45326c0dc4aaf10; sessionid_ss=002c187fbb005f16b45326c0dc4aaf10; sid_ucp_v1=1.0.0-KDgzNGQ4Y2JkYjU0MGZjY2E0YTdjZjg3MjAwZTZlOGY2MDllMWQzZjAKGwiul6Ddr42pAxD8stOtBhjvMSAMOAZA9AdIBBoCbHEiIDAwMmMxODdmYmIwMDVmMTZiNDUzMjZjMGRjNGFhZjEw; ssid_ucp_v1=1.0.0-KDgzNGQ4Y2JkYjU0MGZjY2E0YTdjZjg3MjAwZTZlOGY2MDllMWQzZjAKGwiul6Ddr42pAxD8stOtBhjvMSAMOAZA9AdIBBoCbHEiIDAwMmMxODdmYmIwMDVmMTZiNDUzMjZjMGRjNGFhZjEw; __live_version__=%221.1.1.7489%22; douyin.com; device_web_cpu_core=8; device_web_memory_size=8; architecture=amd64; csrf_session_id=11fdc2e040844afa16efae0603b483bb; passport_fe_beating_status=true; publish_badge_show_info=%220%2C0%2C0%2C1708670595518%22; dy_swidth=1920; dy_sheight=1080; FOLLOW_NUMBER_YELLOW_POINT_INFO=%22MS4wLjABAAAABpiZ3d1HtcvYHvnZQ6Kke_2iTMBROJYpqmlz8x1mopQ4tDHrj6vQ_4QhUX1waRl4%2F1708704000000%2F0%2F1708670597290%2F0%22; strategyABtestKey=%221708670598.544%22; volume_info=%7B%22isUserMute%22%3Afalse%2C%22isMute%22%3Atrue%2C%22volume%22%3A0.991%7D; FRIEND_NUMBER_RED_POINT_INFO=%22MS4wLjABAAAABpiZ3d1HtcvYHvnZQ6Kke_2iTMBROJYpqmlz8x1mopQ4tDHrj6vQ_4QhUX1waRl4%2F1708704000000%2F1708670606804%2F0%2F0%22; FOLLOW_LIVE_POINT_INFO=%22MS4wLjABAAAABpiZ3d1HtcvYHvnZQ6Kke_2iTMBROJYpqmlz8x1mopQ4tDHrj6vQ_4QhUX1waRl4%2F1708704000000%2F1708670610192%2F1708670607286%2F0%22; xg_device_score=7.374006370221997; stream_player_status_params=%22%7B%5C%22is_auto_play%5C%22%3A0%2C%5C%22is_full_screen%5C%22%3A0%2C%5C%22is_full_webscreen%5C%22%3A0%2C%5C%22is_mute%5C%22%3A1%2C%5C%22is_speed%5C%22%3A1%2C%5C%22is_visible%5C%22%3A0%7D%22; pwa2=%220%7C0%7C3%7C0%22; __ac_nonce=065d847e20049c22ed3d; __ac_signature=_02B4Z6wo00f01RYVdyAAAIDCK7xtvHON4A0WNXOAACBfoQrApCozSnr73r4DnQyrGI3p8SbYLc4C9eCXCSBIw9X6w69JKWpiluY95PzXuOzej5ERvl6K3ybWPO7cGzGZlCffjKd5RgAvSHu6d7; stream_recommend_feed_params=%22%7B%5C%22cookie_enabled%5C%22%3Atrue%2C%5C%22screen_width%5C%22%3A1920%2C%5C%22screen_height%5C%22%3A1080%2C%5C%22browser_online%5C%22%3Atrue%2C%5C%22cpu_core_num%5C%22%3A8%2C%5C%22device_memory%5C%22%3A8%2C%5C%22downlink%5C%22%3A10%2C%5C%22effective_type%5C%22%3A%5C%224g%5C%22%2C%5C%22round_trip_time%5C%22%3A100%7D%22; odin_tt=29dfd5b2864a17bc5ffb64fca419cf38bfaf7e3d45eb8cf19b853f5589b1c4e387ae30dcb0b857a7c402eda15dea5398; msToken=Pid3sZXWU50nTRLUjwsMXmhfgQrL3wdMIvhLWIgg2D8bFxdIC6xh4zYGk07kg9JJe0Nd8vy3wx8jxroVqV319GwGamLOBXY6fng7sN5nMP-rAW818DjWwBE28AeFGg==; IsDouyinActive=true; home_can_add_dy_2_desktop=%220%22; msToken=qKzGuMG2aMn72-RVihaSeUxtcLQuy_YpGI0Oh77M6bjm2bth8xI3jK9hCUOIY3RtL3viP_FronC-u8DIs4Ky0YEKnYEK9_v04uRcyZobMJHjGN0qEDdqhkSp3BZSqw==; download_guide=%222%2F20240223%2F0%22; bd_ticket_guard_client_data=eyJiZC10aWNrZXQtZ3VhcmQtdmVyc2lvbiI6MiwiYmQtdGlja2V0LWd1YXJkLWl0ZXJhdGlvbi12ZXJzaW9uIjoxLCJiZC10aWNrZXQtZ3VhcmQtcmVlLXB1YmxpYy1rZXkiOiJCUG9kK044RU9EckFtdGRrZm9waGJSM2JPS1lDbjJLSDN2UFFpSHhIQlNVRnBQMjdlK3A1Y2V0SVJ5WGVXTG41WE4wOFNPN1BqL1RXNnBPSFZIYjhIakk9IiwiYmQtdGlja2V0LWd1YXJkLXdlYi12ZXJzaW9uIjoxfQ%3D%3D; tt_scid=SrMzPtPXIwb250GAXmbAiyoIv-r-4UX1klRmXPhEDcD5N1HOlQNcJgeGV8n3RFwma159',
            'pragma': 'no-cache',
            'referer': 'https://www.douyin.com/user/MS4wLjABAAAAO-muWgmkr6oqYpuB4wwWOUAQphaHalk0aI7Y7eZcZhU',
            'sec-ch-ua': '"Not A(Brand";v="99", "Google Chrome";v="121", "Chromium";v="121"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36',
        }
        return headers

    def def_execjs(self):
        with open("x_b.js") as f:
            js_data = f.read()
        js_compile =execjs.compile(js_data)
        return js_compile
    def get_count(self,next='max_cursor=0'):
        url = "https://www.douyin.com/aweme/v1/web/aweme/post/?"
        params =f'device_platform=webapp&aid=6383&channel=channel_pc_web&sec_user_id=MS4wLjABAAAAJK1h8PSZ3ycKVMm9jskMPVkI4VNyaCwlk09oP6umerE&{next}&locate_query=false&show_live_replay_strategy=1&need_time_list=1&time_list_query=0&whale_cut_token=&cut_version=1&count=18&publish_video_strategy_type=2&pc_client_type=1&version_code=170400&version_name=17.4.0&cookie_enabled=true&screen_width=1707&screen_height=1067&browser_language=zh-CN&browser_platform=Win32&browser_name=Chrome&browser_version=119.0.0.0&browser_online=true&engine_name=Blink&engine_version=119.0.0.0&os_name=Windows&os_version=10&cpu_core_num=16&device_memory=8&platform=PC&downlink=7.9&effective_type=4g&round_trip_time=50&webid=7310230678028846631&msToken=XWdh8ZPfrgSs9QombFXY3DJxXhH3HTyjw7NtYb6tpW9wYpaZqIAuhcZmOtQBu-7qgnSFswVdEZ2cKWsg6A4_WkxwyxIH3CCuMoLOUh4H6iqGBk7-ba8jaBufrmt2jw=='
        xb_data =self.def_execjs().call("get_dy_xb",params)
        urls = url +params + "&X-Bogus=" + xb_data
        response = requests.get(url=urls,headers=self.def_headers()).json()
        if response['max_cursor']!=0:
            max_cursor=response['max_cursor']
            max_id = 'max_cursor=' + str(max_cursor)  # 这个递归返回
            print(max_id)
            for data_list in response['aweme_list']:
                desc = data_list['desc']
                title = re.sub(r'[\/.*":?<>|\n]', '', desc)
                url_list = data_list['video']['play_addr']['url_list'][0]
                print('正在下载>>>>>>>>>>>>>>', title)
                video_content = requests.get(url=url_list, headers=self.def_headers()).content
                with open('video\\' + title + '.mp4', mode='wb') as f:
                    # 写入数据
                    f.write(video_content)
            DY_Personal_list_video().get_count(max_id)
        else:
            response['max_cursor']=0
            print('结束')




if __name__=='__main__':
    DY_Personal_list_video().get_count()
