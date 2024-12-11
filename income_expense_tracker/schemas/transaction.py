from pydantic import BaseModel
from datetime import datetime
from typing import Optional


# Базова схема для доходів
class IncomeBase(BaseModel):
    category: str
    amount: float


# Схема для створення доходів
class IncomeCreate(IncomeBase):
    date: datetime  # Очікуємо дату при створенні запису
    description: Optional[str] = None  # Необов'язковий опис доходу


# Схема для отримання доходів
class Income(IncomeBase):
    id: int
    date: datetime
    description: Optional[str] = None
    author: str  # Автор запису, буде заповнюватись із JWT

    class Config:
        orm_mode = True


# Базова схема для витрат
class ExpenseBase(BaseModel):
    category: str
    amount: float


# Схема для створення витрат
class ExpenseCreate(ExpenseBase):
    date: datetime  # Очікуємо дату при створенні запису
    description: Optional[str] = None  # Необов'язковий опис витрати


# Схема для отримання витрат
class Expense(ExpenseBase):
    id: int
    date: datetime
    description: Optional[str] = None
    author: str  # Автор запису, буде заповнюватись із JWT

    class Config:
        orm_mode = True
