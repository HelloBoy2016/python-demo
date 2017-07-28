# !/usr/bin/python
# -*- coding: UTF-8 -*-

# 遍历字符串
for ch in 'hello':
    print ch

# 遍历list
names = ['xiaoming','xiaohua','xiaoqiang']
for name in names:
    print 'name = ',name

# 通过索引遍历
fruits = ['banana', 'apple', 'mango']
for index in range(len(fruits)):
    print '当前水果 :', fruits[index]
print "Good bye!"

# 使用内置 enumerate 函数进行遍历:
sequence = [12, 34, 34, 23, 45, 76, 89]
for i, j in enumerate(sequence):
    print i,j

# 输出 2 到 100 简的质数
prime = []
for num in range(2,100):  # 迭代 2 到 100 之间的数字
   for i in range(2,num): # 根据因子迭代
      if num%i == 0:      # 确定第一个因子
         break            # 跳出当前循环
   else:                  # 循环的 else 部分
      prime.append(num)
print prime

# 打印空心等边三角形
rows = int(raw_input('输入行数：'))
for i in range(0, rows):
    for k in range(0, 2 * rows - 1):
        if (i != rows - 1) and (k == rows - i - 1 or k == rows + i - 1):
            print " * ",
        elif i == rows - 1:
            if k % 2 == 0:
                print " * ",
            else:
                print "   ",
        else:
            print "   ",
    print "\n"

# 打印三角形
rows2 = int(raw_input('输入行数：'))
for i in range(0,rows2):
    for k in range(0,i+1):
        print k,
        k +=1
    i +=1
    print "\n"
