from sqlalchemy import Table, Column, Integer, String
from .database import metadata, engine

# Таблица с твоими сообщениями
messages = Table(
    "msg",  # имя таблицы
    metadata,
    Column("id", Integer, primary_key=True),
    Column("text", String),  # колонка с сообщением
)

# Создаём таблицу, если её нет
metadata.create_all(engine)
