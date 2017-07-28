# !/usr/bin/python
# -*- coding: UTF-8 -*-

"""
自定义函数规则：
    函数代码块以 def 关键词开头，后接函数标识符名称和圆括号()。
    任何传入参数和自变量必须放在圆括号中间。圆括号之间可以用于定义参数。
    函数的第一行语句可以选择性地使用文档字符串—用于存放函数说明。
    函数内容以冒号起始，并且缩进。
    return [表达式] 结束函数，选择性地返回一个值给调用方。不带表达式的return相当于返回 None。
"""

# 定义函数
def printHello(str):
    "打印传入的参数"
    print str
    return

# 调用函数
printHello("hello world")

"""
在 python 中，strings, tuples, 和 numbers 是不可更改的对象，而 list,dict 等则是可以修改的对象。
不可变类型：变量赋值 a=5 后再赋值 a=10，这里实际是新生成一个 int 值对象 10，再让 a 指向它，而 5 被丢弃，不是改变a的值，相当于新生成了a。
可变类型：变量赋值 la=[1,2,3,4] 后再赋值 la[2]=5 则是将 list la 的第三个元素值更改，本身la没有动，只是其内部的一部分值被修改了。
"""

# python 传不可变对象实例
def changeImmutable(a):
    a = 10
b = 2
changeImmutable(b)
print b  # 结果还是2

# python 传可变对象实例
def changeme(mylist):
    "修改传入的列表"
    mylist.append([1, 2, 3, 4]);
    print "函数内取值: ", mylist
    return
# 调用changeme函数
mylist = [10, 20, 30];
changeme(mylist);
print "函数外取值: ", mylist

# 关键字参数
def printme(str):

    print str;
    return;
# 调用printme函数
printme(str="My string")

# 缺省参数
def printinfo(name, age=35):
    "打印任何传入的字符串"
    print "Name: ", name;
    print "Age ", age;
    return;
# 调用printinfo函数
printinfo(age=50, name="miki");
printinfo(name="miki");

# 不定长参数
# 加了星号（*）的变量名会存放所有未命名的变量参数。选择不多传参数也可。
def printinfo(arg1, *vartuple):
    print "输出arg1: ",arg1
    for var in vartuple:
        print "输出vartuple",var
    return;
# 调用printinfo 函数
printinfo(10)
printinfo(70, 60, 50)

# python 使用 lambda 来创建匿名函数。
sum = lambda arg1, arg2: arg1 + arg2;
# 调用sum函数
print "相加后的值为 : ", sum(10, 20)

# 列表反转函数
def reverse(ListInput):
	RevList=[]
	for i in range (len(ListInput)):
		RevList.append(ListInput.pop())
	return RevList
names = ['xiaoming','xiaoqiang','xiaowen']
print 'names before=',names;
print 'names after=',reverse(names)

# 全局变量想作用于函数内，需加 global
# 1、global---将变量定义为全局变量。可以通过定义为全局变量，实现在函数内部改变变量值。
# 2、一个global语句可以同时定义多个变量，如 global x, y, z。
globvar = 0
def set_globvar_to_one():
    global globvar    # 使用 global 声明全局变量
    globvar = 1

def print_globvar():
    print(globvar)     # 没有使用 global

set_globvar_to_one()
print  globvar        # 输出 1
print_globvar()       # 输出 1，函数内的 globvar 已经是全局变量

def hello(event, context):
    return "hello world"