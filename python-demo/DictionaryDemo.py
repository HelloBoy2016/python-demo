# !/usr/bin/python
# -*- coding: UTF-8 -*-
# 字典的每个键值(key=>value)对用冒号(:)分割，每个对之间用逗号(,)分割，整个字典包括在花括号{}中
# 可以理解成java中的map
# 访问字典里的值
dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}
print "dict['Name']: ", dict['Name']
print "dict['Age']: ", dict['Age']
# print dict['weight'] 如果key错误报错KeyError: 'weight'

# 向字典添加新内容的方法是增加新的键/值对
dict2 = {'Name': 'xiaowen', 'Age': 7, 'Class': 'First'}
dict2['name'] = 'xiaoqiang'
dict2['weight'] = '60kg'
print  dict2['name']
print  dict2['weight']

# 能删单一的元素也能清空字典，清空只需一项操作。
# 显示删除一个字典用del命令
dict3 = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}
del dict3['Name']  # 删除键是'Name'的条目
dict3.clear()  # 清空词典所有条目
del dict3  # 删除词典
# print "dict['Age']: ", dict3['Age'] 报错 NameError: name 'dict3' is not defined

# 字典值可以是任意数值类型
dict4 = {'a':[1,2,3,4,5]} # 值为列表
print dict4['a'][1]
dict5 ={'a':{'b':'c'}} # 值为字典
print dict5['a']['b']

#1. 用户添加单词和含义 2. 查找单词
dictionary = {}
flag = 'a' # 判断循环标志
query = 'y' # 查看字典标志
exist = 'y' # 单词存在标志
while flag == 'a' or 's' :
    flag = raw_input("请输入：a:添加单词 s:查找单词")
    if flag == "a" :                             # 开启
        word = raw_input("请输入单词:")
        defintion = raw_input("请输入单词含义:")
        dictionary[str(word)] = str(defintion)  # 添加字典
        print "添加成功!"
        query = raw_input("请输入：y:查看字典 n:不查看字典")   #
        if query == 'y':
            print '字典：',dictionary
        else :
            continue
    elif flag == 's':
        check_word = raw_input("请输入要查找的单词:")  # 检索a
        for key in sorted(dictionary.keys()):            # yes
            if str(check_word) == key:
                print "该单词存在! 单词:%s,含义:%s" % (key,dictionary[key])
                break
            else:                                       # no
                exist = 'n'
        if exist == 'n':
            print "抱歉，该单词不存在，我们会继续增强我们的单词的！"
    else:                               # 停止
        print "下次请换个姿势输入！！！"
        break