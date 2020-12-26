#-*- codeing = utf-8 -*-
#@Time : 2020/8/2 15:03
#@Author : wang
#@File : demo1.py
#@Software : PyCharm

'''
if 2:
    print("True")
    print("answer")
else :
    print("False")
print("end")
'''

'''
score = 90

if score >= 90 and score <= 100:
    print("本次考试 ，等级为A")
elif score >= 80 and score < 90:
    print("本次考试 ，等级为B")
elif score >= 70 and score < 80:
    print("本次考试 ，等级为C")
elif score >= 60 and score < 70:
    print("本次考试 ，等级为D")
else :           #else 和 elif一起使用
    print("本次考试 ，等级为E")
'''

'''
xingbie = 0 #1代表男生，0代表女生
danshen = 0 #1代表单身，0代表有男/女朋友

if xingbie == 1:
    print("男生")
    if danshen == 1:
        print("我给你介绍一个吧？")
    else:
        print("你给我介绍一个吧？")
else:
    print("女生")
    if danshen == 1:
        print("我给你介绍一个吧？")
    else:
        print("你给我介绍一个吧？")
'''
'''
# 电脑随机生成一个数
import random
number2 = random.randint(0,2)

computer = 0
if number2 == 0:
    computer = "剪刀（0）"
elif number2 == 1:
    computer = "石头（1）"
elif number == 2:
    computer = "布（2）"
# 用户输入
number1 = int(input("请输入一个数字，0代表剪刀，1代表石头，2代表布："))

user = 0
if number1 == 0:
    user = "剪刀（0）"
elif number1 == 1:
    user = "石头（1）"
elif number1 == 2:
    user = "布（2）"

# 打印用户输入的and电脑随机生成的
print("你输入的是：", user)
print("随机生成的是：", computer)

# 判断输赢
if number1 == number2:
    print("平手，再来一次")
elif number1 == 0 and number2 == 1:
    print("抱歉，你输了。")
elif number1 == 0 and number2 == 2:
    print("恭喜你赢了！！！")
elif number1 == 1 and number2 == 0:
    print("恭喜你赢了！！！")
elif number1 == 1 and number2 == 2:
    print("抱歉，你输了。")
elif number1 == 2 and number2 == 0:
    print("抱歉，你输了。")
elif number1 == 2 and number2 == 1:
    print("恭喜你赢了！！！")
'''
'''
for i in range(5):
    print(i)
'''
'''
for i in range(0,10,3):
    print(i)
'''
'''
for i in range(-10,-100,-30):
    print(i)
'''
'''
name = "chengdu"
for x in name:
    print(x,end="\t")
'''
'''
a = ["aa","bb","cc","dd"]
for i in range(len(a)):
    print(i,a[i])
'''

import random

offices = [[],[],[]]

names = ["A","B","C","D","E","F","G","H"]

for name in names:
    index = random.randint(0,2)
    offices[index].append(name)

i = 1
for office in offices:
    print("办公室%d 的人数为: %d"%(i,len(office)))
    i += 1
    for name in office:
        print("%s"%name,end="\t")
    print("\n")
    print("-"*15)