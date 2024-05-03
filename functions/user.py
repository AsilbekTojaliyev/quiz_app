from routes.login import get_password_hash
from functions.univer_function import new_item_db
from models.user import User
from fastapi import HTTPException


def get_users(db, user):
    if user.role == "admin":
        items = db.query(User).all()
        return items
    else:
        raise HTTPException(400, "You can't!!!")


def create_user_f(form, db):
    new_add = User(
        name=form.name,
        username=form.username,
        role="user",
        password=get_password_hash(form.password))
    new_item_db(db, new_add)


def update_user_f(form, db, user):
    if user.role == "user":
        db.query(User).filter(User.id == user.id).update({
            User.name: form.name,
            User.username: form.username,
            User.password: get_password_hash(form.password),
            User.role: "user"
        })

        db.commit()

    elif user.role == "admin":
        db.query(User).filter(User.id == user.id).update({
            User.name: form.name,
            User.username: form.username,
            User.password: get_password_hash(form.password),
            User.role: "admin"
        })
        db.commit()


def delete_user_f(db, user):
    db.query(User).filter(User.id == user.id).delete()
    db.commit()


def get_admin(ident, db):

    if ident > 0:
        ident_filter = User.id == ident
    else:
        ident_filter = User.id > 0

    items = db.query(User).filter(ident_filter).order_by(User.id.desc()).all()
    return items


def create_admin_f(form, db, user):
    if user.role == "admin":
        new_add = User(
            name=form.name,
            username=form.username,
            role="admin",
            password=get_password_hash(form.password))
        new_item_db(db, new_add)
    else:
        raise HTTPException(400, "You can't !!!")





