from fastapi import FastAPI
from app.routes import router

app = FastAPI(title="Library API", description="API для управления библиотекой", version="1.0.0")

# Подключение роутера
app.include_router(router)
