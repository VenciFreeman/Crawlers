from scrapy import signals

class ZhihuspiderSpiderMiddleware(object):
    @classmethod
    def from_crawler(cls, crawler):
    
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_input(self, response, spider):
        return None

    def process_spider_output(self, response, result, spider):
        for i in result:
            yield i

    def process_spider_exception(self, response, exception, spider):
        pass

    def process_start_requests(self, start_requests, spider):
        for r in start_requests:
            yield r

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)

from faker import Faker
class ZhihuspiderDownloadmiddlewareRandomUseragent(object):
    def __init__(self):
        self.fake = Faker()

    def process_request(self,request,spider):
        request.headers.setdefault('User-Agent',self.fake.user_agent())