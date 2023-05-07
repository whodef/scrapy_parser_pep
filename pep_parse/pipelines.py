import csv
import datetime as dt
from collections import Counter
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent


class PepParsePipeline:
    def __init__(self):
        self.status_summary = Counter()

    def open_spider(self, spider):
        pass

    def process_item(self, item, spider):
        self.status_summary[item['status']] += 1
        return item

    @staticmethod
    def close_spider(self, status_summary, spider):
        now_formatted = dt.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
        results_dir = BASE_DIR / 'results'
        results_dir.mkdir(exist_ok=True)
        file_name = f'status_summary_{now_formatted}.csv'
        file_path = results_dir / file_name
        result = (
            [('Статус', 'Количество')]
            + status_summary.most_common() +
            [('Total', sum(status_summary.values()))]
        )

        with open(file_path, 'w', encoding='utf-8') as f:
            writer = csv.writer(f, dialect='unix')
            writer.writerows(result)
