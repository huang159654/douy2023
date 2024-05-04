#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# @当前时间 :2023/11/25 23:59
# @Author  : TS
# @Email   : TS@gmail.com
# @File    : ts2.py
# @Software: PyCharm
"""
import json
import os
import time
import urllib.parse
from tqdm import tqdm
import requests

from DY_Dresponse import DY_core
class DY_single:#单个视频
    def __init__(self):
        self.headers = {
            'authority': 'www.douyin.com',
            'accept': 'application/json, text/plain, */*',
            'accept-language': 'zh-CN,zh;q=0.9',
            'cache-control': 'no-cache',
            'cookie': 'passport_csrf_token=94c2fa9039be7daff5296b4b2b6f09a3; passport_csrf_token_default=94c2fa9039be7daff5296b4b2b6f09a3; s_v_web_id=verify_loslii64_LM25LdN7_afQV_4ycJ_8zwq_cB6tRX75NJhe; download_guide=%223%2F20231110%2F1%22; FORCE_LOGIN=%7B%22videoConsumedRemainSeconds%22%3A180%2C%22isForcePopClose%22%3A1%7D; n_mh=MPHRKGEs6Mdv8j9-lYQ_xItbJLeVCy02zT61y_-m6jI; _bd_ticket_crypt_doamin=2; __security_server_data_status=1; store-region=cn-fj; store-region-src=uid; live_use_vvc=%22false%22; my_rd=2; xgplayer_user_id=84844123561; pwa2=%220%7C0%7C3%7C1%22; SEARCH_RESULT_LIST_TYPE=%22single%22; douyin.com; device_web_cpu_core=8; device_web_memory_size=8; architecture=amd64; webcast_local_quality=null; csrf_session_id=90a90aaa7707b23918a293cb6e2059ee; VIDEO_FILTER_MEMO_SELECT=%7B%22expireTime%22%3A1701266743654%2C%22type%22%3A1%7D; dy_swidth=1536; dy_sheight=864; bd_ticket_guard_client_web_domain=2; strategyABtestKey=%221700896590.264%22; toutiao_sso_user=fd6251a8ae525a7ded89ee0203680067; toutiao_sso_user_ss=fd6251a8ae525a7ded89ee0203680067; passport_auth_status=3e384b8a7477412e04c590b7745fb87c%2C550f1567e80b273498d07a8b0039732b; passport_auth_status_ss=3e384b8a7477412e04c590b7745fb87c%2C550f1567e80b273498d07a8b0039732b; _bd_ticket_crypt_cookie=eee97678c9b6557ae009731be481ea6d; publish_badge_show_info=%220%2C0%2C0%2C1700907774769%22; __live_version__=%221.1.1.5721%22; webcast_leading_last_show_time=1700907784317; webcast_leading_total_show_times=1; live_can_add_dy_2_desktop=%221%22; volume_info=%7B%22isUserMute%22%3Afalse%2C%22isMute%22%3Afalse%2C%22volume%22%3A0.867%7D; FOLLOW_NUMBER_YELLOW_POINT_INFO=%22MS4wLjABAAAABOhvAjIm3vns-R1X1jh5dt-kQ5s_ihMeO9UG_JpkDRw%2F1700928000000%2F0%2F1700919965502%2F0%22; stream_player_status_params=%22%7B%5C%22is_auto_play%5C%22%3A0%2C%5C%22is_full_screen%5C%22%3A0%2C%5C%22is_full_webscreen%5C%22%3A0%2C%5C%22is_mute%5C%22%3A0%2C%5C%22is_speed%5C%22%3A1%2C%5C%22is_visible%5C%22%3A0%7D%22; FOLLOW_LIVE_POINT_INFO=%22MS4wLjABAAAABOhvAjIm3vns-R1X1jh5dt-kQ5s_ihMeO9UG_JpkDRw%2F1700928000000%2F1700907778289%2F1700920757032%2F0%22; ttwid=1%7CJvG9DofnLgc-E1muZscZpLg0qTWJ6EbQrc_bt2vK0l4%7C1700921347%7C345dc0791223acf8d844ae79158d363e94dd7cbc6f72d1b28395871ab05df65b; LOGIN_STATUS=0; sso_uid_tt=90944c8a15c00757e7aab751b4801788; sso_uid_tt_ss=90944c8a15c00757e7aab751b4801788; sid_ucp_sso_v1=1.0.0-KDkxOTAyMjRjZWIzNDdmMzcxZDFkNTNlZTUxYmZkMzhkN2E1ZjFlZTgKCRCFhIirBhjvMRoCaGwiIGZkNjI1MWE4YWU1MjVhN2RlZDg5ZWUwMjAzNjgwMDY3; ssid_ucp_sso_v1=1.0.0-KDkxOTAyMjRjZWIzNDdmMzcxZDFkNTNlZTUxYmZkMzhkN2E1ZjFlZTgKCRCFhIirBhjvMRoCaGwiIGZkNjI1MWE4YWU1MjVhN2RlZDg5ZWUwMjAzNjgwMDY3; odin_tt=a05bc5252c83dc76452a9b78f92cedbc9cfa6e57cbfb8615275f30c539b2b3a2; sid_guard=c61ceb77f2cb75a37a79476b756b7456%7C1700921861%7C21600%7CSat%2C+25-Nov-2023+20%3A17%3A41+GMT; uid_tt=7d05f4a228ac5e59bc8c39ec988c7e97; uid_tt_ss=7d05f4a228ac5e59bc8c39ec988c7e97; sid_tt=c61ceb77f2cb75a37a79476b756b7456; sessionid=c61ceb77f2cb75a37a79476b756b7456; sessionid_ss=c61ceb77f2cb75a37a79476b756b7456; sid_ucp_v1=1.0.0-KDM3Nzk1N2U1YzViNTNjNDEyMTYxNTQyYWM5MzBkMmIxOGIzOTA4YmEKCBCFhIirBhgNGgJscSIgYzYxY2ViNzdmMmNiNzVhMzdhNzk0NzZiNzU2Yjc0NTY; ssid_ucp_v1=1.0.0-KDM3Nzk1N2U1YzViNTNjNDEyMTYxNTQyYWM5MzBkMmIxOGIzOTA4YmEKCBCFhIirBhgNGgJscSIgYzYxY2ViNzdmMmNiNzVhMzdhNzk0NzZiNzU2Yjc0NTY; __ac_nonce=06562020e0099d9f473ae; __ac_signature=_02B4Z6wo00f01L7GcuwAAIDAPsSIruV3AAS-5nZAAErYMP5wqXcvz0wQZRRsOIn62IjIwYlhJ7ueYkc9Gkq8gEW29swdAV5.7NkCHpz0GVWqVnPYkGwfhQS0feMrM5HizXOS5pawViMBLPtaf8; bd_ticket_guard_client_data=eyJiZC10aWNrZXQtZ3VhcmQtdmVyc2lvbiI6MiwiYmQtdGlja2V0LWd1YXJkLWl0ZXJhdGlvbi12ZXJzaW9uIjoxLCJiZC10aWNrZXQtZ3VhcmQtcmVlLXB1YmxpYy1rZXkiOiJCRTcxWjQwUGxWK3ZqVkpWY0ZuYnlxNzdGR1Q3d0ZqUG9GZUdEVUVFdUdqQnlxSEhsQjJwYldQaXd2eU5NWmUvMWJKV3daUXVqRnlRWlVzM1ZXVUZBeWM9IiwiYmQtdGlja2V0LWd1YXJkLXdlYi12ZXJzaW9uIjoxfQ%3D%3D; msToken=cpwYBZFtHUEs3nURfCh5j0pqeuP97hFw63UU-GoirwMiYSbv9cvhqOFp5L8L88-WRMCQ7oDuGzPBD9yzu_Nhgbg00kVU-E8GYeRPVn4czw3OZbZMIAY=; msToken=wgQnz3CILWJjeX8u62Jpa9T2Kr_pDB8AO0pKy5kqLobQHPCjjzJRIm35CmsylABhTYta6g2FuUv8Ys8zfy_QJ-uHjQvKYBqVBUnyrD2XNjM1ACF_0bI=; tt_scid=fpEShCLf7-1oeO-375m3Wf8O2G5Akn7GTAAZSqN09OlkIBNRX1ekwhzotN35w4gE06d4; IsDouyinActive=false; home_can_add_dy_2_desktop=%220%22; stream_recommend_feed_params=%22%7B%5C%22cookie_enabled%5C%22%3Atrue%2C%5C%22screen_width%5C%22%3A1536%2C%5C%22screen_height%5C%22%3A864%2C%5C%22browser_online%5C%22%3Atrue%2C%5C%22cpu_core_num%5C%22%3A8%2C%5C%22device_memory%5C%22%3A8%2C%5C%22downlink%5C%22%3A10%2C%5C%22effective_type%5C%22%3A%5C%224g%5C%22%2C%5C%22round_trip_time%5C%22%3A0%7D%22',
            'pragma': 'no-cache',
            'referer': 'https://www.douyin.com/video/7221060204610309413',
            'sec-ch-ua': '"Google Chrome";v="119", "Chromium";v="119", "Not?A_Brand";v="24"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36',
        }
    def def_Dxb_assembly(self,aweme_id):#xb生成
        headers= DY_core().def_headers()
        queries = DY_core().def_queries(aweme_id)
        url = DY_core().def_url()
        self.def_D_headers(url=url,headers=headers,params=queries)

    def def_D_headers(self,url=None,headers=None,params=None):
        response = requests.get(url=url, params=params, headers=headers).json()
        self.def_DParse_data(data=response)
    def def_DParse_data(self,data=None):#解析数据
        list = []
        list_1 = []
        if data['aweme_detail']:
            desc = data['aweme_detail']['desc']
            video=data['aweme_detail']['video']['play_addr']['url_list'][0]
            list.append(desc)
            list_1.append(video)
        dict = {'视频标题': list, '视频url': list_1}
        # print(dict)
        self.def_Dsvcv(data=dict)
    def def_Dsvcv(self,data=None):
        if not os.path.exists('../video'):
            os.mkdir('../video')
        dict_vide = data['视频url']
        dict_titie = data['视频标题']
        for titie, video in zip(dict_titie, dict_vide):
            url_video = video
            url_titie = titie
            video_content = requests.get(url=url_video, headers=self.headers, stream=True).content
            print('正在下载', url_titie)
            with open('video\\' + url_titie + '.mp4', mode='wb') as f:
                # 写入数据
                f.write(video_content)

if __name__=='__main__':
    id=input('请输入你要下载的id:')
    DY_single().def_Dxb_assembly(aweme_id=id)
