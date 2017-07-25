# !/usr/bin/python
# -*- coding: UTF-8 -*-

counter = 100  # 赋值整型变量
miles = 1000.0  # 浮点型
name = "John"  # 字符串
print counter
print miles
print name

#Python允许你同时为多个变量赋值
a = b = c = 1;
print a,b,c;

#为多个对象指定多个变量
a, b, c = 1, 2, "john";
print a,b,c;

'''
Python有五个标准的数据类型：
    Numbers（数字）
    String（字符串）
    List（列表）
    Tuple（元组）
    Dictionary（字典）
'''
'''
Python支持四种不同的数字类型：
    int（有符号整型）
    long（长整型[也可以代表八进制和十六进制]）
    float（浮点型）
    complex（复数） 
'''

#字符串或串(String)是由数字、字母、下划线组成的一串字符。
#获取一段子字符串的话，可以使用变量 [头下标:尾下标]
s = 'ilovepython';
print s[1:5]; #截取字符串1,5

#加号（+）是字符串连接运算符，星号（*）是重复操作。如下实例：
str = 'Hello World!'
print str  # 输出完整字符串
print str[0]  # 输出字符串中的第一个字符
print str[2:5]  # 输出字符串中第三个至第五个之间的字符串
print str[2:]  # 输出从第三个字符开始的字符串
print str * 2  # 输出字符串两次
print str + "TEST"  # 输出连接的字符串

# List（列表） 是 Python 中使用最频繁的数据类型。
# 列表可以完成大多数集合类的数据结构实现。它支持字符，数字，字符串甚至可以包含列表（即嵌套）。
list = ['runoob', 786, 2.23, 'john', 70.2]
tinylist = [123, 'john']
print list  # 输出完整列表
print list[0]  # 输出列表的第一个元素
print list[1:3]  # 输出第二个至第三个的元素
print list[2:]  # 输出从第三个开始至列表末尾的所有元素
print tinylist * 2  # 输出列表两次
print list + tinylist  # 打印组合的列表

# 元组是另一个数据类型，类似于List（列表）。
# 元组用"()"标识。内部元素用逗号隔开。但是元组不能二次赋值，相当于只读列表。
tuple = ('runoob', 786, 2.23, 'john', 70.2)
tinytuple = (123, 'john')
print tuple  # 输出完整元组
print tuple[0]  # 输出元组的第一个元素
print tuple[1:3]  # 输出第二个至第三个的元素
print tuple[2:]  # 输出从第三个开始至列表末尾的所有元素
print tinytuple * 2  # 输出元组两次
print tuple + tinytuple  # 打印组合的元组

'''
字典(dictionary)是除列表以外python之中最灵活的内置数据结构类型。列表是有序的对象结合，字典是无序的对象集合。
两者之间的区别在于：字典当中的元素是通过键来存取的，而不是通过偏移存取。
字典用"{ }"标识。字典由索引(key)和它对应的值value组成。
'''
dict = {}
dict['one'] = "This is one"
dict[2] = "This is two"
tinydict = {'name': 'john', 'code': 6734, 'dept': 'sales'}
print dict['one']  # 输出键为'one' 的值
print dict[2]  # 输出键为 2 的值
print tinydict  # 输出完整的字典
print tinydict.keys()  # 输出所有键
print tinydict.values()  # 输出所有值

# 将一个整数装换成十六进制
a = 123
print hex(a)

# << >>
b = 60
print b >> 2
print b << 2

# is ==
c = 6666
d = 6666
print c is d
print c == d



