import scrapy


class XiaohuaSpider(scrapy.Spider):
    name = 'xiaohua'
    # allowed_domains = ['www.xxx.com']
    start_urls = ['http://www.521609.com/tuku/hdxz/']

    #生成一个通用的url模板(不可变)
    url = 'http://www.521609.com/tuku/hdxz/index_%d.html'
    page_num = 2

    def parse(self, response):
        li_list = response.xpath('/html/body/div[4]/div[3]/ul/li')
        for li in li_list:
            img_name = li.xpath('./a/@title').extract_first()
            print(img_name)

        if self.page_num <= 3:
            new_url = format(self.url%self.page_num)
            self.page_num += 1
            #手动请求发送: callback回调函数是专门用作于数据解析
            yield scrapy.Request(url=new_url,callback=self.parse)
