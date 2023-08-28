from pydantic import BaseModel,EmailStr
from datetime import datetime
class postSchema(BaseModel):
    title: str
    content: str
    published: bool = False #this is optional schema


class responseSchema(BaseModel):
    title: str
    content: str
    created_at: datetime

    class Config:
        from_attributes = True


class UserSchema(BaseModel):
    email: EmailStr
    password: str

class resUser(BaseModel):
    email: EmailStr
    created_at: datetime

    class Config:
        from_attributes = True

class loginSchema(BaseModel):
    email: EmailStr
    password: str

# class Token(BaseModel):
#     access_token: str
#     token_type: str

#     class


