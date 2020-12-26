#-*- codeing = utf-8 -*-
#@Time : 2020/7/11 21:57
#@Author : wang
#@File : hello.py
#@Software : PyCharm

print("hello world") #这是单行注释

'''
这是第一行注释
这是第二行注释

'''
'''
print("这是标准变量")
a = 10
print("这是变量:",a)
#格式化输出
age = 18
print("我的名字是%s,我的国家是%s"%("xiaoming","zhongguo"))
print("我的年龄是 %d 岁" %age)
print("aaa","bbb","ccc")
print("www","baidu","com",sep=".")
print("hello", end="")
print("world", end="\t")
print("wang", end="\n")
print("end")
'''
'''
password = input("请输入密码:")
print("您刚刚输入的密码是:",password)
'''
'''
#a = 10
#a = "abc"
a = input("输入 : ")
print(type(a))

print("请输入一个数字：%s" %a)
'''
a = int("123")
print(type(a))
b = a + 100
print(b)

c = int (input("输入c ："))
print ("输入了一个数字 ：%d" %c)
