# !/usr/bin/python
# -*- coding: UTF-8 -*-

# 打印到屏幕-可以给它传递零个或多个用逗号隔开的表达式
name = "xiaoming"
age = 25
print  "userInfo:name=",name," age=",age

# 读取键盘输入， Python提供了两个内置函数从标准输入读入一行文本，默认的标准输入是键盘
# raw_input([prompt]) 函数从标准输入读取一个行，并返回一个字符串（去掉结尾的换行符）
# str = raw_input("请输入：")
# print  "你输入的内容：",str

# input([prompt]) 函数和 raw_input([prompt]) 函数基本类似，但是 input 可以接收一个Python表达式作为输入，并将运算结果返回。
# str2 = raw_input("请输入：")
# print  "你输入的内容：",str2

# Python内置的open()函数打开一个文件，创建一个file对象，相关的方法才可以调用它进行读写
# 打开一个文件
fo = open("foo.txt", "wb")
print "文件名: ", fo.name
print "是否已关闭 : ", fo.closed
print "访问模式 : ", fo.mode
print "末尾是否强制加空格 : ", fo.softspace
# 关闭文件
fo.close()
"""
write()方法可将任何字符串写入一个打开的文件。需要重点注意的是，Python字符串可以是二进制数据，而不是仅仅是文字。
write()方法不会在字符串的结尾添加换行符('\n')
"""
# 打开一个文件
fileObject = open("foo.txt","wb")
fileObject.write("Hello python!\nHello java!\n")
# 关闭一个文件
fileObject.close()
print  "文件是否关闭：",fileObject.closed

# read（）方法从一个打开的文件中读取一个字符串。需要重点注意的是，Python字符串可以是二进制数据，而不是仅仅是文字。
# 打开一个文件
fo = open("foo.txt", "r+")
# str = fo.read(10)
str = fo.read()
print "读取的字符串是 : ", str
# 关闭打开的文件
fo.close()

"""
tell()方法告诉你文件内的当前位置；换句话说，下一次的读写会发生在文件开头这么多字节之后。
seek（offset [,from]）方法改变当前文件的位置。Offset变量表示要移动的字节数。From变量指定开始移动字节的参考位置。
如果from被设为0，这意味着将文件的开头作为移动字节的参考位置。如果设为1，则使用当前的位置作为参考位置。如果它被设为2，那么该文件的末尾将作为参考位置。 
"""
# 打开一个文件
fo = open("foo.txt", "r+")
str = fo.read(10);
print "读取的字符串是 : ", str

# 查找当前位置
position = fo.tell();
print "当前文件位置 : ", position

# 把指针再次重新定位到文件开头
position = fo.seek(0, 0);
str = fo.read(10);
print "重新读取字符串 : ", str
# 关闭打开的文件
fo.close()

#  rename()方法需要两个参数，当前的文件名和新文件名。
import os
# 重命名文件foo.txt到foo2.txt。
#os.rename("foo.txt", "foo2.txt")

# remove()方法删除文件，需要提供要删除的文件名作为参数。
#os.remove("foo2.txt")

# mkdir()方法创建一个新目录
# 创建目录haha
# os.mkdir("haha")

# chdir()方法来改变当前的目录
# 将当前目录改为haha
# os.chdir("haha")
print "当前目录：",os.getcwd() # getcwd()方法显示当前的工作目录

"""
rmdir()方法删除目录，目录名称以参数传递。
在删除这个目录之前，它的所有内容应该先被清除。 
"""
os.rmdir('haha')