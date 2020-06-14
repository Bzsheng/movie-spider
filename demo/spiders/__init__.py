# This package will contain the spiders of your Scrapy project
#
# Please refer to the documentation for information on how to create and manage
# your spiders.
import scrapy
from demo.items import movieItem
from scrapy.selector import Selector

class movieSpider(scrapy.Spider):
    name = 'movie'
    allowed_domians = ['movie.douban.com']

    def __init__(self, *args, **kwargs):
        super(movieSpider,self).__init__(*args, **kwargs)
        self.start_urls = ['https://movie.douban.com/top250?start=' + str(x) for x in range(0, 250 ,25)]

    def parse(self, response):
        result = Selector(response)
        movie_list = result.xpath('//*[@class="item"]')
        for movie in movie_list:
            item = movieItem()

            title = movie.xpath('.//img/@alt').extract()[0]
            url = movie.xpath('.//img/@src').extract()[0]

            has_info = movie.xpath('.//span[@class="inq"]')
            if has_info:
                info = movie.xpath('.//span[@class="inq"]/text()').extract()[0]
            else:
                info = ''
            # print(title)
            # print(url)
            # print(info)
            item['title'] = title
            item['url'] = url
            item['info'] = info
            yield item