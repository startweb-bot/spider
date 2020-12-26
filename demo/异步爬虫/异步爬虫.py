# import requests
# from lxml import etree
# headers = {
#     'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36 Edg/87.0.664.47'
# }
# url = 'https://sc.chinaz.com/jianli/201203111431.htm'
#
# page_text = requests.get(url=url,headers=headers).text
#
# # //*[@id="down"]/div[2]/ul/li[1]
# # /html/body/div[8]/div[2]/div[2]/div[1]/div[8]/div[2]/ul/li[1]
# tree = etree.HTML(page_text)
# li_list = tree.xpath('//*[@id="down"]/div[2]/ul/li')
#
#
# temp = []
#
# for li in li_list:
#     a_url = li.xpath('./a/@href')[0]
#     #print(a_url)
#     temp.append(a_url)
#
#     with open('./1.txt','w') as fp:
#         fp.write(str(temp))
#         print(a_url,'下载成功！！！')



import requests
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36 Edg/87.0.664.47'
}
urls = [
    'http://downsc.chinaz.net/Files/DownLoad/jianli/202011/jianli14107.rar',
    'http://downsc.chinaz.net/Files/DownLoad/jianli/202011/jianli14107.rar',
    'http://downsc.chinaz.net/Files/DownLoad/jianli/202011/jianli14107.rar',
    'http://downsc.chinaz.net/Files/DownLoad/jianli/202011/jianli14107.rar',
    'http://downsc.chinaz.net/Files/DownLoad/jianli/202011/jianli14107.rar',
    'http://downsc.chinaz.net/Files/DownLoad/jianli/202011/jianli14107.rar',
    'http://downsc.chinaz.net/Files/DownLoad/jianli/202011/jianli14107.rar',
    'http://downsc.chinaz.net/Files/DownLoad/jianli/202011/jianli14107.rar',
    'http://downsc.chinaz.net/Files/DownLoad/jianli/202011/jianli14107.rar',
    'http://downsc.chinaz.com/Files/DownLoad/jianli/202011/jianli14107.rar',
    'http://downsc.chinaz.com/Files/DownLoad/jianli/202011/jianli14107.rar',
    'http://downsc.chinaz.com/Files/DownLoad/jianli/202011/jianli14107.rar'
]

def get_content(url):
    print('正在爬取: ',url)
    #get方法是一个阻塞的方法
    response = requests.get(url=url,headers=headers)
    if response.status_code == 200 :
        return response.content

def parse_content(content):
    print('响应数据的长度为: ',len(content))

for url in urls:
    content = get_content(url)
    parse_content(content)
