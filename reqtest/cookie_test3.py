# -*- coding: utf-8 -*-
'''
@Time    : 2021/2/6 15:21
@Author  : zxd
'''
#1---导入
import requests


# 发送Post请求
urlstr = 'https://www.wanandroid.com/user/login'

data = {'username':'zhuxiaodong','password':'test01'}

#2---发送请求
r  = requests.post(url=urlstr,data=data)
# print('***',r.text)
print(r.cookies)  #cookies 对应的Jsessionid每次都有变化,动态获取
print(r.cookies['JSESSIONID'])

# #获取上次请求放回的response中的cookie，通过字典的形式引用cookie返回的JSESSIONID，放入下次请求cookie中
cookie = {
    'JSESSIONID':r.cookies['JSESSIONID']
}

#携带cookie发送请求
r2 = requests.get('https://www.wanandroid.com/lg/todo/list/0',cookies = cookie)

# print('****',r2.text)
# print('****',r2.headers)

