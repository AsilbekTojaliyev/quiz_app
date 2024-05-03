from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session, joinedload
from db_connect import database
from functions.univer_function import get_in_db
from models.answers import Answers
from models.finally_result import Finally_result
from models.results import Results
from routes.login import get_current_active_user
from schemas.user import CreateUser

router_finally_result = APIRouter(prefix="/Finally_Result", tags=["finally_result operations"])


@router_finally_result.get("/get_finally_result")
def get_all(db: Session = Depends(database),
            current_user: CreateUser = Depends(get_current_active_user)):
    forms = db.query(Results).filter(Results.user_id == current_user.id).all()
    total = 0
    currect = 0
    for form in forms:
        total += 1
        answer = get_in_db(db, Answers, form.answer_id)
        if answer.status:
            currect += 1
    if total == 0:
        raise HTTPException(400, "siz hali test yechmadingiz !!!")
    percent = (currect * 100) / total
    return f"All Answers: {total}, Trues: {currect}, Percentage: {percent}%"


@router_finally_result.get("/get_create_result")
def get_first(db: Session = Depends(database),
              current_user: CreateUser = Depends(get_current_active_user)):
    return db.query(Finally_result).filter(Finally_result.user_id == current_user.id).all()

