# -*- coding = utf-8 -*-
# @time : 2020/12/29 14:16
# @Author : 王振朋
# @File : sqlitetest.py
# @Software : PyCharm

import sqlite3
# #1.创建数据库
# conn = sqlite3.connect("test.db")       #打开或创建数据库文件
# print("Opened database successfully")

#2.创建数据表
# conn = sqlite3.connect("test.db")       #打开或创建数据库文件
# print("成功打开数据库")
# c = conn.cursor()       #获取游标
# sql = '''
#     create table company
#         (id int primary key not null,
#         name text not null,
#         age int not null,
#         address char(50),
#         salary real);
# '''
# c.execute(sql)          #执行sql语句
# conn.commit()           #提交数据库操作
# conn.close()            #关闭数据库连接
# print("成功创表")

# #3.插入数据
# conn = sqlite3.connect("test.db")       #打开或创建数据库文件
# print("成功打开数据库")
# c = conn.cursor()       #获取游标
# sql1 = '''
#     insert into company(id,name,age,address,salary)
#     values(1,'张三',32,"成都",8000)
# '''
# sql2 = '''
#     insert into company(id,name,age,address,salary)
#     values(2,'李四',30,"郑州",15000)
# '''
# c.execute(sql1)          #执行sql语句
# c.execute(sql2)          #执行sql语句
# conn.commit()           #提交数据库操作
# conn.close()            #关闭数据库连接
# print("插入数据完毕")

#4.查询数据
conn = sqlite3.connect("test.db")       #打开或创建数据库文件
print("成功打开数据库")
c = conn.cursor()       #获取游标
sql = "select id,name,address,salary from company"
cursor = c.execute(sql)          #执行sql语句
for row in cursor:
    print("id= ",row[0])
    print("name= ",row[1])
    print("address= ",row[2])
    print("salary= ",row[3],"\n")
conn.close()            #关闭数据库连接
print("查询数据完毕")