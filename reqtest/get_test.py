# -*- coding: utf-8 -*-
'''
@Time    : 2021/2/6 10:44
@Author  : zxd
'''
import requests

#1.请求地址
urlstr = 'https://www.wanandroid.com/'
#2.发送请求
r = requests.get(url=urlstr)
#3.输出响应结果
print(r.status_code)
print(r.text)