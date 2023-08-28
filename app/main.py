'''
    NOTE: we can define schema by using pydantic api
'''

from fastapi import FastAPI
from fastapi import Response,status,HTTPException,Depends
from pydantic import BaseModel #BaseModel helps us define the schema
from typing import List
#from passlib.context import CryptContext
from . import models
from .schemas import postSchema,responseSchema,UserSchema,resUser
from .utils import hash
from sqlalchemy.orm import Session
from .database import engine,get_db
from .routers import post,user,auth

models.Base.metadata.create_all(bind=engine) #creates database
#pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
app = FastAPI()
app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)

@app.get("/")
def root():
    return {"message":"hello word"}