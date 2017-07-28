# !/usr/bin/python
# -*- coding: UTF-8 -*-
count = 0
while(count < 10):
    print 'this count = ', count
    count +=1

# break 来跳过循环，continue 用于跳过该次循环
i = 0
while i < 10:
    i += 1
    if i%2 <> 0:
        continue
    print i

j = 0
while 1:
    print j
    j +=1
    if j > 10:
        break

# 一个石头剪刀布的小游戏
import random
while 1:
    s = int(random.randint(1, 3))
    if s == 1:
        ind = "石头"
    elif s == 2:
        ind = "剪子"
    elif s == 3:
        ind = "布"
    m = raw_input('输入 石头、剪子、布,输入"end"结束游戏:')
    blist = ['石头', "剪子", "布"]
    if (m not in blist) and (m != 'end'):
        print "输入错误，请重新输入！"
    elif (m not in blist) and (m == 'end'):
        print "\n游戏退出中..."
        break
    elif m == ind :
        print "电脑出了： " + ind + "，平局！"
    elif (m == '石头' and ind =='剪子') or (m == '剪子' and ind =='布') or (m == '布' and ind =='石头'):
        print "电脑出了： " + ind +"，你赢了！"
    elif (m == '石头' and ind =='布') or (m == '剪子' and ind =='石头') or (m == '布' and ind =='剪子'):
        print "电脑出了： " + ind +"，你输了！"

# 猜大小游戏
import random
s = int(random.uniform(1,10))
m = int(input('输入整数:'))
while m != s:
	if m > s:
		print('大了')
		m = int(input('输入整数:'))
	if m < s:
		print('小了')
		m = int(input('输入整数:'))
	if m == s:
		print('OK')
		break;

# 摇塞子游戏
import random
import sys
import time

result = []
while True:
    result.append(int(random.uniform(1,7)))
    result.append(int(random.uniform(1,7)))
    result.append(int(random.uniform(1,7)))
    print result
    count = 0
    index = 2
    pointStr = ""
    while index >= 0:
        currPoint = result[index]
        count += currPoint
        index -= 1
        pointStr += " "
        pointStr += str(currPoint)
    if count <= 11:
        sys.stdout.write(pointStr + " -> " + "小" + "\n")
        time.sleep( 1 )   # 睡眠一秒
    else:
        sys.stdout.write(pointStr + " -> " + "大" + "\n")
        time.sleep( 1 )   # 睡眠一秒
    result = []