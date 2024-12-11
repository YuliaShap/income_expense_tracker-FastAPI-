from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from .. import crud, schemas, db

router = APIRouter()

@router.post("/", response_model=schemas.Expense)
def create_expense(expense: schemas.ExpenseCreate, db: Session = Depends(db.get_db)):
    """
    Створює новий запис витрат.
    """
    return crud.create_expense(db=db, expense=expense)

@router.get("/", response_model=list[schemas.Expense])
def read_expenses(skip: int = 0, limit: int = 10, db: Session = Depends(db.get_db)):
    """
    Отримує список витрат з можливістю пагінації.
    """
    return crud.get_expenses(db=db, skip=skip, limit=limit)


@router.get("/total", response_model=float)
def read_total_expenses(db: Session = Depends(db.get_db)):
    """
    Отримує загальну суму витрат.
    """
    return crud.get_total_expenses(db=db)
