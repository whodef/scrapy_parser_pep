import datetime as dt
import csv
from collections import Counter

from .constants import BASE_DIR, DATE_FORMAT, FIELDS_NAME


def write_results(status_summary):
    TOTAL_SUM = ('Total', sum(status_summary.values()))

    timestamp = dt.datetime.now().strftime(DATE_FORMAT)
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
        pass

    def open_spider(self, spider):
        self.status_summary = Counter()

    def process_item(self, item, spider):
        self.status_summary[item['status']] += 1
        return item

    def close_spider(self, spider):
        write_results(self.status_summary)
