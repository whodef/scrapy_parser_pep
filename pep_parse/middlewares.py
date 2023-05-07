"""
См. документацию
https://docs.scrapy.org/en/latest/topics/spider-middleware.html#writing-your-own-spider-middleware
"""

from scrapy import signals


class PepParseSpiderMiddleware:
    @classmethod
    def from_crawler(cls, crawler):
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    @staticmethod
    def process_spider_input(self, response, spider):
        return None

    @staticmethod
    def process_spider_output(self, response, result, spider):
        for i in result:
            yield i

    @staticmethod
    def process_spider_exception(self, response, exception, spider):
        pass

    @staticmethod
    def process_start_requests(self, start_requests, spider):
        for r in start_requests:
            yield r

    @staticmethod
    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)


class PepParseDownloaderMiddleware:
    @classmethod
    def from_crawler(cls, crawler):
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    @staticmethod
    def process_request(self, request, spider):
        return None

    @staticmethod
    def process_response(self, request, response, spider):
        return response

    def process_exception(self, request, exception, spider):
        pass

    @staticmethod
    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)
