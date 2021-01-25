# -*- coding: utf-8 -*-
'''
@Time    : 2021/1/23 17:00
@Author  : zxd
'''
#多继承
#师傅类
class Master():
    def __init__(self):
        self.kongfu = '[五香煎饼果子]'
    def make_cake(self):
        print(f'运用{self.kongfu}制作五香#####')
class School():
    def __init__(self):
        self.kongfu = '[香辣煎饼果子]'
    def make_cake(self):
        print(f'运用{self.kongfu}制作香辣#####')
#徒弟类
class Prentice(School, Master):
    def __init__(self):
        self.kongfu = '[独创煎饼果子]'
        #定义私有属性
        self.__monkey = 1000
    #定义私有方法
    def __info_print(self):
        print(self.kongfu)
        print(self.__monkey)
    #获取私有属性
    def get_money(self):
        return self.__monkey
    #设置修改私有属性
    def set_money(self):
        self.__monkey = 500


    def make_cake(self):
        #如果先调用父类的属性和方法,父类的属性方法会覆盖子类的属性方法,故先调用子类的初始化方法
        self.__init__()
        print(f'运用{self.kongfu}制作独创#####')
    def make_master_cake(self):
        #调用父类方法,为了保证调用的是父类的属性,故先调用父类的初始化方法
        Master.__init__(self)
        Master.make_cake(self)

    def make_schoole_cake(self):
        School.__init__(self)
        School.make_cake(self)
#徒孙类
class TuSun(Prentice):
    pass

xiaoming  = Prentice()
# print(xiaoming.get_money())
# xiaoming.set_money()
# print(xiaoming.get_money())
# xiaoming.__info_() #对象不能访问私有属性和私有方法
#
xiaogang = TuSun()
print(xiaogang.get_money())
# xiaogang.__info_print()#子类不能访问私有属性和私有方法

