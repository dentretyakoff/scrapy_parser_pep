# Scrapy settings for pep_parse project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html
import datetime as dt
from pathlib import Path


BASE_DIR = Path(__file__).parent

BOT_NAME = 'pep_parse'

SPIDER_MODULES = ['pep_parse.spiders']
NEWSPIDER_MODULE = 'pep_parse.spiders'

# Obey robots.txt rules
ROBOTSTXT_OBEY = True

LOGS_DIR = BASE_DIR / 'logs'
LOGS_DIR.mkdir(exist_ok=True)
DATETIME_FORMAT = '%Y-%m-%d_%H-%M-%S'
NOW_FORMATTED = dt.datetime.now().strftime(DATETIME_FORMAT)

LOG_FILE = f'{LOGS_DIR}/scrapy_{NOW_FORMATTED}.log'
LOG_LEVEL = 'INFO'

FEEDS = {
    'results/pep_%(time)s.csv': {
        'format': 'csv',
        'fields': ['number', 'name', 'status'],
        'overwrite': True
    }
}

ITEM_PIPELINES = {
    'pep_parse.pipelines.PepParsePipeline': 300,
}
