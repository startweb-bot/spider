# -*- coding = utf-8 -*-

import bs4       #网页解析，获取数据
import re        #正则表达式，进行文字匹配
import urllib.request,urllib.error          #制定URL,获取网页数据
import xlwt        #进行excel操作
import sqlite3      #进行SQLite数据库操作

def main():
    baseurl = "https://movie.douban.com/top250?start="
    #1.爬取网页
    datalist = getData(baseurl)
    savepath = ".\\豆瓣电影Top250.xls"
    # 3.保存数据
    # saveData(savepath)

    askURL("https://movie.douban.com/top250?start=")

#爬取网页
def getData(baseurl):
    datalist = []
    for i in range(0,10):       #调用获取页面信息的函数 10次
        url = baseurl + str(i*25)
        html = askURL(url)      #保存获取到的网页源码

        # 2.解析数据(逐一解析）
    return datalist

def askURL(url):
    head = {        #模拟浏览器头部信息，向豆瓣服务器发送消息
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36 Edg/87.0.664.41'
    }     #用户代理，告诉豆瓣服务器，我们是什么类型的机器浏览器(本质上是告诉浏览器，我们可以接收什么类型的数据)
    request = urllib.request.Request(url,headers=head)
    html = ""
    try:
        response = urllib.request.urlopen(request)
        # html = response.read().decode("utf-8")
        html = response
        print(html)
    except urllib.error.URLError as e:
        if hasattr(e,"code"):
            print(e,"code")
        if hasattr(e,"reason"):
            print(e.reason)

    return html

def saveData(savepath):
    pass


# 3.保存数据
if __name__ == '__main__':          #当程序执行时
    #调用函数
    main()

