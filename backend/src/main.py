from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from features.users.user import users_router

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_credentials=True,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(users_router)
