# -*- coding: utf-8 -*-
'''
@Time    : 2021/2/6 11:20
@Author  : zxd
'''
import requests
help(requests)
#1.请求地址
urlstr = 'https://www.baidu.com'
#2.发送请求
r = requests.get(url=urlstr)
#3.输出响应结果
print(r.encoding)  #响应的编码方式
print(r.apparent_encoding)
# r.encoding = r.apparent_encoding
print(r.status_code)
# print(r.text)
print(r.headers)