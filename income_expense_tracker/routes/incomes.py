from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from .. import crud, schemas, db

router = APIRouter()


@router.post("/", response_model=schemas.Income)
def create_income(income: schemas.IncomeCreate, database: Session = Depends(db.get_db)):
    """
    Створює новий запис доходів.
    """
    return crud.create_income(db=database, income=income)


@router.get("/", response_model=list[schemas.Income])
def read_incomes(skip: int = 0, limit: int = 10, database: Session = Depends(db.get_db)):
    """
    Отримує список розходів з можливістю пагінації.
    """
    return crud.get_incomes(db=database, skip=skip, limit=limit)


@router.get("/total", response_model=float)
def read_total_incomes(database: Session = Depends(db.get_db)):
    """
    Отримує загальну суму доходів.
    """
    return crud.get_total_incomes(db=database)


@router.get("/net", response_model=float)
def read_net_income(database: Session = Depends(db.get_db)):
    """
    Отримує чистий дохід (доходи мінус витрати).
    """
    return crud.get_net_income(db=database)


