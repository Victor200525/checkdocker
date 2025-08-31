from sqlalchemy import create_engine, MetaData

# Путь к базе внутри проекта/контейнера
DATABASE_URL = "sqlite:///./check.db"

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
metadata = MetaData()
