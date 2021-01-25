# -*- coding: utf-8 -*-
'''
@Time    : 2021/1/23 17:37
@Author  : zxd
'''
#super
#师傅类
class Master():
    def __init__(self):
        self.kongfu = '[五香煎饼果子]'
    def make_cake(self):
        print(f'运用{self.kongfu}制作五香#####')
#学校继承老师傅类
class School(Master):
    def __init__(self):
        self.kongfu = '[香辣煎饼果子]'
    def make_cake(self):
        print(f'运用{self.kongfu}制作香辣#####')
        #super()就是父类的意思
    def make_cake2(self):
        super().__init__()
        super().make_cake()
# scho = School()
# scho.make_cake()
# scho.make_cake2()
#徒弟类
class Prentice(School):
    def __init__(self):
        self.kongfu = '[独创煎饼果子]'
    def make_cake(self):
        #如果先调用父类的属性和方法,父类的属性方法会覆盖子类的属性方法,故先调用子类的初始化方法
        self.__init__()
        print(f'运用{self.kongfu}制作独创#####')
    def make_old_cake(self):
        super().__init__()
        super().make_cake()

xiaoming = Prentice()
xiaoming.make_cake()
xiaoming.make_old_cake()
