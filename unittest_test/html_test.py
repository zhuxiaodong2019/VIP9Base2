# -*- coding: utf-8 -*-
'''
@Time    : 2021/2/6 18:06
@Author  : zxd
'''
import unittest,os
from HTMLTestRunner import HTMLTestRunner
class RunAllCase:
    def run_test(self):
        #调用defaultTestLoader类中的discover方法,寻找测试集合
        test_dir = os.path.dirname(__file__)
        suite=unittest.defaultTestLoader.discover(test_dir,pattern="test*.py")
        #构建html测试报告,以wb写的方式打开
        fp = open('./test.html','wb')
        runner=HTMLTestRunner(stream=fp,title='计算器接口自动化测试报告',description='测试用例执行情况')
        # 4.运行测试用例集合
        runner.run(suite)
if __name__ == '__main__':
    RunAllCase().run_test()