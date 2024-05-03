from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, HTTPException
from db_connect import database
from models.categories import Categories
from typing import List
from routes.login import get_current_active_user
from schemas.categories import CreateCategory, UpdateCategory
from functions.categories import create_category, update_category, delete_choise_category
from schemas.user import CreateUser

router_category = APIRouter(prefix="/Categories", tags=["category operations"])


@router_category.post('/create_category')
def create(form: CreateCategory,
           db: Session = Depends(database),
           current_user: CreateUser = Depends(get_current_active_user)):
    create_category(db, form, current_user)
    raise HTTPException(200, "Success")


@router_category.get('/get_all_category')
def get(db: Session = Depends(database)):
    return db.query(Categories).all()


@router_category.put('/update_category')
def update(forms: List[UpdateCategory],
           db: Session = Depends(database),
           current_user: CreateUser = Depends(get_current_active_user)):
    update_category(db, forms, current_user)
    raise HTTPException(200, "Success!!!")


@router_category.delete('/delete_choice_category')
def delete(idents: List[int],
           db: Session = Depends(database),
           current_user: CreateUser = Depends(get_current_active_user)):
    delete_choise_category(db, idents, current_user)
    raise HTTPException(200, "Success!!!")
