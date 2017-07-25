# !/usr/bin/python
# -*- coding: UTF-8 -*-
# Python程序语言指定任何非0和非空（null）值为true，0 或者 null为false。
name = 'xubiao'
if(name == 'xubiao'):
    print('name = ' + name)
else:
    print('name ! = ' + name)

#if 语句多条件
num = 9
if num >= 0 and num <= 10:  # 判断值是否在0~10之间
    print 'hello'

num = 10
if num < 0 or num > 10:  # 判断值是否在小于0或大于10
    print 'hello'
else:
    print 'undefine'

num = 8
# 判断值是否在0~5或者10~15之间
if (num >= 0 and num <= 5) or (num >= 10 and num <= 15):
    print 'hello'
else:
    print 'undefine'


#python 复合布尔表达式计算采用短路规则，即如果通过前面的部分已经计算出整个表达式的值，则后面的部分不再计算
a = 0
b = 1
if (a > 0) and (b / a > 2):
    print "yes"
else:
    print "no"
