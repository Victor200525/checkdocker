from fastapi import FastAPI, Form, Request, Depends
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
from .database import Base, engine, SessionLocal
from .models import Request as RequestModel

# Создаём таблицы, если нет
Base.metadata.create_all(bind=engine)

app = FastAPI()
templates = Jinja2Templates(directory="app/templates")

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/", response_class=HTMLResponse)
def read_form(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/add", response_class=HTMLResponse)
def add_request(request: Request, text: str = Form(...), db: Session = Depends(get_db)):
    new_req = RequestModel(text=text)
    db.add(new_req)
    db.commit()
    return templates.TemplateResponse("index.html", {"request": request, "message": "Сохранено!"})

@app.get("/history", response_class=HTMLResponse)
def get_history(request: Request, db: Session = Depends(get_db)):
    items = db.query(RequestModel).all()
    return templates.TemplateResponse("history.html", {"request": request, "items": items})
