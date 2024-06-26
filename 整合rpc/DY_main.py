#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# @当前时间 :2024/1/31 14:14
# @Author  : TS
# @Email   : TS@gmail.com
# @File    : ts2.py
# @Software: PyCharm
"""

from DY_xlsx import Xlsx
from DY_xlsx import Xlsx_video
from DY_ALL_Parse import Retweet_parse_list
from DY_ALL_Parse import Comments_parse_sql
class DY_main():
    def __init__(self):
        pass
    def def_host(self):
        menum = """
                        =======================抖音采集=======================
                                            A。点赞和转发
                        ----------------------------------------------------
                                            B。评论
                        ----------------------------------------------------
                                            Q。结束选择文件操作
                        ====================================================
                                """
        print(menum)
        while 1:
            menum = input('请选择你要保存的文件>>>>>>')
            if menum.upper() == 'A':
                menums = """
                        =======================采集保存文件=======================
                                            A。保存csv文件
                        ----------------------------------------------------
                                            B。保存sql文件
                        ----------------------------------------------------
                                            Q。结束选择文件操作
                        ====================================================
                
                        """
                print(menums)
                while 1:
                    menums = input('请选择你要保存的文件>>>>>>')
                    if menums.upper() == 'A':
                        menum_2 = """
                            ======================================csv转换URL========================================
                                 A。xlsx转换 https://v.douyin.com/iKeD74w/为csv文件
                            ---------------------------------------------------------------------------------------
                                 B。xlsx转换/video/7312743380214238498 为csv文件
                            ---------------------------------------------------------------------------------------
                                                Q。结束选择文件操作
                            =======================================================================================
                                    """
                        print(menum_2)
                        while 1:
                            menum_2 = input('请选择csv格式转换的url格式>>>>>>')
                            if menum_2.upper() == 'A':
                                Xlsx().def_csv()
                                Retweet_parse_list().def_csv()
                                menums_file = """
                                ====================采集完毕！>>>>是否继续采集>>>返回上一页=====================================
                                ======================================csv转换URL========================================
                                                 A。xlsx转换 https://v.douyin.com/iKeD74w/为csv文件
                                ---------------------------------------------------------------------------------------
                                                 B。xlsx转换/video/7312743380214238498 为csv文件
                                ---------------------------------------------------------------------------------------
                                                 Q。返回上一页
                                =======================================================================================
                                """
                                print(menums_file)
                            elif menum_2.upper() == 'B':
                                Xlsx_video().def_csv()
                                Retweet_parse_list().def_csv()
                                menums_file = """
                                                                ====================采集完毕！>>>>是否继续采集>>>返回上一页=====================================
                                                                ======================================csv转换URL========================================
                                                                                 A。xlsx转换 https://v.douyin.com/iKeD74w/为csv文件
                                                                ---------------------------------------------------------------------------------------
                                                                                 B。xlsx转换/video/7312743380214238498 为csv文件
                                                                ---------------------------------------------------------------------------------------
                                                                                 Q。返回上一页
                                                                =======================================================================================
                                                                """
                                print(menums_file)
                            elif menum_2.upper() == 'Q':
                                print("""==================结束操作>>>>>>>返回上一页=================""")
                                menums_file = """
                                                        =======================保存文件=======================
                                                                            A。保存csv文件
                                                        ----------------------------------------------------
                                                                            B。保存sql文件
                                                        ----------------------------------------------------
                                                                            Q。结束选择文件操作
                                                        ====================================================

                                                        """
                                print(menums_file)
                                break
                    elif menums.upper() == 'B': #sql数据
                        menum_2 = """
                                                    ======================================sql转换URL===========================================
                                                         A。xlsx转换 https://v.douyin.com/iKeD74w/ 为sql文件
                                                    ---------------------------------------------------------------------------------------
                                                         B。xlsx转换/video/7312743380214238498 为sql文件
                                                    ---------------------------------------------------------------------------------------
                                                         Q。结束选择文件操作
                                                    =======================================================================================
                                                            """
                        print(menum_2)
                        while 1:
                            menum_2 = input('请选择sql格式转换的url格式>>>>>>')
                            if menum_2.upper() == 'A':
                                Xlsx().def_sql_url()
                                Retweet_parse_list().sql_s()
                                menums_file = """
                                ====================采集完毕！>>>>是否继续采集>>>返回上一页=====================================
                                ======================================sql转换URL========================================
                                A。xlsx转换 https://v.douyin.com/iKeD74w/ 为sql文件
                                ---------------------------------------------------------------------------------------
                                B。xlsx转换/video/7312743380214238498 为sql文件
                                ---------------------------------------------------------------------------------------
                                Q。返回上一页
                                =======================================================================================
                                                            """
                                print(menums_file)
                            elif menum_2.upper() == 'B':
                                Xlsx_video().def_sql_url()
                                Retweet_parse_list().sql_s()
                                menums_file = """   
                                                    ====================采集完毕！>>>>是否继续采集>>>返回上一页=====================================
                                                    ======================================sql转换URL========================================
                                                         A。xlsx转换 https://v.douyin.com/iKeD74w/ 为sql文件
                                                    ---------------------------------------------------------------------------------------
                                                         B。xlsx转换/video/7312743380214238498 为sql文件
                                                    ---------------------------------------------------------------------------------------
                                                         Q。返回上一页
                                                    =======================================================================================
                                                            """
                                print(menums_file)
                            elif menum_2.upper() == 'Q':
                                print("""==================结束操作>>>>>>>返回上一页=================""")
                                menums_file = """
                                                                                =======================保存文件=======================
                                                                                                    A。保存csv文件
                                                                                ----------------------------------------------------
                                                                                                    B。保存sql文件
                                                                                ----------------------------------------------------
                                                                                                    Q。返回上一页
                                                                                ====================================================

                                                                                """
                                print(menums_file)
                                break
                    elif menums.upper() == 'Q':
                        print("""==================结束本次操作>>>返回主页=================""")
                        menum_collection = """
                                                =======================抖音采集=======================
                                                                    A。点赞和转发
                                                ----------------------------------------------------
                                                                    B。评论
                                                ----------------------------------------------------
                                                                    Q。结束选择文件操作
                                                ====================================================
                                                        """
                        print(menum_collection)
                        break
            elif menum.upper() == 'B':#评论
                menums = """
                                        =======================采集保存文件=======================
                                                            A。保存csv文件
                                        ----------------------------------------------------
                                                            B。保存sql文件
                                        ----------------------------------------------------
                                                            Q。结束选择文件操作
                                        ====================================================

                                        """
                print(menums)
                while 1:
                    menums = input('请选择你要保存的文件>>>>>>')
                    if menums.upper() == 'A':
                        menum_2 = """
                            ======================================csv转换URL========================================
                                 A。xlsx转换 https://v.douyin.com/iKeD74w/为csv文件
                            ---------------------------------------------------------------------------------------
                                 B。xlsx转换/video/7312743380214238498 为csv文件
                            ---------------------------------------------------------------------------------------
                                                Q。结束选择文件操作
                            =======================================================================================
                                    """
                        print(menum_2)
                        while 1:
                            menum_2 = input('请选择csv格式转换的url格式>>>>>>')
                            if menum_2.upper() == 'A':
                                Xlsx().def_csv()
                                Comments_parse_sql().def_csv()
                                menums_file = """
                                ====================采集完毕！>>>>是否继续采集>>>返回上一页=====================================
                                ======================================csv转换URL========================================
                                                 A。xlsx转换 https://v.douyin.com/iKeD74w/为csv文件
                                ---------------------------------------------------------------------------------------
                                                 B。xlsx转换/video/7312743380214238498 为csv文件
                                ---------------------------------------------------------------------------------------
                                                 Q。返回上一页
                                =======================================================================================
                                """
                                print(menums_file)
                            elif menum_2.upper() == 'B':
                                Xlsx_video().def_csv()
                                Comments_parse_sql().def_csv()
                                menums_file = """
                                                                ====================采集完毕！>>>>是否继续采集>>>返回上一页=====================================
                                                                ======================================csv转换URL========================================
                                                                                 A。xlsx转换 https://v.douyin.com/iKeD74w/为csv文件
                                                                ---------------------------------------------------------------------------------------
                                                                                 B。xlsx转换/video/7312743380214238498 为csv文件
                                                                ---------------------------------------------------------------------------------------
                                                                                 Q。返回上一页
                                                                =======================================================================================
                                                                """
                                print(menums_file)
                            elif menum_2.upper() == 'Q':
                                print("""==================结束操作>>>>>>>返回上一页=================""")
                                menums_file = """
                                                        =======================保存文件=======================
                                                                            A。保存csv文件
                                                        ----------------------------------------------------
                                                                            B。保存sql文件
                                                        ----------------------------------------------------
                                                                            Q。结束选择文件操作
                                                        ====================================================

                                                        """
                                print(menums_file)
                                break
                    elif menums.upper() == 'B':  # sql数据
                        menum_2 = """
                                                    ======================================sql转换URL===========================================
                                                         A。xlsx转换 https://v.douyin.com/iKeD74w/ 为sql文件
                                                    ---------------------------------------------------------------------------------------
                                                         B。xlsx转换/video/7312743380214238498 为sql文件
                                                    ---------------------------------------------------------------------------------------
                                                         Q。结束选择文件操作
                                                    =======================================================================================
                                                            """
                        print(menum_2)
                        while 1:
                            menum_2 = input('请选择sql格式转换的url格式>>>>>>')
                            if menum_2.upper() == 'A':
                                Xlsx().def_sql_url()
                                Comments_parse_sql().def_sql()
                                menums_file = """
                                ====================采集完毕！>>>>是否继续采集>>>返回上一页=====================================
                                ======================================sql转换URL========================================
                                A。xlsx转换 https://v.douyin.com/iKeD74w/ 为sql文件
                                ---------------------------------------------------------------------------------------
                                B。xlsx转换/video/7312743380214238498 为sql文件
                                ---------------------------------------------------------------------------------------
                                Q。返回上一页
                                =======================================================================================
                                                            """
                                print(menums_file)
                            elif menum_2.upper() == 'B':
                                Xlsx_video().def_sql_url()
                                Comments_parse_sql().def_sql()
                                menums_file = """   
                                                    ====================采集完毕！>>>>是否继续采集>>>返回上一页=====================================
                                                    ======================================sql转换URL========================================
                                                         A。xlsx转换 https://v.douyin.com/iKeD74w/ 为sql文件
                                                    ---------------------------------------------------------------------------------------
                                                         B。xlsx转换/video/7312743380214238498 为sql文件
                                                    ---------------------------------------------------------------------------------------
                                                         Q。返回上一页
                                                    =======================================================================================
                                                            """
                                print(menums_file)
                            elif menum_2.upper() == 'Q':
                                print("""==================结束操作>>>>>>>返回上一页=================""")
                                menums_file = """
                                                                                =======================保存文件=======================
                                                                                                    A。保存csv文件
                                                                                ----------------------------------------------------
                                                                                                    B。保存sql文件
                                                                                ----------------------------------------------------
                                                                                                    Q。返回上一页
                                                                                ====================================================

                                                                                """
                                print(menums_file)
                                break
                    elif menums.upper() == 'Q':
                        print("""==================结束本次操作>>>返回主页=================""")
                        menum_collection = """
                                                =======================抖音采集=======================
                                                                    A。点赞和转发
                                                ----------------------------------------------------
                                                                    B。评论
                                                ----------------------------------------------------
                                                                    Q。结束选择文件操作
                                                ====================================================
                                                        """
                        print(menum_collection)
                        break
            elif menum.upper()=='Q':
                print("""==================结束程序=================""")
                break
if __name__=='__main__':
    DY_main().def_host()