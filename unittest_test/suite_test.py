# -*- coding: utf-8 -*-
'''
@Time    : 2021/2/6 17:18
@Author  : zxd
'''
#测试用例类继承unittest.TestCase类
import unittest

from myfun import *


class TestMyFun(unittest.TestCase):

    #测试用例,方法以test开头
    def test_add(self):
        print("执行测试add方法")
        #断言
        self.assertEqual(add(1,2),3)
    @unittest.skip("临时跳过此条测试用例")
    def test_minus(self):
        print("执行测试minus方法")
        #断言
        self.assertEqual(2,minus(5,3))
    def test_mult(self):
        print("执行测试mult方法")
        # 断言
        self.assertEqual(5, multi(2, 3))
if __name__ == '__main__':
    #1.创建测试用例集合
    suite = unittest.TestSuite()
    #2.将测试用例方法加入到用例集合
    suite.addTest(TestMyFun('test_add'))
    # suite.addTests([TestMyFun('test_add'),])
    #3.构建测试用例执行机器
    runner = unittest.TextTestRunner()
    #4.运行测试用例集合
    runner.run(suite)