from scrapy.cmdline import execute

# 第一种启动方式
# execute("scrapy crawl baidu".split())
# 第二种启动方式
# execute(["scrapy", "crawl", "baidu"])

execute(["scrapy", "crawl", "maoyan"])

# 导出数据为json文档
# execute(["scrapy", "crawl", "qidian", "-o", "dataFile/books.json"])

# 导出数据为xml文档
# execute(["scrapy", "crawl", "qidian", "-o", "dataFile/books.xml"])

# 导出数据为csv文档
# execute(["scrapy", "crawl", "qidian", "-o", "dataFile/books.csv"])
