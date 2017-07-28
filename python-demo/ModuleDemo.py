# !/usr/bin/python
# -*- coding: UTF-8 -*-

# 导入模块
import math

import support

# 调用模块中的函数  调用规则：模块名.函数名
support.stringFunc("xiaoming")
support.listFunc(["xiaoming","xiaohaung","xiaowen"])

# Python 的 from 语句让你从模块中导入一个指定的部分到当前命名空间中
from support2 import getUserById
getUserById("user_id")

# from support2 import *  把一个模块的所有内容全都导入到当前的命名空间

# 命名空间和作用域
Money = 2000
def AddMoney():
    global Money
    Money = Money + 1
print Money
AddMoney()
print Money

# dir() 函数一个排好序的字符串列表，内容是一个模块里定义过的名字
content = dir(math)
print content

# globals() 和 locals() 函数可被用来返回全局和局部命名空间里的名字
print  globals()
print  locals()