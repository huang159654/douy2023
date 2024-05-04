#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# @当前时间 :2024/1/7 19:46
# @Author  : TS
# @Email   : TS@gmail.com
# @File    : ts2.py
# @Software: PyCharm
"""
from  DY_Provincial import DY_Provincia

from DY_Provincial import DY_Popularity
from apscheduler.schedulers.blocking import BlockingScheduler

class D_DY_Provincia():#城市排行榜
    def __init__(self):
        pass
    def def_main(self):
        anchor_id = 4420516664586606
        room_id = 7321327191466494746
        DY_Provincia().def_Parse(anchor_id=anchor_id, room_id=room_id)
        print('===============================================================')
    def def_my_job(self):
        sched = BlockingScheduler()
        # 设定执行时间
        sched.add_job(self.def_main, 'cron',second = '*/5', )#表示每5秒执行该程序一次，相当于interval 间隔调度中seconds = 5
        sched.start()
    def dj(self):
        d= {'城市':['贵州'], 'anchor_id':4420516664586606,'room_id':7321327191466494746}
class D_DY_Popularity():#人气排行榜
    def __init__(self):
        pass
    def def_main(self):
        DY_Popularity().def_Parse()
        print('===============================================================')
    def def_my_job(self):
        sched = BlockingScheduler()
        # 设定执行时间
        sched.add_job(self.def_main, 'cron',second = '*/5', )#表示每5秒执行该程序一次，相当于interval 间隔调度中seconds = 5
        sched.start()


