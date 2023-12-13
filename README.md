# Проект парсинга pep
Асинхронный парсер документации PEP с сайта https://peps.python.org/. \
Используется фреймворк Scrapy.

## Установка и настройка
- Клонируйте репозиторий: `git clone git@github.com:dentretyakoff/scrapy_parser_pep.git`
- Перейдите в директорию проекта: `cd ваш-репозиторий`
- Создайте и активируйте виртуальное окружение: `python3 -m venv venv && source venv/bin/activate`
- Установите зависимости: `pip install -r requirements.txt`

## Использование
Из дериктории с проектом выполните команду:
```
scrapy crawl pep
```
Парсер сохранит данные в файлы `*.csv` в директорию `results/`.
- `pep_ДатаВремя.csv` - файл со списком PEP, содержит столбцы «Номер», «Название» и «Статус».
- `status_summary_ДатаВремя.csv` - файл со сводкой по статусам, содержит столбцы «Статус» и «Количество».
Лог работы сохранятеся в каталоге `logs/`.

### Авторы
[Денис Третьяков](https://github.com/dentretyakoff)
### Лицензия
[MIT License](https://opensource.org/licenses/MIT)