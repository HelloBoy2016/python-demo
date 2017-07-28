# !/usr/bin/python
# -*- coding: UTF-8 -*-

# 使用下标索引来访问列表中的值，同样你也可以使用方括号的形式截取字符
list = ['hello','xiaoming',25,'65kg']
print list[0]
print list[0:4]

# 对列表的数据项进行修改或更新，你也可以使用append()方法来添加列表项
name = ['xiaoming','xiaoqiang','xiaohua']
print 'name[1]',name[1]
name[1] = 'xiaoqiang_new'
print 'name[1]',name[1]
# 在列表末尾添加新对象
name.append('xiaowen')
print name

# ASCII转中文
print '\xc5\xc0\xb3\xe6'.decode('gbk')

# 删除列表元素
list2 = ['physics', 'chemistry', 1997, 2000]
print 'del before=',list2
del list2[2]
print 'del after=',list2

# Python列表截取
companyNames = ['Google', 'Alibaba', 'TenXun','BaiDu']
print companyNames[2] # 读取列表第3个元素
print companyNames[-2] # 读取列表倒数第二个元素
print companyNames[1:] # 从第二个元素开始截取列表

# 创建二维列表，将需要的参数写入 cols 和 rows
users = [['xiaoming',25,'50kg'],['xiaowen',23,'45kg']]
for user in users:
    print user