# !/usr/bin/python
# -*- coding: UTF-8 -*-
"""try:
<语句>        #运行别的代码
except <名字>：
<语句>        #如果在try部份引发了'name'异常
except <名字>，<数据>:
<语句>        #如果引发了'name'异常，获得附加的数据
else:
<语句>        #如果没有异常发生
"""
# 正常执行
try:
    fh = open("testfile.txt", "w")
    fh.write("这是一个测试文件，用于测试异常!!")
except IOError:
    print "Error: 没有找到文件或读取文件失败"
else:
    print "内容写入文件成功"
    fh.close()

# 异常执行
try:
    fh = open("testfile.txt", "r")
    fh.write("这是一个测试文件，用于测试异常!!")
except IOError:
    print "Error: 没有找到文件或读取文件失败"
else:
    print "内容写入文件成功"
    fh.close()

# try-finally 语句无论是否发生异常都将执行最后的代码。
try:
    fh = open("testfile2.txt", "w")
    fh.write("这是一个测试文件，用于异常测试")
finally:
    print "无论如何都要执行"

# 经典文件操作
try:
    fh = open("testfile2.txt", "r")
    try:
        fh.write("这是一个测试文件，用于测试异常!!")
    finally:
        print "关闭文件"
        fh.close()
except IOError:
    print "Error: 没有找到文件或读取文件失败"

# 异常的参数
def tempConvert(str):
    try:
        return int(str)
    except ValueError:
        print "参数不是数字：",str
# 调用函数
tempConvert("abc")

"""
使用raise语句自己触发异常
"""
# 定义函数
# def mye(level):
#     if level < 1:
#         raise Exception("Invalid level!", level)
#         # 触发异常后，后面的代码就不会再执行
# try:
#     mye(0)
# except "Invalid level!":
#     print 1
# else:
#     print 2

# 0 作为除数
try:
    1 / 0
except Exception as e:
    '''异常的父类，可以捕获所有的异常'''
    print "0不能被除"
else:
    '''保护不抛出异常的代码'''
    print "没有异常"
finally:
    print "最后总是要执行"
