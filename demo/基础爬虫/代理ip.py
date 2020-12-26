#需求：
import requests
url = 'http://ip.293.net/'
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36 Edg/87.0.664.47'
}

page_text = requests.get(url=url,headers=headers,proxies={"http":'http://180.122.104.201:4257'}).text

with open('ip.html','w',encoding='utf-8') as fp:
    fp.write(page_text)