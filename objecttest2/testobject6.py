# -*- coding: utf-8 -*-
'''
@Time    : 2021/1/30 11:10
@Author  : zxd
'''
#多态

class Dog(object):
    def work(self):  # ⽗父类提供统⼀一的⽅方法，哪怕是空⽅方法
        print('指哪打哪...')

class ArmyDog(Dog):  # 继承Dog类
    def work(self):  # ⼦子类重写⽗父类同名⽅方法
        print('追击敌...')

class DrugDog(Dog):
    def work(self):
        print('追查毒品...')

class Person(object):
    def work_with_dog(self, d):  # 传⼊入不不同的对象，执⾏行行不不同的代码，即不不同的work函数
        d.work()

ad = ArmyDog()
dd = DrugDog()
daqiu = Person()
daqiu.work_with_dog(ad)
daqiu.work_with_dog(dd)