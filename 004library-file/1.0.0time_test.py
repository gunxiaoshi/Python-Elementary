#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2018/12/13 17:36
# @Author  : Jianfeng Ding
# @Site    : 
# @File    : 1.0.0time_test.py
# @Software: PyCharm

# # time模块常用于时间和日期的查看
# import time
#
# print(time.time())
# print(time.localtime())
# print(time.strftime('%Y-%m-%d %H:%M:%S'))
# print(time.strftime('%Y%m%d'))

# datetime模块常用于时间和日期的修改
import datetime

print(datetime.datetime.now())
newtime = datetime.timedelta(minutes=10)
print(datetime.datetime.now() + newtime)

one_day = datetime.datetime(2018, 12, 23)
new_date = datetime.timedelta(days=10)
print(one_day + new_date)
