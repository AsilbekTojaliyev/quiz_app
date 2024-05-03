from fastapi import HTTPException
from models.categories import Categories
from functions.univer_function import new_item_db, get_in_db


def create_category(db, form, user):
    if user.role == "admin":
        new = Categories(category=form.category)
        new_item_db(db, new)
    else:
        raise HTTPException(400, "You can't!")


def update_category(db, forms, user):
    if user.role == "admin":
        for form in forms:
            get_in_db(db, Categories, form.ident)
            db.query(Categories).filter(Categories.id == form.ident).update({
                Categories.category: form.category
            })
            db.commit()
    else:
        raise HTTPException(400, "You can't!")


def delete_choise_category(db, idents, user):
    if user.role == "admin":
        for ident in idents:
            get_in_db(db, Categories, ident)
            db.query(Categories).filter(Categories.id == ident).delete()
        db.commit()
    else:
        raise HTTPException(400, "You can't!")
