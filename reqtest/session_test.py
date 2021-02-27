# -*- coding: utf-8 -*-
'''
@Time    : 2021/2/6 14:15
@Author  : zxd
'''
#1.请求地址
import requests
urlstr1 = "https://www.wanandroid.com/user/login"
urlstr = "https://www.wanandroid.com/lg/todo/list/0"
datas = {'username':'zhuxiaodong','password':'test01'}
#访问登录后的接口,用session方式访问
s=requests.session()
r=s.post(url=urlstr1,data=datas)
#2.发送请求
r2=s.get(url=urlstr)
print(r2.status_code)
print(r2.text)

