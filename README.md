# Scrapy Parser Pep

Асинхронный парсинг документов PEP

[![Python](https://img.shields.io/badge/-Python-464646?style=flat&logo=Python&logoColor=ffffff&color=informational)](https://www.python.org/)
[![Scrapy](https://img.shields.io/badge/-Scrapy-464646?style=flat&logo=Scrapy&logoColor=ffffff&color=informational)](https://docs.scrapy.org/en/latest/topics/architecture.html)

Проект "Асинхронный парсинг документов PEP" предназначен для удобства доступа к документации, теперь информация будет всегда под рукой.
Не безызвестно, что развитие языка Python сопровождается документами PEP — Python Enhancement Proposal.

Результат работы программы сохраняется в двух файлах.
- `pep_DateTime` собирает список всех PEP c номером, названием и статусом, сохраняя в csv файл.
- `status_summary_DateTime` просчитывает количество PEP в каждом статусе и их общее количество, так же сохраняет в csv файл.


## Запуск проекта

1. Клонируйте репозиторий и перейдите в него
    ```bash
   https://github.com/whodef/bs4_parser_pep.git
   ```
2. Установите и активируйте виртуальное окружение
    ```bash
   python3 -m venv venv
   ```
3. Установите зависимости из файла requirements.txt
    ```bash
    python3 -m pip install --upgrade pip
    ```
    ```bash
    pip3 install -r requirements.txt
    ```
4. Через командную строку в директории src запустите скрипт:
    ```bash
    scrapy crawl pep
    ```


## Автор проекта

**[Tatiana Seliuk](https://github.com/whodef)**