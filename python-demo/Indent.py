# !/usr/bin/python
# -*- coding: UTF-8 -*-
import sys;
# 没有严格缩进，在执行时会报错
# Python 的代码块不使用大括号 {} 来控制类，函数以及其他逻辑判断。python 最具特色的就是用缩进来写模块。

if True:
    print "Answer";
    print "True";
else:
    print "Answer";
    print "False";

#下面的程序执行后就会等待用户输入，按回车键后就会退出：
raw_input("\n\nPress the enter key to exit.");


x = 'hahaha';
sys.stdout.write(x + '\n')
