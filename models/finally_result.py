from sqlalchemy import Column, Integer, Numeric
from sqlalchemy.orm import relationship
from db_connect import Base
from models.categories import Categories
from models.user import User


class Finally_result(Base):
    __tablename__ = "finally_result"
    id = Column(Integer, primary_key=True, autoincrement=True)
    category_id = Column(Integer, nullable=False)
    common = Column(Integer, nullable=False)
    found = Column(Integer, nullable=False)
    percent = Column(Numeric(255))
    user_id = Column(Integer, nullable=False)
    user = relationship(argument="User", foreign_keys=[user_id],
                        primaryjoin=lambda: Finally_result.user_id == User.id)
    category = relationship(argument="Categories", foreign_keys=[category_id],
                            primaryjoin=lambda: Finally_result.category_id == Categories.id)
