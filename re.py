'''
<div class="thumb">

<a href="/article/123814885" target="_blank">
<img src="//pic.qiushibaike.com/system/pictures/12381/123814885/medium/1OQTGVY8LB2RQIOQ.jpg" alt="糗事#123814885" class="illustration" width="100%" height="auto">
</a>
</div>

ex = '<div class="thumb">.*?<img src="(.*?)" alt.*?</div>'
'''

#!/usr/bin/env python
# -*- coding:utf-8 -*-
import requests
import re
import os
#需求:爬取糗事百科中热图板块下所有的糗图图片
#if _name_ == "_main_":
#创建一个文件夹，保存所有的图片
if not os.path.exists('./qiutuLibs'):
    os.mkdir('./qiutuLibs')
url = 'https://www.qiushibaike.com/imgrank/'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36 Edg/87.0.664.41'
}
    #使用通用爬虫对url对应的一整张页面进行爬取
page_text = requests.get(url=url,headers=headers).text

    #使用聚焦爬虫将页面中所有的糗图进行解析/提取
ex = '<div class="thumb">.*?<img src="(.*?)" alt.*?</div>'
img_src_list = re.findall(ex,page_text,re.S)
#print(img_src_list)
for src in img_src_list:
    #拼接出一个完整的图片url
    src = 'https:'+src
    #请求到了图片的二进制数据
    img_data = requests.get(url=src,headers=headers).content
    #生成图片名称
    img_name = src.split('/')[-1]
    #图片存储的路径
    imgPath = './qiutuLibs/'+img_name
    with open(imgPath,'wb') as fp:
        fp.write(img_data)
        print(img_name,'下载成功！！！')
