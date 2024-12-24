### Setup

```bash
cd /Users/itgelt/Desktop/itgelt_hw/IIS/7/
python3 -m venv venv --system-site-packages
source venv/bin/activate.fish # Depends on your system
pip install -r requirements.txt
uvicorn app.main:app --reload
```

### Tests

```bash
python3 -m pytest
```

### Run interface

```bash
streamlit run /Users/itgelt/Desktop/itgelt_hw/IIS/7/front/ui.py
```
