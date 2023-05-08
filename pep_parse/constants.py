from pathlib import Path


# Base Directory

BASE_DIR = Path(__file__).resolve().parent


# Formats

DATE_FORMAT = '%Y-%m-%dT%H-%M-%S'


# Constants

FIELDS_NAME = ('Статус', 'Количество')

STATUS_SELECTOR = 'dt:contains("Status") + dd > abbr::text'
