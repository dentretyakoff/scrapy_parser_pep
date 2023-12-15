import csv
import datetime as dt
from collections import defaultdict
from pathlib import Path

from pep_parse.settings import DATETIME_FORMAT


BASE_DIR = Path(__file__).parent.parent


class PepParsePipeline:
    """При обходе страниц PEP подсчитывает количество уникальных статусов."""
    def open_spider(self, spider):
        self.count_pep_per_status = defaultdict(int)

    def process_item(self, item, spider):
        self.count_pep_per_status[item.get('status')] += 1
        return item

    def close_spider(self, spider):
        now = dt.datetime.now()
        now_formatted = now.strftime(DATETIME_FORMAT)
        file_name = f'status_summary_{now_formatted}.csv'
        result = [('Статус', 'Количество')]
        result.extend([(k, v) for k, v in self.count_pep_per_status.items()])
        result.append(('Total', sum(self.count_pep_per_status.values())))
        with open(BASE_DIR / 'results' / file_name,
                  mode='w', encoding='utf-8') as csvfile:
            writer = csv.writer(csvfile, dialect='unix')
            writer.writerows(result)
