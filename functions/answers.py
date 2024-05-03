from fastapi import HTTPException
from functions.univer_function import new_item_db, get_in_db
from models.answers import Answers


def create_answer(db, forms, user):
    if user.role == "admin":
        for form in forms:
            new_add = Answers(
                answer=form.answer,
                status=form.status,
                question_id=form.question_id
            )
            new_item_db(db, new_add)
    else:
        raise HTTPException(400, "You can't !!!")


def update_answer(db, forms, user):
    if user.role == "admin":
        for form in forms:
            get_in_db(db, Answers, form.ident)
            db.query(Answers).filter(Answers.id == form.ident).update({
                Answers.answer: form.answer,
                Answers.status: form.status,
                Answers.question_id: form.question_id
            })
            db.commit()
    else:
        raise HTTPException(400, "You cannot upgrade !!!")


def delete_choise_answer(db, idents, user):
    if user.role == "admin":
        for ident in idents:
            get_in_db(db, Answers, ident)
            db.query(Answers).filter(Answers.id == ident).delete()
        db.commit()
    else:
        raise HTTPException(400, "You can't !!!")
