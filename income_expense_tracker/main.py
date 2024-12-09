from fastapi import FastAPI
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from starlette.requests import Request

app = FastAPI()

# Підключення шаблонів
templates = Jinja2Templates(directory="templates")

# Підключення статичних файлів
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/")
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})