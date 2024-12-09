import os

from pydantic_settings import BaseSettings
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv

# Завантажуємо .env файл
load_dotenv()


class Settings(BaseSettings):
    DATABASE_URL: str = os.getenv("DATABASE_URL")

    class Config:
        env_file = ".env"


settings = Settings()

# Створення інтерфейсу для взаємодії з базою даних
engine = create_engine(settings.DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


# Функція для отримання сесії
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
