from fastapi import HTTPException


def new_item_db(db, a):
    db.add(a)
    db.commit()
    db.refresh(a)


def get_in_db(db, model, ident):
    text = db.query(model).filter(model.id == ident).first()
    if text is None:
        raise HTTPException(400, f"No information found from {model}!")
    return text
