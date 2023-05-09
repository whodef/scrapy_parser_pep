from pathlib import Path


# Base Directory

BASE_DIR = Path(__file__).resolve().parent


# Formats

DATE_FORMAT = '%Y-%m-%dT%H-%M-%S'


# Regular expressions

REG_EXP = r'PEP (\d+) - (.+)'


# String literals

PEP_URLS_SELECTOR = 'section#numerical-index tr > td:nth-child(3) a'

TITLE_TEXT_SELECTOR = 'h1.page-title::text'

STATUS_SELECTOR = 'dt:contains("Status") + dd > abbr::text'


# Constants

FIELDS_NAME = ('Статус', 'Количество')
