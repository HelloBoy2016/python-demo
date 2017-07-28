# !/usr/bin/python
# -*- coding: UTF-8 -*-
"""
这个语法是用来代替传统的try...finally语法的
基本思想是with所求值的对象必须有一个__enter__()方法，一个__exit__()方法。
紧跟with后面的语句被求值后，返回对象的__enter__()方法被调用，这个方法的返回值将被赋值给as后面的变量。当with后面的代码块全部被执行完之后，将调用前面返回对象的__exit__()方法。
"""
# try finally写法
file = open("foo.txt")
try:
    data = file.read()
    print data
finally:
    file.close()

# 使用with...as...的方式替换
with open("foo.txt") as file:
    data = file.read()
    print data


class Sample:
    def __enter__(self):
        print "In __enter__()"
        return "Foo"
    def __exit__(self, type, value, trace):
        print "In __exit__()"

def get_sample():
    return Sample()

with get_sample() as sample:
    print "sample:", sample





