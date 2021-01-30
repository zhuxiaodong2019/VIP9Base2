# -*- coding: utf-8 -*-
'''
@Time    : 2021/1/30 13:51
@Author  : zxd
'''
#异常定义
# try:
#     open('test.txt', 'r')
# except:
#     open('test.txt', 'w')

#指定异常
# try:
#     print(num)
# except NameError:
#     print('num 有错误')
#捕获多个指定异常
# try:
#     print(1/0)
# except (NameError, ZeroDivisionError):
#     print('0不能做除数')
#捕获异常描述信息
# try:
#     print(1/0)
# except (NameError, ZeroDivisionError) as msg:
#     print(msg)
#捕获所有异常
# try:
#     print(1/0)
# except Exception as msg:
#     print(msg)
#异常中的else,没有异常会执行else
# try:
#     print(1/1)
# except Exception as msg:
#     print(msg)
# else:
#     print('我是异常中的else')
#异常中的finally,无论代码是否有异常都要执行的代码
# global f
# try:
#     f = open('test2.txt','r')
# except Exception as msg:
#     print(msg)
# else:
#     print('没有异常')
# finally:
#     print("finally执行")
#     f.close()

#异常传递
import time
try:
    f = open('test.txt')
    try:
        while True:
            content = f.readline()
            if len(content) == 0:
                break
            time.sleep(2)
            print(content)
    except:
        # 如果在读取⽂文件的过程中，产⽣生了了异常，那么就会捕获到
        # 比如 按下了了 ctrl+c
        print('意外终止了读取数据')
    finally:
        f.close()
        print('关闭文件')
        #向上层抛出异常
except:
    print("没有这个文件")
