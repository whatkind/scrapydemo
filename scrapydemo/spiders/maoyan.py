import scrapy
from scrapydemo.items import FilmsItem

class MaoyanSpider(scrapy.Spider):
    name = 'maoyan'
    allowed_domains = ['maoyan.com']
    start_urls = ['https://maoyan.com/films']

    def parse(self, response):
        titles = response.xpath('//div[@class="channel-detail movie-item-title"]/@title').extract()
        scopes = [scope.xpath('string(.)').extract_first() for scope in response.xpath('//div[@class="channel-detail channel-detail-orange"]')]
        # 第一种数据传输方式
        # for title, scope in zip(titles, scopes):
        #     yield {"title": title, "scope": scope}

        # 第二种数据传输方式
        item = FilmsItem()
        for title, scope in zip(titles, scopes):
            item['title'] = title
            item['scope'] = scope
            yield item
