# ！/usr/bin/env python
# -*- coding: utf-8 -*-
import requests
from lxml import etree
#需求: 爬取58二手房中的房源信息
if __name__ == "__main__":
    headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36 Edg/87.0.664.47'
    }
    #爬取到页面源码数据
    url = 'https://cd.58.com/ershoufang/'
    page_text = requests.get(url=url,headers=headers).text

    #数据解析
    tree = etree.HTML(page_text)
    #存储的就是li标签对象
    li_list = tree.xpath('//ul[@class="house-list-wrap"]/li')
    fp = open('58.txt','w',encoding='utf-8')
    for li in li_list:
        title = li.xpath('./div[2]/h2/a/text()')[0]
        print(title)
        fp.write(title+'\n')