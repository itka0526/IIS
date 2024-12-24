### Setup

```bash
cd /Users/itgelt/Desktop/itgelt_hw/IIS/5/
python3 -m venv venv --system-site-packages
source venv/bin/activate.fish # Depends on your system
pip install -r requirements.txt
uvicorn app.main:app --reload
```

### Tests

#### 14. Убедитесь что данные создаются и сохраняются в файле БД : library.db

#### 17. Проверьте работоспособность новых маршрутов.

```bash
bash ./test.sh
```
