# -*- coding: utf-8 -*-
'''
@Time    : 2021/3/6 10:54
@Author  : zxd
@功能: 时间包
'''
import time

print(time.time())  #时间戳
print(time.localtime())  #time.struct_time(tm_year=2021, tm_mon=3, tm_mday=6, tm_hour=10, tm_min=57, tm_sec=3,)
print(time.strftime("%Y_%m_%d_%H_%M_%S", time.localtime())) #格式化时间输出
