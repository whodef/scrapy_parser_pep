import csv
import datetime as dt
from collections import Counter
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent
FIELDS_NAME = ('Статус', 'Количество')
DATE_FORMAT = '%Y-%m-%dT%H-%M-%S'
TIME_NOW = dt.datetime.now().strftime(DATE_FORMAT)


def write_results(status_summary):
    TOTAL_SUM = ('Total', sum(status_summary.values()))

    timestamp = TIME_NOW
    results_dir = BASE_DIR / 'results'
    results_dir.mkdir(exist_ok=True)
    file_name = f'status_summary_{timestamp}.csv'
    file_path = results_dir / file_name
    result = (
        [FIELDS_NAME] + status_summary.most_common() + [TOTAL_SUM]
    )

    with open(file_path, 'w', encoding='utf-8') as f:
        writer = csv.writer(f, dialect='unix')
        writer.writerows(result)


class PepParsePipeline:
    def __init__(self):
        self.status_summary = Counter()

    def open_spider(self, spider):
        pass

    def process_item(self, item, spider):
        self.status_summary[item['status']] += 1
        return item

    def close_spider(self, spider):
        write_results(self.status_summary)
