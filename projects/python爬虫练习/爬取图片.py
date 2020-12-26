#！/usr/bin/env python
# -*- coding: utf-8 -*-
'''
import requests
#if _name_ == "_main_":
    #如何爬取图片数据
url = 'https://pic.qiushibaike.com/system/pictures/12380/123806109/medium/PIHJE56TA4QRHIRB.jpg'
    # text(字符串)  content(二进制)   json() (对象)
img_data = requests.get(url=url).content

with open('./qiutu.jpg','wb') as fp:
    fp.write(img_data)
'''

'''
单字符:
    . : 除换行以外所有字符
    [] : [aoe] [a-w] 匹配集合中任意一个字符
    \d : 数字 [0-9]
    \D : 非数字
    \w : 数字、字母、下划线、中文
    \W : 非\w
    \s : 所有的空白字符包，括空格、制表符、换页符等等。等价于[ \f\n\r\t\v]
    \S : 非空白
数量修饰:
    * : 任意多次 >=0
    + : 至少1次 >=1
    ? : 可有可无 0次或者1次
    {m} : 固定m次 hello{3,}
    {m,} : 至少m次
    {m,n} : m-n次
边界:
    $ : 以某某结尾
    ^ : 以某某开头
分组:
    (ab)
贪婪模式:  .*
非贪婪(惰性)模式: .*?

re:I : 忽略大小写
re.M : 多行匹配
re.S : 单行匹配

re.sub(正则表达式,替换内容,字符串)
'''


import re
#提取出python
key = "javapythonc++php"
re.findall('python',key)[0]

#提取出hello world
key = "hello world"
re.findall('(.*)',key)[0]

#提取170
string = '我喜欢身高为170的女孩'
re.findall('\d+',string)

#提取出http://和https://
key = 'http://www.baidu.com and https://boob.com'
re.findall('http?s://',key)

#提取出hello
key = 'lalalahellohahaha' #输出hello
re.findall('<[Hh][Tt][mM][lL]>(.*)',key)

#提取出hit
key = 'bobo@hit.edu.com' #想要匹配到hit.
re.findall('h.*?\.',key)

#匹配sas和saas
key = 'saas and sas and saaas'
re.fandall('sa{1,2}s',key)



