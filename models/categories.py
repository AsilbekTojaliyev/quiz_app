from sqlalchemy import Column, String, Integer
from db_connect import Base


class Categories(Base):
    __tablename__ = "categories"
    id = Column(Integer, primary_key=True, autoincrement=True)
    category = Column(String(255), nullable=False)
