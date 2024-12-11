from fastapi import FastAPI
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from starlette.requests import Request
from .routes import incomes, expenses

app = FastAPI()

# Підключення шаблонів
templates = Jinja2Templates(directory="templates")

# Підключення статичних файлів
app.mount("/static", StaticFiles(directory="static"), name="static")

# Підключення роутерів
app.include_router(incomes.router, prefix="/incomes", tags=["incomes"])
app.include_router(expenses.router, prefix="/expenses", tags=["expenses"])

@app.get("/")
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})