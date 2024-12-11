from sqlalchemy.orm import Session
from .db import models, schemas
from sqlalchemy import func


def create_income(db: Session, income: schemas.IncomeCreate):
    db_income = models.Income(**income.dict())
    db.add(db_income)
    db.commit()
    db.refresh(db_income)
    return db_income


def get_incomes(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Income).offset(skip).limit(limit).all()


def get_total_incomes(db: Session):
    return db.query(func.sum(models.Income.amount)).scalar() or 0


def get_net_income(db: Session):
    # Отримуємо суму доходів
    total_incomes = db.query(func.sum(models.Income.amount)).scalar() or 0
    # Отримуємо суму витрат
    total_expenses = db.query(func.sum(models.Expense.amount)).scalar() or 0
    # Чистий дохід = доходи - витрати
    net_income = total_incomes - total_expenses
    return net_income


def create_expense(db: Session, expense: schemas.ExpenseCreate):
    db_expense = models.Expense(**expense.dict())
    db.add(db_expense)
    db.commit()
    db.refresh(db_expense)
    return db_expense


def get_expenses(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Expense).offset(skip).limit(limit).all()


def get_total_expenses(db: Session):
    return db.query(func.sum(models.Expense.amount)).scalar() or 0


