from sqlalchemy import Column, Integer, String, Float, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from income_expense_tracker.db.database import Base


class Income(Base):
    __tablename__ = 'incomes'

    id = Column(Integer, primary_key=True, index=True)
    category = Column(String, index=True, nullable=False)
    amount = Column(Float, nullable=False)
    date = Column(DateTime, default=datetime.utcnow, nullable=False)
    description = Column(String, nullable=True)
    author = Column(String, nullable=True)

    def __repr__(self):
        return f"<Income(category={self.category}, amount={self.amount}, date={self.date})>"


class Expense(Base):
    __tablename__ = 'expenses'

    id = Column(Integer, primary_key=True, index=True)
    category = Column(String, index=True, nullable=False)
    amount = Column(Float, nullable=False)
    date = Column(DateTime, default=datetime.utcnow, nullable=False)
    description = Column(String, nullable=True)
    author = Column(String, nullable=True)


    def __repr__(self):
        return f"<Expense(category={self.category}, amount={self.amount}, date={self.date})>"
