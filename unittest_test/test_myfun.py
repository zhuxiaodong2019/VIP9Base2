# -*- coding: utf-8 -*-
'''
@Time    : 2021/2/6 16:24
@Author  : zxd
'''
#测试用例类继承unittest.TestCase类
import unittest
from unittest_test.myfun import *


class TestMyFun(unittest.TestCase):

    #初始化方法 setUp
    @classmethod
    def setUpClass(cls):
        print("setUpClass整个测试用例执行前执行一次")
    def setUp(self):
        print("setUp每条测试用例执行前执行一次")

    #结束工作方法  tearDown
    @classmethod
    def tearDownClass(cls) -> None:
        print("tearDownClass整个测试用例执行后执行一次")
    def tearDown(self) -> None:
        print("tearDown每条测试用例执行后执行一次")

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
    unittest.main(verbosity=2)
