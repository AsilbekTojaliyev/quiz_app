from models.answers import Answers
from models.categories import Categories
from models.finally_result import Finally_result
from models.questions import Questions
from models.results import Results
from functions.univer_function import new_item_db, get_in_db
from fastapi import HTTPException


def create_result(db, forms, user):
    total = 0
    currect = 0
    for form in forms:
        get_in_db(db, Categories, form.category_id)
        question = get_in_db(db, Questions, form.question_id)
        answer = get_in_db(db, Answers, form.answer_id)

        if answer.question_id != question.id:
            raise HTTPException(400, "variyant idga savol id ma'lumoti to'g'ri kelmadi!")
        new_add = Results(
            category_id=form.category_id,
            question_id=form.question_id,
            answer_id=form.answer_id,
            user_id=user.id
        )
        new_item_db(db, new_add)
        total += 1
        if answer.status:
            currect += 1
    percent = (currect * 100) // total

    new_result = Finally_result(
        category_id=form.category_id,
        common=total,
        found=currect,
        percent=percent,
        user_id=user.id
    )
    new_item_db(db, new_result)

    return f"All Answers: {total}, Trues: {currect}, Percentage: {percent}%"

