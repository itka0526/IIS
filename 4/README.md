### Setup

```bash
cd /Users/itgelt/Desktop/itgelt_hw/IIS/4/
python3 -m venv venv --system-site-packages
source venv/bin/activate.fish # Depends on your system
pip install -r requirements.txt
uvicorn app.main:app --reload
```

### 13. Проверьте работоспособность эндпоинтов вызвав каждый из методов аналогично тому как вы делали в предыдущихпрактических работах: Создайте 2 книги, получите список книг, удалите 1 книгу, измените другую книгу, получите книгу пo id

```bash
bash ./test.sh > output.txt && cat ./output.txt
```
