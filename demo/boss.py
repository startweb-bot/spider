# -*- coding = utf-8 -*-
# @time : 2020/12/22 23:00
# @Author : 王振朋
# @File : boss.py
# @Software : PyCharm

from selenium import webdriver
from lxml import etree
from time import sleep
#实例化一个浏览器对象（传入浏览器的驱动程序）
bro = webdriver.Chrome(executable_path='./chromedriver')
#让浏览器发起一个指定url对应请求
bro.get('https://www.zhipin.com/job_detail/?query=python&city=101270100&industry=&position=')

#page_source获取浏览器当前页面的页面源码数据
page_text = bro.page_source

#解析企业名称
tree = etree.HTML(page_text)
li_list = tree.xpath('//*[@id="main"]/div/div[2]/ul/li')
# print(page_text)
for li in li_list:
    name = li.xpath('./div/div[1]/div[1]/div/div[1]/span[1]/a/@title')[0]
    print(name)
sleep(5)
bro.quit()




