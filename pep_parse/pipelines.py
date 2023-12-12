import datetime as dt
from collections import defaultdict

from pep_parse.settings import BASE_DIR, DATETIME_FORMAT

RESULTS_DIR = BASE_DIR.parent / 'results'


class PepParsePipeline:
    def open_spider(self, spider):
        self.count_pep_per_status = defaultdict(int)

    def process_item(self, item, spider):
        self.count_pep_per_status[item.get('status')] += 1
        return item

    def close_spider(self, spider):
        now = dt.datetime.now()
        now_formatted = now.strftime(DATETIME_FORMAT)
        file_name = f'status_summary_{now_formatted}.csv'
        total = sum(self.count_pep_per_status.values())
        with open(f'{RESULTS_DIR}/{file_name}',
                  mode='w', encoding='utf-8') as f:
            f.write('Статус,Количество\n')
            for status, count in self.count_pep_per_status.items():
                f.write(f'{status}, {count}\n')
            f.write(f'Total,{total}\n')
