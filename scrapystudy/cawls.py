from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

process = CrawlerProcess(get_project_settings())

# myspd1是爬虫名
# process.crawl('test')
# process.crawl('handan')
process.crawl('NjMuseum')
process.start()