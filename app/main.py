'''
    NOTE: we can define schema by using pydantic api
'''

from fastapi import FastAPI
from fastapi import Response,status,HTTPException
from pydantic import BaseModel #BaseModel helps us define the schema
from typing import Optional
from random import randrange
app = FastAPI()

class postSchema(BaseModel):
    title: str
    content: str
    published: bool = False #this is optional schema
    rating: Optional[int] = None

data = [{"title":"the title is non","content":"tour","id":1},{"title":"the title is beverly hils","content":"houses","id":2}]

def get_one_post(id):
    for i in data:
        if i['id'] == id:
            return i
        
def postIndex(id):
    for num,i in enumerate(data):
        if i['id'] == id:
            return num

@app.get("/")
def root():
    return {"message":"hello word"}

@app.get("/posts")
def get_post():
    return {"data":data}

@app.post("/posts",status_code = 201)
def create_posts(payload:postSchema):
    #converting pydantic model to dictionary
    payloadDict = payload.dict() #this converts the pydantic model to dict
    payloadDict['id'] = randrange(1,1000000)
    data.append(payloadDict)
    return payloadDict 

#going to retrive one post w.r.t id
#if we give some random id which is not included in data list then it will return numm , but status code will be 200 ok , but i want 400 not found code
@app.get('/posts/{id}')
def retrive_one_post(id: int, res: Response):
    post = get_one_post(id)
    if post is None:
        raise HTTPException(status_code = 404,detail = "Item Not Found")
        #res.status_code = status.HTTP_404_NOT_FOUND
    return {"data":post}

# letd delete now
@app.delete('/posts/{id}')
def del_post(id: int):
    index = postIndex(id)
    if index == None:
        raise HTTPException(status_code = 404,detail = "Item Not Found")
    data.pop(index)
    return Response(status_code = 204) 

# update posts
@app.put('/posts/{id}')
def update(id:int,payload:postSchema):
    index = postIndex(id)
    if index == None:
        raise HTTPException(status_code = 404,detail = "Item Not Found")
    
    post_dict = payload.dict()
    post_dict['id'] = id
    data[index] = post_dict
    return {"updated data":data}