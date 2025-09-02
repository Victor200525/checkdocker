from sqlalchemy import Column, Integer, String
from .database import Base

class Request(Base):
    __tablename__ = "requests"

    id = Column(Integer, primary_key=True, index=True)
    text = Column(String, nullable=False)
