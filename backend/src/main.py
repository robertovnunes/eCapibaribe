from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from backend.src.features.users.user import users_router
from backend.src.features.users.create_user import cadastro

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_credentials=True,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(users_router)
app.include_router(cadastro)
