#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# @当前时间 :2024/1/7 22:04
# @Author  : TS
# @Email   : TS@gmail.com
# @File    : ts2.py
# @Software: PyCharm
"""
from DY_Provincia_s import D_DY_Provincia
from DY_Provincia_s import D_DY_Popularity
class DY_host():
    menum_1 = """

                        |================抖音信息============|
                        |       A.城市排行榜                  |
                        |----------------------------------|
                        |       B.人气排行榜                  |   
                        |----------------------------------|
                        |       Q.退出                      |
                        |==================================|
                        """
    print(menum_1)
    while 1:
        num_2 = input('请输入:')
        if num_2.upper() == 'A':
            print('请稍后')
            D_DY_Provincia().def_my_job()
        elif num_2.upper() == 'B':
            D_DY_Popularity().def_my_job()
        elif num_2.upper() == 'Q':
            print("""==================结束本次操作=================""")
            break

if __name__ == '__main__':
        DY_host()
