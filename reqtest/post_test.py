# -*- coding: utf-8 -*-
'''
@Time    : 2021/2/6 11:37
@Author  : zxd
'''

#1.请求地址
import requests

urlstr = "https://www.wanandroid.com/user/login"
datas = {'username':'zhuxiaodong','password':'test01'}
# print(type(datas))
#2.发送请求
r = requests.post(url=urlstr,data=datas)
print(r.status_code)
# print(r.text)
print(r.json())
#响应结果为res_result
res_result=r.json()  #将json类型转换为dict类型
print(type(res_result))
# r2=r.text   r.text输出为字符串
# print(r2['errorCode'])
errCode=res_result['errorCode']
username=res_result['data']['username']
#响应断言
if errCode==0 and username==datas['username']:
    print("登录成功")
