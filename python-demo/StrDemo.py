# !/usr/bin/python
# -*- coding: UTF-8 -*-

# Python访问子字符串，可以使用方括号来截取字符串
var1 = 'Hello World!'
var2 = "Python Runoob"
print "var1[0]: ", var1[0]
print "var2[1:5]: ", var2[1:5]

# str测试
a = "Hello"
b = "Python"
print "a + b 输出结果：", a + b
print "a * 2 输出结果：", a * 2
print "a[1] 输出结果：", a[1]
print "a[1:4] 输出结果：", a[1:4]

if( "H" in a) :
    print "H 在变量 a 中"
else :
	print "H 不在变量 a 中"

if( "M" not in a) :
    print "M 不在变量 a 中"
else :
	print "M 在变量 a 中"

print r'\n'
print R'\n'

# Python 字符串格式化
print "My name is %s, age is %s , weight is %skg" % ("xubiao",25,60)