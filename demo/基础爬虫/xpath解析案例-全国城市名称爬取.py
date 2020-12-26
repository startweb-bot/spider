# ！/usr/bin/env python
# -*- coding:utf-8 -*-
import requests
from lxml import etree
#项目需求: 解析出所有城市名称https://www.aqistudy.cn/historydata/
if __name__ == "__main__":
    # headers = {
    #     'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36 Edg/87.0.664.47'
    # }
    # url = 'https://www.aqistudy.cn/historydata/'
    # page_text = requests.get(url=url,headers=headers).text
    #
    # tree = etree.HTML(page_text)
    # host_li_list = tree.xpath('//div[@class="bottom"]/ul/li')
    # all_city_names = []
    # #解析到了热门城市的城市名称
    # for li in host_li_list:
    #     hot_city_name = li.xpath('./a/text()')[0]
    #     all_city_names.append(hot_city_name)
    #
    # #解析的是全部城市的名称
    # city_names_list = tree.xpath('//div[@class="bottom"]/ul/div[2]/li')
    # for li in city_names_list:
    #     city_name = li.xpath('./a/text()')[0]
    #     all_city_names.append(city_name)
    #
    # print(all_city_names,len(all_city_names))
    headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36 Edg/87.0.664.47'
    }
    url = 'https://www.aqistudy.cn/historydata/'
    page_text = requests.get(url=url,headers=headers).text

    tree = etree.HTML(page_text)
    #解析到热门城市和所有城市对应的a标签
    # //div[@class="bottom"]/ul/li/a          热门城市a标签的层级关系
    # //div[@class="bottom"]/ul/div[2]/li/a   全部城市a标签的层级关系
    a_list = tree.xpath('//div[@class="bottom"]/ul/li/a | //div[@class="bottom"]/ul/div[2]/li/a')
    all_city_names = []
    for a in a_list:
        city_name = a.xpath('./text()')[0]
        all_city_names.append(city_name)
    print(all_city_names,len(all_city_names))