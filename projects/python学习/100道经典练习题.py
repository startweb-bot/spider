# -*- coding = utf-8 -*-
# @time : 2020/12/26 21:57
# @Author : 王振朋
# @File : 100道经典练习题.py
# @Software : PyCharm

# # 程序1 有1，2，3，4个数字，能组成多个不相同i的数字？都是多少
# for i in range(1,5):
#     for j in range(1,5):
#         for k in range(1,5):
#             if(i!=k)&(i!=j)&(j!=k):
#                 print (i,j,k)

# #  程序2 利润<=10万,提10%  <=20万,提7.5%   <=40万,提5%   <=60万,提3%   <=100万,1.5%  >100万，1%
# bonus1 = 100000*0.1
# bonus2 = bonus1 + 100000*0.075
# bonus4 = bonus2 + 200000*0.05
# bonus6 = bonus4 + 200000*0.03
# bonus10 = bonus6 + 400000*0.015
#
# i = int(input('imput gain:\n'))
# if i<=100000:
#     bonus=i*0.1
# elif i<=200000:
#     bonus=bonus1+(i-100000)*0.075
# elif i<=400000:
#     bonus=bonus2+(i-200000)*0.05
# elif i<=600000:
#     bonus=bonus4+(i-400000)*0.03
# elif i<=1000000:
#     bonus=bonus6+(i-600000)*0.015
# else:
#     bonus=bonus10+(i-1000000)*0.01
# print('bonus=',bonus)

# #程序3 一个整数, 加100是完全平方数, 再加268是完全平方数, 该数是
# #include "math.h"
# import math
# for i in range(10000):
#     #转化为整数值
#     x=int(math.sqrt(i+100))
#     y=int(math.sqrt(i+368))
#     if(x*x==i+100)and(y*y==i+368):
#         print(i)

# #程序4 输入某年某月某日,判断这一天是这一年的第几天
# year = int(input('year:\n'))
# month = int(input('month:\n'))
# day = int(input('day:\n'))
#
# months = (0,31,59,90,120,151,181,212,243,273,304,334)
# if 0<= month <=12:
#     sum = months[month-1]
# else:
#     print('data error')
# sum += day
# leap = 0
# if(year%400==0) or ((year%4==0)and(year%100!=0)):
#     leap = 1
# if(leap == 1)and(month > 2):
#     sum += 1
# print('it is the %dth day.'%sum)

#程序5 输入三个整数x,y,z, 把这三个数由小到大输出。
l = []
for i in range(3):
    x = int(input('integer:\n'))
    l.append(x)
l.sort()
print(l)



