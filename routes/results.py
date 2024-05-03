from typing import List
from sqlalchemy.orm import Session, joinedload
from db_connect import database
from fastapi import APIRouter, Depends
from functions.results import create_result
from models.results import Results
from routes.login import get_current_active_user
from schemas.results import CreateResult
from schemas.user import CreateUser

router_result = APIRouter(prefix="/Results", tags=["result operations"])


@router_result.get('/get_result')
def get(category: int = 0, question: int = 0, answer: int = 0, db: Session = Depends(database),
        current_user: CreateUser = Depends(get_current_active_user)):
    user = current_user.id
    if question > 0:
        question_filter = Results.question_id == question
    else:
        question_filter = Results.id > 0

    if answer > 0:
        answer_filter = Results.answer_id == answer
    else:
        answer_filter = Results.id > 0

    if category > 0:
        category_filter = Results.category_id == category
    else:
        category_filter = Results.id > 0

    if user > 0:
        user_filter = Results.user_id == user
    else:
        user_filter = Results.id > 0

    return db.query(Results).options(
        joinedload(Results.question), joinedload(Results.answer),
        joinedload(Results.category), joinedload(Results.user)).filter(
        question_filter, answer_filter, category_filter, user_filter).all()


@router_result.post('/create_result')
def create(forms: List[CreateResult], db: Session = Depends(database),
           current_user: CreateUser = Depends(get_current_active_user)):
    return create_result(db, forms, current_user)
