# -*- coding: utf-8 -*-
'''
@Time    : 2021/2/6 15:26
@Author  : zxd
'''
#1---导入
import requests


# 发送Post请求
urlstr = 'https://www.wanandroid.com/user/login'

data = {'username':'zhuxiaodong','password':'test01'}


#2---发送请求
r  = requests.post(url=urlstr,data=data)
# print('***text',r.text)
# print('***cookie',r.cookies)
# print('***headers',r.headers)
# print(r.cookies['JSESSIONID'])
#
# #获取上次请求放回的response中的cookie，通过字典的形式引用cookie返回的JSESSIONID，放入下次请求header中
#
header = {
    'cookie':'JSESSIONID='+r.cookies['JSESSIONID']
}

r2 = requests.get('https://www.wanandroid.com/lg/todo/list/0',headers = header)


print('****',r2.text)
#find方法
#str.find方法返回-1表示未找到，非-1表示找到,并返回子字符串的索引
# result = r2.text.find("已完成清单")
# print(result)
# if result != -1:
#     print('查询成功')
# else:
#     print('查询失败')
# #
# #或通过正则来查找
import re
pattern = re.compile(r';\">(.*?)</h2>')
result = pattern.findall(r2.text)
print(result)
#

#
# .点 匹配任何单个字符。例如正则表达式r(.)匹配字符串abcd  a   cd   匹配a。
# * 匹配0或多个在它之前的那个字符。例如正则表达式。*意味着能够匹配任意数量的任何字符。 a*
# ? 匹配0或1个正好在它之前的那个字符。    a?



