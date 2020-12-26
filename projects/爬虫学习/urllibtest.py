# -*- coding = utf-8 -*-
# @time:2020/12/22 10:25
# @Author:王振朋
# @File:lianxi.py
# @Software:PyCharm

import urllib.request

# #获取一个get请求
# response = urllib.request.urlopen("http://www.baidu.com")
# print(response.read().decode('utf-8'))   #对获取到的网页源码进行utf-8解码

import urllib.parse
# data = bytes(urllib.parse.urlencode({"hello":"world"}),encoding="utf-8")
# response = urllib.request.urlopen("http://www.httpbin.org/post",data=data)
# print(response.read().decode("utf-8"))


#超时处理
# try:
#     response = urllib.request.urlopen("http://www.httpbin.org/get",timeout=0.01)
#     print(response.read().decode("utf-8"))
# except urllib.error.URLError as e:
#     print('time out!')

# response = urllib.request.urlopen("http://www.httpbin.org/get")
# print(response.status)

# response = urllib.request.urlopen("http://www.baidu.com")
# print(response.getheader("Server"))

# url = "http://www.httpbin.org/post"
# headers = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36 Edg/87.0.664.41'
# }
# data = bytes(urllib.parse.urlencode({"name":"eric"}),encoding="utf-8")
# req = urllib.request.Request(url=url,data=data,headers=headers,method="POST")
# response = urllib.request.urlopen(req)
# print(response.read().decode("utf-8"))

url = 'https://www.douban.com'
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36 Edg/87.0.664.41'
}
req = urllib.request.Request(url=url,headers=headers)
response = urllib.request.urlopen(req)
print(response.read().decode("utf-8"))


