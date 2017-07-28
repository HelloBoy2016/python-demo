# !/usr/bin/python
# -*- coding: UTF-8 -*-

# 元组的元素不能修改
# 元组中只包含一个元素时，需要在元素后面添加逗号
tup1 = (50,)
print tup1[0]

# 元组可以使用下标索引来访问元组中的值
names = ('xiaoming',25,'60kg')
print names[2]
print names[0:3]

# 元组中的元素值是不允许修改的，但我们可以对元组进行连接组合
tup1 = (12, 34.56)
tup2 = ('abc', 'xyz')
# 以下修改元组元素操作是非法的。
# tup1[0] = 100
# 创建一个新的元组
tup3 = tup1 + tup2
print tup3

# 元组中的元素值是不允许删除的，但我们可以使用del语句来删除整个元组

tup = ('physics', 'chemistry', 1997, 2000)
print tup
del tup
# print "After deleting tup : ",tup  这句报错NameError: name 'tup' is not defined