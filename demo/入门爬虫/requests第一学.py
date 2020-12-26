# -*- coding:utf-8 -*-
# 需求: 爬取搜狗首页的页面数据
import requests
#if _name_ == "_main_":
    #step 1:指定url
url = 'https://www.sogou.com/'
    #step 2:发起请求
    #get方法会返回一个响应数据
response = requests.get(url=url)
    #step 3:获取响应数据.text返回的是字符串形式的响应数据
page_text = response.text
print(page_text)
    #step 4:持久化存储
with open('./sogou.html','w',encoding='utf-8') as fp:
    fp.write(page_text)
print('爬取数据结束！！！')