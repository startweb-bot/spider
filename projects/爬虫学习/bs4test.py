# -*- coding = utf-8 -*-
# @time : 2020/12/27 9:44
# @Author : 王振朋
# @File : bs4test.py
# @Software : PyCharm

#BeautifulSoup4将复杂HTML文档转换成一个复杂的树形结构，每个节点都是Python对象，所有对象可以归纳为4种：
#  - Tag
#  - NavigableString
#  - BeautifulSoup
#  - Comment

# import requests
# url = 'https://www.baidu.com/'
# headers = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36 Edg/87.0.664.41'
# }
# response = requests.get(url=url,headers=headers).text
# print(response)
# with open("./baidu.html","wb") as file:
#     file.write(response.encode('utf-8'))

from bs4 import BeautifulSoup
file = open("./baidu.html","rb")
html = file.read()
bs = BeautifulSoup(html,"html.parser")
# print(bs.title)
# print(bs.a)
# print(bs.head)
# print(type(bs.head))
#1.Tag 标签及其内容：拿到它所找到的第一个内容
# print(bs.title.string)
# print(type(bs.title.string))
#2.NavigableString 标签里的内容(字符串)
# print(bs.a.attrs)
# print(type(bs))
#3.BeautifulSoup 表示整个文档
# print(bs.name)
# print(bs)
# print(bs.a.string)
# print(type(bs.a.string))
#4.Comment是一个特殊的NavigableString,输出的内容不包含注释符号

#文档的遍历
# print(bs.head.contents)
# print(bs.head.contents[1])   #更多内容搜遍历文档树

#文档的搜索
 # (1)find_all()
# t_list = bs.find_all("a")

import re
#(2)正则表达式搜索: 使用search()方法来匹配内容
# t_list = bs.find_all(re.compile("a"))

#(3)传入一个函数(方法),根据函数的要求来搜索
# def name_is_exists(tag):
#     return tag.has_attr("name")
# t_list = bs.find_all(name_is_exists)
# for item in t_list:
#     print(item)

#2.kwargs     参数
# t_list = bs.find_all(id="head")
# t_list = bs.find_all(href="http://news.baidu.com")
# t_list = bs.find_all(class_=True)
# for item in t_list:
#     print(item)

#3.text参数
# t_list = bs.find_all(text = "hao123")
# t_list = bs.find_all(text = ["hao123","贴吧","地图"])
# t_list = bs.find_all(text = re.compile("\d"))   #应用正则表达式来查找包含特定文本的内容(标签里的字符串)
# for item in t_list:
#     print(item)

#4.limit参数
# t_list = bs.find_all("a",limit=3)
# for item in t_list:
#     print(item)

#css选择器
# t_list = bs.select('title')      #通过标签来查找
# t_list = bs.select(".mnav")      #通过类名来查找
# t_list = bs.select("#u1")        #通过id来查找
# t_list = bs.select('a[href="#"]')      #通过属性来查找
# t_list = bs.select("head > title")     #通过子标签来查找
t_list = bs.select(".mnav ~ .bri")
print(t_list[0].get_text())




