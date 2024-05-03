from fastapi import HTTPException
from functions.univer_function import new_item_db, get_in_db
from models.questions import Questions


def create_question(db, forms, user):
    if user.role == "admin":
        for form in forms:
            new_add = Questions(
                question=form.question,
                category_id=form.category_id
            )
            new_item_db(db, new_add)
    else:
        raise HTTPException(400, "You can't!")


def update_question(db, forms, user):
    if user.role == "admin":
        for form in forms:
            get_in_db(db, Questions, form.ident)
            db.query(Questions).filter(Questions.id == form.ident).update({
                Questions.question: form.question,
                Questions.category_id: form.category_id
            })
            db.commit()
    else:
        raise HTTPException(400, "You can't!")


def delete_choise_question(db, idents, user):
    if user.role == "admin":
        for ident in idents:
            get_in_db(db, Questions, ident)
            db.query(Questions).filter(Questions.id == ident).delete()
        db.commit()
    else:
        raise HTTPException(400, "You can't!")
