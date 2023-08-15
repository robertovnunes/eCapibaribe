from fastapi import FastAPI
from features.users.user import users_router

app = FastAPI()
app.include_router(users_router)
