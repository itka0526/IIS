#!/bin/bash

rm o*.json

# 14. Убедитесь что данные создаются и сохраняются в файле БД : library.db
curl -X 'POST' \
  'http://127.0.0.1:8000/book/' \
  -H 'Content-Type: application/json' \
  -d '{
    "id": 0,
    "title": "Война и мир",
    "author": "Лев Толстой",
    "year": 1869
  }' > o1_books.json

curl -X 'POST' \
  'http://127.0.0.1:8000/reader/' \
  -H 'Content-Type: application/json' \
  -d '{
    "name": "reader test1"
  }' > o2_readers.json

curl -X 'POST' \
  'http://127.0.0.1:8000/issue/' \
  -H 'Content-Type: application/json' \
  -d '{
    "book_id": 4,
    "reader_id": 1
  }' > o3_issues.json

# 17. Проверьте работоспособность новых маршрутов.

curl -X 'GET' \
  'http://127.0.0.1:8000/book/'  > o4_get_books.json

curl -X 'GET' \
  'http://127.0.0.1:8000/reader/'  > o5_get_readers.json

curl -X 'GET' \
  'http://127.0.0.1:8000/issue/'  > o6_get_issues.json

