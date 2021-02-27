# -*- coding: utf-8 -*-
'''
@Time    : 2021/2/6 13:40
@Author  : zxd
'''
#1.请求地址
import requests

urlstr = "https://www.wanandroid.com/user/login"
datas = {'username':'zhuxiaodong','password':'test01'}
#请求头,浏览器或客户端
header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.146 Safari/537.36'}
print(type(datas))
#2.发送请求
r = requests.post(url=urlstr,data=datas,headers=header)
#r.headers 响应头
print(r.headers)
print(r.status_code)
print(r.text)