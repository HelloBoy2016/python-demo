# !/usr/bin/python
# -*- coding: UTF-8 -*-
import pymysql
import logging

def mysqlConnTest(event, context):
    logger = logging.getLogger()

    # 连接配置信息
    config = {
         'host':'198.19.23.3',
         'port':3306,
         'user':'root',
         'password':'root123',
         'db':'sudiyi-tower-detection',
         'charset':'gbk',
         'cursorclass':pymysql.cursors.DictCursor,
         }

    # 执行sql语句
    try:
        # 创建连接
        connection = pymysql.connect(**config)

        with connection.cursor() as cursor:
            # 执行sql语句，进行查询
            sql = 'SELECT id,user_name,user_pwd,role_name FROM user'
            cursor.execute(sql)
            # 获取查询结果
            results = cursor.fetchall()
            print results
            for row in results:
                id = row['id']
                userName = row['user_name']
                userPwd = row['user_pwd']
                roleName = row['role_name']
                print "id:%s,userName:%s,userPwd:%s,roleName:%s" % (id,userName,userPwd,roleName)
        # 没有设置默认自动提交，需要主动提交，以保存所执行的语句
        connection.commit()
    except:
        # 发生错误时回滚
        logger.info("发生错误时回滚")
        connection.rollback()
    finally:
        # 关闭数据库连接
        logger.info("关闭数据库连接")
        connection.close();
    return  results
