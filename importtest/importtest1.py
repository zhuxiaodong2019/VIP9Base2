# -*- coding: utf-8 -*-
'''
@Time    : 2021/1/30 11:34
@Author  : zxd
'''
# import math
# print(math.sqrt(9))

# from math import sqrt
# from math import  *  # *表示导入所有方法
# from math import sqrt as st  #as别名:将sqrt重命名为st
# print(st(9))
#包--邮件:mark directory as -->source Root
# import my_module1
# my_module1.testA(1,2)

# from my_module1 import my_test
# from my_module2 import my_test
# my_test(3,2)
# from my_module1 import *
# testA()
# testB()

# from my_module1 import *
# from my_module2 import *
# import importtest.my_module1
# importtest.my_module1.info_print1()
# info_print1()
# info_print2()
from importtest import *
my_module1.info_print1()
my_module2.info_print2()