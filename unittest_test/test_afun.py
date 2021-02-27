# -*- coding: utf-8 -*-
'''
@Time    : 2021/2/6 17:37
@Author  : zxd
'''
#测试用例类继承unittest.TestCase类
import unittest

from myfun import *


class TestAFun(unittest.TestCase):
    #测试用例,方法以test开头
    def test_div(self):
        print("执行测试div方法")
        # 断言
        self.assertEqual(2, divide(6, 3))

if __name__ == '__main__':
    pass
    # unittest.main(verbosity=2)