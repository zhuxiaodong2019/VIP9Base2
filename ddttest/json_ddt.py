# -*- coding: utf-8 -*-
'''
@Time    : 2021/2/27 17:26
@Author  : zxd
'''
import unittest
from ddt import ddt,data,unpack,file_data

@ddt
class TestMy(unittest.TestCase):

    @file_data('D:\\apitest\\VIP9Base2\\ddttest\\data.json')
    def test_fun(self,value):
        print(value)

if __name__ == '__main__':
    unittest.main()