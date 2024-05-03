from sqlalchemy.orm import Session, joinedload
from fastapi import APIRouter, Depends, HTTPException
from db_connect import database
from models.questions import Questions
from typing import List
from routes.login import get_current_active_user
from schemas.questions import CreateQuestion, UpdateQuestion
from functions.questions import create_question, update_question, delete_choise_question
from schemas.user import CreateUser

router_question = APIRouter(prefix="/Questions", tags=["question operations"])


@router_question.post('/create_question')
def create(forms: List[CreateQuestion],
           db: Session = Depends(database),
           current_user: CreateUser = Depends(get_current_active_user)):
    create_question(db, forms, current_user)
    raise HTTPException(200, "Success")


@router_question.get('/get_all_question')
def get(category: int = 0, db: Session = Depends(database),
        current_user: CreateUser = Depends(get_current_active_user)):
    return db.query(Questions).all()
    # if category > 0:
    #     category_filter = Questions.category_id == category
    # else:
    #     category_filter = Questions.id > 0
    # return db.query(Questions).options(joinedload(Questions.category)).filter(category_filter).all()


@router_question.put('/update_question')
def update(forms: List[UpdateQuestion],
           db: Session = Depends(database),
           current_user: CreateUser = Depends(get_current_active_user)):
    update_question(db, forms, current_user)
    raise HTTPException(200, "Success!!!")


@router_question.delete('/delete_question')
def delete(idents: List[int],
           db: Session = Depends(database),
           current_user: CreateUser = Depends(get_current_active_user)):
    delete_choise_question(db, idents, current_user)
    raise HTTPException(200, "Success!!!")
