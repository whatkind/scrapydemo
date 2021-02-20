import scrapy


class QidianSpider(scrapy.Spider):
    name = 'qidian'
    allowed_domains = ['qidian.com']
    start_urls = ['https://www.qidian.com/all']

    def parse(self, response):
        names = response.xpath('//h4/a/text()').extract()
        authors = response.xpath('//p[@class="author"]/a[@class="name"]/text()').extract()
        # print(names)
        # print(authors)
        books = []
        for name, author in zip(names, authors):
            books.append({'name': name, 'author': author})
        return books
