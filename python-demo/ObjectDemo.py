# !/usr/bin/python
# -*- coding: UTF-8 -*-
"""
类变量：类变量在整个实例化的对象中是公用的。类变量定义在类中且在函数体之外。类变量通常不作为实例变量使用。
实例变量：定义在方法中的变量，只作用于当前实例的类。
"""

class User:
    '用户类'
    userCount = 0 # 类变量，用户个数

    # __init__()方法是一种特殊的方法，被称为类的构造函数或初始化方法，当创建了这个类的实例时就会调用该方法
    def __init__(self,userName,userPwd,addr):  # 实例变量：userName,userPwd,addr
        self.userName = userName
        self.userPwd = userPwd
        self.addr = addr
        User.userCount += 1

    # 用户总数
    def userTotal(self):
        print "总用户量：%d" % User.userCount

    # 用户信息   self 代表类的实例，self 在定义类的方法时是必须有的，虽然在调用时不必传入相应的参数。
    def userInfo(self):
        print "用户名：%s,用户密码：%s,用户地址：%s" % (self.userName,self.userPwd,self.addr)

# 创建对象
user = User("xiaoming","xiaoming123","北京")
user2 = User("xiaohua","xiaohua123","成都")
user.userInfo()
user2.userInfo()
print "总用户量：%d" % User.userCount

"""
getattr(obj, name[, default]) : 访问对象的属性。
hasattr(obj,name) : 检查是否存在一个属性。
setattr(obj,name,value) : 设置一个属性。如果属性不存在，会创建一个新属性。
delattr(obj, name) : 删除属性。
"""
user3 = User("xiaowen","123","成都")
print hasattr(user3, 'userName')    # 如果存在 'age' 属性返回 True。
print getattr(user3, 'userName')    # 返回 'age' 属性的值
print setattr(user3, 'age',25) # 添加属性 'age' 值为 8
print delattr(user3, 'age')    # 删除属性 'age'

"""
_dict__ : 类的属性（包含一个字典，由类的数据属性组成）
__doc__ :类的文档字符串
__name__: 类名
__module__: 类定义所在的模块（类的全名是'__main__.className'，如果类位于一个导入模块mymod中，那么className.__module__ 等于 mymod）
__bases__ : 类的所有父类构成元素（包含了一个由所有父类组成的元组） 
"""
print "User.__doc__:", User.__doc__
print "User.__name__:", User.__name__
print "User.__module__:", User.__module__
print "User.__bases__:", User.__bases__
print "User.__dict__:", User.__dict__

# 析构函数 __del__ ，__del__在对象销毁的时候被调用，当对象不再被使用时，__del__方法运行
class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __del__(self):
        class_name = self.__class__.__name__
        print class_name, "销毁"

pt1 = Point()
pt2 = pt1
pt3 = pt1
print id(pt1), id(pt2), id(pt3)  # 打印对象的id
del pt1
del pt2
del pt3

"""
在python中继承中的一些特点：
    1：在继承中基类的构造（__init__()方法）不会被自动调用，它需要在其派生类的构造中亲自专门调用。
    2：在调用基类的方法时，需要加上基类的类名前缀，且需要带上self参数变量。区别于在类中调用普通函数时并不需要带上self参数
    3：Python总是首先查找对应类型的方法，如果它不能在派生类中找到对应的方法，它才开始到基类中逐个查找。（先在本类中查找调用的方法，找不到才去基类中找）。
"""


class Parent:  # 定义父类
    parentAttr = 100

    def __init__(self):
        print "调用父类构造函数"

    def parentMethod(self):
        print '调用父类方法'

    def setAttr(self, attr):
        Parent.parentAttr = attr

    def getAttr(self):
        print "父类属性 :", Parent.parentAttr

class Child(Parent):  # 定义子类
    def __init__(self):
        print "调用子类构造方法"

    def childMethod(self):
        print '调用子类方法 child method'

c = Child()  # 实例化子类
c.childMethod()  # 调用子类的方法
c.parentMethod()  # 调用父类方法
c.setAttr(200)  # 再次调用父类的方法
c.getAttr()  # 再次调用父类的方法

#issubclass() - 布尔函数判断一个类是另一个类的子类或者子孙类，语法：issubclass(sub,sup)
print issubclass(Child,Parent)

#isinstance(obj, Class) 布尔函数如果obj是Class类的实例对象或者是一个Class子类的实例对象则返回true
print isinstance(c,Child)

# 方法重写
class Animal:  # 定义父类
    def __init__(self):
        print "调用父类构造函数"

    def myMethod(self):
        print '调用父类方法'


class Dog(Animal):  # 定义子类
    def __init__(self):
        print "调用子类构造函数"

    def myMethod(self):
        print '调用子类方法'


dog = Dog()  # 子类实例
dog.myMethod()  # 子类调用重写方法

"""
单下划线、双下划线、头尾双下划线说明：
    __foo__: 定义的是特列方法，类似 __init__() 之类的。
    _foo: 以单下划线开头的表示的是 protected 类型的变量，即保护类型只能允许其本身与子类进行访问，不能用于 from module import *
    __foo: 双下划线的表示的是私有类型(private)的变量, 只能是允许这个类本身进行访问了。
"""
class Device:
    deviceCount = 0 # 公共变量
    __deviceFactoryCount = 0 # 私有变量

    def count(self):
        self.deviceCount += 1
        self.__deviceFactoryCount += 1
        print self.__deviceFactoryCount

    def getDeviceFactoryCount(self):
        return self.__deviceFactoryCount

device = Device()
device.count()
device.count()
print "设备总数：%d" % device.deviceCount
# print "设备厂家总数：%d" % device.__deviceFactoryCount  # 报错，实例不能访问私有变量
# Python不允许实例化的类访问私有数据，但你可以使用 object._className__attrName 访问属性
print  "设备厂家总数：%d" % device._Device__deviceFactoryCount
print  "设备厂家总数：%d" % device.getDeviceFactoryCount()
