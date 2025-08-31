from fastapi import FastAPI
from sqlalchemy import select
from .database import engine
from .models import messages

app = FastAPI()

@app.get("/")
async def read_message():
    with engine.connect() as conn:
        result = conn.execute(select(messages)).first()
        if result:
            return {"message": result.text}
        return {"message": "Сообщений нет."}
