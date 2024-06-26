import logging
import re

import scrapy

from pep_parse.items import PepParseItem


class PepSpider(scrapy.Spider):
    name = 'pep'
    allowed_domains = ['peps.python.org']
    start_urls = ['https://peps.python.org/']

    def parse(self, response):
        """Получает ссылки на страницы PEP."""
        all_peps = response.css(
            'section#index-by-category tbody a::attr(href)')
        for pep_link in all_peps:
            yield response.follow(pep_link, callback=self.parse_pep)

    def parse_pep(self, response):
        """Со страницы PEP получает номер, название и статус."""
        raw_title = ' '.join(response.xpath(
            '//h1[@class="page-title"]//text()').getall())
        cleaned_title = ' '.join(raw_title.split())
        pattern = re.match(r'PEP (?P<number>\d+) – (?P<title>.+)',
                           cleaned_title)
        if pattern:
            yield PepParseItem(
                {'number': pattern.group('number'),
                 'name': pattern.group('title'),
                 'status': response.css(
                     'dt:contains("Status") + dd abbr::text').get()})
        else:
            self.log(f'По адресу {response.url} не найден заголовок',
                     level=logging.WARNING)
