#!/bin/bash

# Book 1
curl -X 'POST' \
  'http://127.0.0.1:8000/book' \
  -H 'Content-Type: application/json' \
  -d '{
    "id": 0,
    "title": "Война и мир",
    "author": "Лев Толстой",
    "year": 1869
  }'

# Book 2
curl -X 'POST' \
  'http://127.0.0.1:8000/book' \
  -H 'Content-Type: application/json' \
  -d '{
    "id": 0,
    "title": "test2",
    "author": "test_author2",
    "year": 1999
  }'

# Get all books
curl -X 'GET' \
  'http://127.0.0.1:8000/book/all'

# Delete 1 book
curl -X 'DELETE' \
  'http://127.0.0.1:8000/book/1'

# Get book by ID
curl -X 'GET' \
  'http://127.0.0.1:8000/book/2'
