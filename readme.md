# Тестовое задание Тензор

## Сторонние библиотеки
1. psycopg2

## Инструкция по запуску 
1. В файле database.ini указываем данные для подключения к базе данных PostgreSQL
2. Создаем таблцы и заполняем их данными из файла .json с помощью Python скрипта
```bash
python db_create.py
```
или
```bash
JSON="data.json" python db_create.py
```
3. Выполняем запрос на получение коллег по офису с помощью Python скрипта
```bash
python db_query.py
```