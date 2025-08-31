from sqlalchemy import insert
from app.database import engine
from app.models import messages

with engine.connect() as conn:
    conn.execute(insert(messages).values(text="Привет! Это твоё сообщение."))
    conn.commit()

print("База создана и сообщение добавлено.")
