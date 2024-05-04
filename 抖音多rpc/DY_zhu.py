#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# @当前时间 :2023/11/7 23:41
# @Author  : TS
# @Email   : TS@gmail.com
# @File    : ts2.py
# @Software: PyCharm
"""
import re
from DY_comments import D_pl
from DY_user_videos import DY_parse
from DY_video_detailed import Parse
from DY_Video_search import D_reques
from DY_Video_thumbs import D_requess
from DY_Personal_details import DY_parses
from DY_single_video import DY_single
class DY_host():
    menum_1 = """
                        
                        |================抖音信息============|
                        |       A.评论信息                   |
                        |-----------------------------------|
                        |       B.视频点赞                   |   
                        |-----------------------------------|
                        |       C.搜索最新视频                |   
                        |-----------------------------------|   
                        |       D.搜索视频点赞                | 
                        |-----------------------------------|         
                        |       E.个人视频列表                |  
                        |-----------------------------------|  
                        |       F.用户详细信息                |  
                        |-----------------------------------|  
                        |       g.单个视频                |  
                        |-----------------------------------| 
                        |       Q.退出                       |
                        |===================================|
                        """
    print(menum_1)
    while 1:
        num_2 = input('Q.退出程序)>>>')
        if num_2.upper() == 'A':
            menum_1 = """
                        |================抖音信息==================|
                        |       输入提示 7295734255374617910       |
                        |-----------------------------------------|
                        |       5.      返回主页面                 |
                        |===================END==================|
                        """
            print(menum_1)
            while 1:
                awem_id = input('请输入视频id:')
                if awem_id == '5':
                    break
                elif re.match(r'[a-zA-Z\_]', awem_id) or re.match(r'^[@_!#$%^&*()<>?/\|}{~:+,-;=.。、]$',
                                                                  awem_id) or re.match(r'^[0-9]+\.[0-9]+$',
                                                                                       awem_id) or re.match(
                    r'^\s*$', awem_id) or len(awem_id) < 19 or re.match(r'^\s*$', awem_id) or len(awem_id) > 19:
                    print('请输入正确的视频id')
                elif D_pl().def_pagination(awem_id):
                    print('正在执行')
                # elif awem_id=='5':
                #     break
                else:
                    print('input error')
        elif num_2.upper() == 'B':
            menum_1 = """
                                    |================抖音信息==================|
                                    |       输入提示 7295734255374617910       |
                                    |-----------------------------------------|
                                    |       5.      返回主页面                 |
                                    |===================END==================|
                                    """
            print(menum_1)
            while 1:
                awem_id = input('请输入id:')
                if awem_id == '5':
                    break
                elif re.match(r'[a-zA-Z\_]', awem_id) or re.match(r'^[@_!#$%^&*()<>?/\|}{~:+,-;=.。、]$',
                                                                  awem_id) or re.match(r'^[0-9]+\.[0-9]+$',
                                                                                       awem_id) or re.match(
                        r'^\s*$', awem_id) or len(awem_id) < 19 or re.match(
                    r'^\s*$', awem_id) or len(awem_id) > 19:
                    print('请输入正确的视频id!')
                elif Parse().def_parse(awem_id):
                    print('正在执行')
                    # elif awem_id=='5':
                    #     break
                else:
                    print('input error')
        elif num_2.upper() == 'C':
            menum_1 = """
                                    |================抖音信息==================|
                                    |       输入提示    中文                    |
                                    |-----------------------------------------|
                                    |       5.      返回主页面                 |
                                    |===================END==================|
                                    """
            print(menum_1)
            while 1:
                keyword = input('请输入你要搜索的关键字:')
                if awem_id == '5':
                    break
                elif re.match(r'[0-9]+$', keyword) or re.match(r'^[@_!#$%^&*()<>?/\|}{~:+,-;=.。、]$',
                                                               keyword) or re.match(r'^[0-9]+\.[0-9]+$',
                                                                                    keyword) or re.match(
                        r'[0-9a-zA-Z\_]', keyword) or re.match(r'^\s*$', keyword):
                    print("请输入中文!")
                elif D_reques().def_request(keyword):
                    print('正在执行')
                else:
                    print('input error')
        elif num_2.upper() == 'D':
            menum_1 = """
                                    |================抖音信息==================|
                                    |       输入提示    中文                    |
                                    |-----------------------------------------|
                                    |       5.      返回主页面                 |
                                    |===================END==================|
                                    """
            print(menum_1)
            while 1:
                keyword = input('请输入你要搜索的关键字:')
                if awem_id == '5':
                    break
                elif re.match(r'[0-9]+$', keyword) or re.match(r'^[@_!#$%^&*()<>?/\|}{~:+,-;=.。、]$',
                                                               keyword) or re.match(
                        r'^[0-9]+\.[0-9]+$', keyword) or re.match(r'[0-9a-zA-Z\_]', keyword) or re.match(r'^\s*$',
                                                                                                         keyword):
                    print("请输入中文!")

                elif D_requess().def_request(keyword):
                    print('正在执行')
                else:
                    print('input error')
        elif num_2.upper() == 'E':
            menum_1 = """
                                    |================抖音信息==================|
                                    |       输入提示  用户主页ID                |
                                    |-----------------------------------------|
                                    |       5.      返回主页面                 |
                                    |===================END==================|
                                    """
            print(menum_1)
            while 1:
                sec_user_id = input('请输入你要用户id:')
                if sec_user_id == '5':
                    break
                elif re.match(r'^\s*$',sec_user_id) or len(
                        sec_user_id) < 55 or re.match(r'^\s*$', sec_user_id) or len(sec_user_id) > 55:
                    print('请输入正确的个人id!')
                elif DY_parse().def_data(sec_user_id=sec_user_id):
                    print('正在执行')
                else:
                    print('input error')
        elif num_2.upper() == 'F':
            menum_1 = """
                                                |================抖音信息==================|
                                                |       输入提示  用户主页ID                |
                                                |-----------------------------------------|
                                                |       5.      返回主页面                 |
                                                |===================END==================|
                                                """
            print(menum_1)
            while 1:
                sec_user_id = input('请输入你要用户id:')
                if sec_user_id == '5':
                    break
                elif re.match(r'^[@_!#$%^&*()<>?/\|}{~:+,-;=.。、]$', sec_user_id) or re.match(r'^\s*$',sec_user_id):
                    print('请输入正确的个人id!')
                elif DY_parses().def_response(sec_user_id):
                    print('正在执行')
                    # elif awem_id=='5':
                    #     break
                else:
                    print('input error')
        elif num_2.upper() == 'G':
            menum_1 = """
                                                |================抖音信息==================|
                                                |       输入提示  7271959364527803684      |
                                                |-----------------------------------------|
                                                |       5.      返回主页面                 |
                                                |===================END==================|
                                                """
            print(menum_1)
            while 1:
                awem_id = input('请输入你要用户id:')
                if awem_id == '5':
                    break
                elif re.match(r'[a-zA-Z\_]', awem_id) or re.match(r'^[@_!#$%^&*()<>?/\|}{~:+,-;=.。、]$',awem_id) or re.match(r'^[0-9]+\.[0-9]+$',awem_id) or re.match(
                        r'^\s*$', awem_id) or len(awem_id) < 19 or re.match(
                    r'^\s*$', awem_id) or len(awem_id) > 19:
                    print('请输入正确的个人id!')
                elif DY_single().def_Dxb_assembly(aweme_id=awem_id):
                    print('正在执行')
                else:
                    print('input error')
        elif num_2.upper() == 'Q':
            print("""==================结束本次操作=================""")
            break

if __name__ == '__main__':
    DY_host()
