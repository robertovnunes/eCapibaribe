from fastapi import FastAPI 
from fastapi.middleware.cors import CORSMiddleware 
from features.items.items import items_router
from features.users.user import users_router


app = FastAPI()

app.add_middleware(     
    CORSMiddleware,     
    allow_credentials=True,     
    allow_origins=[""],     
    allow_methods=[""],     
    allow_headers=["*"], 
) 

app.include_router(items_router)
app.include_router(users_router)