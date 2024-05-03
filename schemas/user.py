from pydantic import BaseModel, validator
from models.user import User
from db_connect import SessionLocal
from functions.univer_function import get_in_db

db = SessionLocal()


class CreateUser(BaseModel):
    name: str
    username: str
    password: str

    @validator('username')
    def username_validate(cls, username):
        validate_my = db.query(User).filter(
            User.username == username,
        ).count()

        if validate_my != 0:
            raise ValueError('Bunday login avval ro`yxatga olingan!')
        return username

    @validator('password')
    def password_validate(cls, password):
        if len(password) < 8:
            raise ValueError('Parol 8 tadan kam bo`lmasligi kerak')
        return password


class UpdateUser(BaseModel):
    ident: int
    name: str
    username: str
    password: str

    @validator('username')
    def username_validate(cls, username):
        validate_my = db.query(User).filter(
            User.username == username,
        ).count()

        the_user = get_in_db(db, User)

        if validate_my != 0 and username != the_user.username:
            raise ValueError('Bunday login avval ro`yxatga olingan!')
        return username

    @validator('password')
    def password_validate(cls, password):
        if len(password) < 8:
            raise ValueError('Parol 8 tadan kam bo`lmasligi kerak')
        return password


