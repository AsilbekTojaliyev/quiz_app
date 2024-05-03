from sqlalchemy import Column, Integer
from sqlalchemy.orm import relationship
from db_connect import Base
from models.questions import Questions
from models.answers import Answers
from models.categories import Categories
from models.user import User


class Results(Base):
    __tablename__ = "results"
    id = Column(Integer, primary_key=True, autoincrement=True)
    category_id = Column(Integer, nullable=False)
    question_id = Column(Integer, nullable=False)
    answer_id = Column(Integer, nullable=False)
    user_id = Column(Integer, nullable=False)

    question = relationship(argument="Questions", foreign_keys=[question_id],
                         primaryjoin=lambda: Questions.id == Results.question_id)
    answer = relationship(argument="Answers", foreign_keys=[answer_id],
                         primaryjoin=lambda: Answers.id == Results.answer_id)
    category = relationship(argument="Categories", foreign_keys=[category_id],
                       primaryjoin=lambda: Categories.id == Results.category_id)
    user = relationship(argument="User", foreign_keys=[user_id],
                        primaryjoin=lambda: User.id == Results.user_id)
