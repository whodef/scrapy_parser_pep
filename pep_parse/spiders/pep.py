import scrapy
import re

from pep_parse.items import PepParseItem
from pep_parse.constants import STATUS_SELECTOR


class PepSpider(scrapy.Spider):
    name = 'pep'
    allowed_domains = ['peps.python.org']
    start_urls = ['https://peps.python.org/']

    def parse(self, response, **kwargs):
        pep_urls = response.css(
            'section#numerical-index tr > td:nth-child(3) a'
        )
        yield from response.follow_all(pep_urls, callback=self.parse_pep)

    @staticmethod
    def parse_pep(response):
        title_text = response.css('h1.page-title::text').get().strip()
        status = response.css(STATUS_SELECTOR).get()

        match = re.match(r'PEP (\d+) - (.+)', title_text)
        if match:
            number, name = match.groups()
        else:
            number, name = None, None

        pep_info = {
            'number': number,
            'name': name,
            'status': status,
        }

        yield PepParseItem(pep_info)
