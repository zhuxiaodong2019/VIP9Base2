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

# xiaoming = Prentice()
# print(xiaoming.kongfu)
# xiaoming.make_cake()
# xiaoming.make_master_cake()
# xiaoming.make_schoole_cake()

# mst = Master()
# mst.make_cake()
# print(Prentice.__mro__)  #类的调用顺序
xiaogang = TuSun()
xiaogang.make_cake()
xiaogang.make_master_cake()
xiaogang.make_schoole_cake()