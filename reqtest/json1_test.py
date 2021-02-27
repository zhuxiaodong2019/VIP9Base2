# -*- coding: utf-8 -*-
'''
@Time    : 2021/2/6 13:34
@Author  : zxd
'''
#1---导入
import requests,json


# 发送Post请求

urlstr = 'http://httpbin.org/post'
#字典类型参数
payload = {'cont':'selenium+jmeter+loadrunner','qq':'106014970'}
#接口文档要求传入json类型,需要进行转换
# 方法1:dumps方法
#通过json.dumps方法将Python字符串转换成json类型
# payload = json.dumps(payload)

#2---发送请求
# r  = requests.post(url=urlstr,data=payload)

#方法2:
r  = requests.post(url=urlstr,json=payload)
print(r.encoding)
#3---获取结果
print(r.text)

#返回为json类型，可以通过r.json方法来查看结果
print(r.json())