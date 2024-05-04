#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# @当前时间 :2024/2/25 12:37
# @Author  : TS
# @Email   : TS@gmail.com
# @File    : ts2.py
# @Software: PyCharm
"""
import json
import os
import random
import time
import execjs
import pandas as pd
import requests
from DY_Read import Read_csv
from DY_xlsx import Xlsx
from DY_xlsx import Xlsx_video
class Multiple_comment():#多个评论采集保存sql
    def __init__(self):
        pass
    def def_headers(self):
        with open('package.json', mode='r', encoding='utf-8')as f:
            json_data=json.load(f)
            headers=json_data['ALL_headers']
            return headers
    def def_execjs(self):
        with open("x_b.js") as f:
            js_data = f.read()
        js_compile =execjs.compile(js_data)
        return js_compile

    def def_url(self):
        url = "https://www.douyin.com/aweme/v1/web/comment/list/?"
        return url
    def def_params(self,awemes_id=None,cursor=None):
        params = f'device_platform=webapp&aid=6383&channel=channel_pc_web&aweme_id={awemes_id}&cursor={cursor}&count=20&item_type=0&whale_cut_token=&cut_version=1&rcFT=&pc_client_type=1&version_code=170400&version_name=17.4.0&cookie_enabled=true&screen_width=1920&screen_height=1080&browser_language=zh-CN&browser_platform=Win32&browser_name=Chrome&browser_version=121.0.0.0&browser_online=true&engine_name=Blink&engine_version=121.0.0.0&os_name=Windows&os_version=10&cpu_core_num=8&device_memory=8&platform=PC&downlink=10&effective_type=4g&round_trip_time=50&webid=7317023263425775145&msToken=Y5ky0EBdSM1YZp3j_FDy6Kj-n3ax6dWWhVLvV9m008gWBhQKjBiKCNFKCaqmjKFW9dLqT92HiD56pJNsNm7TU-PqDMlxCe-y2k5VrcGxvlCndLCeFTiD-Lflzb4COg=='
        return params

    def def_csv_id(self):
        for id in Read_csv().def_csv():
            dict={'awemes_id':id['id']}
            yield dict
    def def_xb(self,):
        for awemes_i in self.def_csv_id():
            awemes_id=awemes_i['awemes_id']
            xb_data = self.def_execjs().call("get_dy_xb", self.def_params(awemes_id=awemes_id))
            urls = self.def_url() + self.def_params(awemes_id=awemes_id) + "&X-Bogus=" + xb_data
            response = requests.get(url=urls, headers=self.def_headers()).json()
            if response['comments'] != None:
                total = response['total']
                # dai = total / 20
                # tota_l = math.ceil(dai)
                dict={'awemes_id':awemes_id,'tota_l':total}
                # print(dict)
                yield dict
            else:
                response['comments'] = None
                with open('评论url错误链接.txt', mode='a', ) as f:
                    url = 'https://www.douyin.com/video/' + awemes_id
                    txt = url + '\n'  # 数据分行
                    f.write(txt)
    def def_requests(self, ):
        for cursor_sa in self.def_xb():
            awemes_id=cursor_sa['awemes_id']
            for cursor in range(0, cursor_sa['tota_l'],20):
                data = self.def_params(awemes_id=awemes_id, cursor=cursor)
                print('Flipping pages, please wait!')
                xb_data = self.def_execjs().call("get_dy_xb", data)
                urls = self.def_url() + data + "&X-Bogus=" + xb_data
                response = requests.get(url=urls, headers=self.def_headers()).json()
                # print(response['comments'])
                randoms = random.randint(5, 15)
                time.sleep(randoms)
                if response['comments'] is None:
                    print("字典中'comments'对应的值为None")
                    break
                else:
                    yield response


    def def_parse(self, ):  # 解析数据
        for data_list in self.def_requests():
            try:
                for data in data_list['comments']:
                    nickname = data.get('user').get('nickname')  # 用户昵称
                    sec_uid = data.get('user').get('sec_uid')  # 用户详情页id
                    short_id = data.get('user').get('short_id')  # 用户抖音号
                    text_s = data.get('text')  # 评论文本
                    create = data.get('create_time')  # 发布时间
                    timeArray = time.localtime(create)
                    create_time = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)  # 发布时间
                    ip_label = data.get('ip_label')  # ip地址
                    reply_comment_total = data.get('reply_comment_total')  # 回复数
                    cid = data.get('cid')  # 主键id
                    aweme_id = data.get('aweme_id')  # 视频id
                    aweme_url = 'https://www.douyin.com/video/' + aweme_id  # 视频链接
                    dict = [{'视频id': aweme_id, 'cid': cid, '用户昵称': nickname, '用户详情页id': sec_uid,
                             '用户抖音号': short_id,
                             '评论文本': text_s, '发布时间': create_time, '用户ip地址': ip_label,
                             '用户评论回复数': reply_comment_total,
                             '视频链接': aweme_url}]
                    # print(dict)
                    yield dict
            except :
                 continue

    def def_csv(self):#保存csv
        for data in self.def_parse():
            dataframe = pd.DataFrame(data)
            if not os.path.exists('抖音评论.csv'):
                dataframe.to_csv('./抖音评论.csv', mode='a',encoding='utf_8_sig',index=False, )
            dataframe.to_csv('./抖音评论.csv', mode='a',encoding='utf_8_sig', header=False, index=False)
            # current_time = datetime.datetime.now()
            print('Comment collection completed')#评论采集完毕
            df = pd.read_csv('抖音评论.csv')
            # 删除重复项
            df = df.drop_duplicates()
            # 保存修改后的DataFrame对象到新的CSV文件
            df.to_csv('抖音评论.csv', index=False)

    def def_main(self):
        menum = """
                                ===================================抖音评论采集=========================================
                                A。读取xlsx 文件中https://v.douyin.com/iKeD74w/链接
                                ----------------------------------------------------
                                B。读取xlsx 文件中https://www.douyin.com/video/7312743380214238498链接
                                ----------------------------------------------------
                                Q。结束选择文件操作
                               =====================================================================================
                                        """
        print(menum)
        while 1:
            menum = input('请选择你要保存的文件>>>>>>')
            if menum.upper() == 'A':
                Xlsx().def_csv()
                Multiple_comment().def_csv()
            elif menum.upper() == 'B':
                Xlsx_video().def_csv()
                Multiple_comment().def_csv()
            elif menum.upper() == 'Q':
                print("""==================结束程序=================""")
                break

if __name__=='__main__':
    Multiple_comment().def_main()

