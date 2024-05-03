from sqlalchemy.orm import Session, joinedload
from fastapi import APIRouter, Depends, HTTPException
from db_connect import database
from models.answers import Answers
from typing import List

from routes.login import get_current_active_user
from schemas.answers import CreateAnswer, UpdateAnswer
from functions.answers import create_answer, update_answer, delete_choise_answer
from schemas.user import CreateUser

router_answer = APIRouter(prefix="/Answers", tags=["answer operations"])


@router_answer.post('/create_answer')
def create(forms: List[CreateAnswer],
           db: Session = Depends(database),
           current_user: CreateUser = Depends(get_current_active_user)):
    create_answer(db, forms, current_user)
    raise HTTPException(200, "Success")


@router_answer.get('/get_all_answer')
def get(question: int = 0, db: Session = Depends(database),
        current_user: CreateUser = Depends(get_current_active_user)):
    if question > 0:
        question_filter = Answers.question_id == question
    else:
        question_filter = Answers.id > 0
    return db.query(Answers).filter(question_filter).all()


@router_answer.put('/update_answer')
def update(forms: List[UpdateAnswer],
           db: Session = Depends(database),
           current_user: CreateUser = Depends(get_current_active_user)):
    update_answer(db, forms, current_user)
    raise HTTPException(200, "Success!!!")


@router_answer.delete('/delete_choice_answer')
def delete(idents: List[int],
           db: Session = Depends(database),
           current_user: CreateUser = Depends(get_current_active_user)):
    delete_choise_answer(db, idents, current_user)
    raise HTTPException(200, "Success!!!")
