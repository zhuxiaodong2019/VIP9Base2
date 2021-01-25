# -*- coding: utf-8 -*-
'''
@Time    : 2021/1/23 16:49
@Author  : zxd
'''
#继承
# A :父类
# class A():
#     def __init__(self):
#         self.num = 1
#
#     def info_print(self):
#         print(self.num)
# #B继承A中所有的属性和方法
# #B :子类
# class B(A):
#     pass


# result = B()
# result.info_print()
#师傅类
class Master():
    def __init__(self):
        self.kongfu = '[五香煎饼果子]'
    def make_cake(self):
        print(f'运用{self.kongfu}制作五香#####')
#徒弟类
class Prentice(Master):
    pass

# xiaoming = Prentice()
# print(xiaoming.kongfu)
# xiaoming.make_cake()
# mst = Master()
# mst.make_cake()