import scrapy


class BossSpider(scrapy.Spider):
    name = 'boss'
    # allowed_domains = ['www.xxx.com']
    start_urls = ['https://www.zhipin.com/job_detail/?query=python&city=101270100&industry=&position=']

    def parse(self, response):
        li_list = response.xpath('/html/body/div[1]/div[3]/div/div[3]/ul/li')
        print(li_list)
        for li in li_list:
            job_name = li.xpath('./div/div[1]/div[1]/div/div[1]/span[1]/a/@title').extract_first()
            # // *[ @ id = "main"]/div/div[3]/ul/li[1]/div/div[1]/div[1]/div/div[1]/span[1]/a
            print(job_name)