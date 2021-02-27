# -*- coding: utf-8 -*-
'''
@Time    : 2021/2/6 15:11
@Author  : zxd
'''
#携带cookie
'''
通过r.cookies手动获取上一请求返回的cookie来设置下次请求的cookie

'''
#1---导入
import requests


# 发送Post请求
urlstr = 'https://www.wanandroid.com/user/login'

data = {'username':'zhuxiaodong','password':'test01'}

#2---发送请求
r  = requests.post(url=urlstr,data=data)
# print('***',r.text)
print('***',r.cookies)
print('***',r.headers)

#获取上次请求放回的response中的cookie，传递给下次请求
cookie = r.cookies
# #
# # #携带cookie发送请求
r2 = requests.get('https://www.wanandroid.com/lg/todo/list/0',cookies = cookie)
print('***',r2.status_code)
