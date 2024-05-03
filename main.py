from fastapi import FastAPI
from routes.finally_result import router_finally_result
from routes.user import users_router
from routes.login import login_router
from routes.categories import router_category
from routes.questions import router_question
from routes.answers import router_answer
from routes.results import router_result

app = FastAPI(docs_url="/")

app.include_router(login_router)
app.include_router(users_router)
app.include_router(router_category)
app.include_router(router_question)
app.include_router(router_answer)
app.include_router(router_result)
app.include_router(router_finally_result)

