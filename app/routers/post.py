from typing import List
from ..schemas import responseSchema,postSchema
from sqlalchemy.orm import Session
from fastapi import Depends,HTTPException,APIRouter,Response
from ..database import get_db
from .. import models

router = APIRouter(tags = ['posts'])

@router.get("/posts",response_model = List[responseSchema]) 
def get_post(db:Session = Depends(get_db)):

    post = db.query(models.PostTable).all()
    return post


@router.post("/posts",status_code = 201,response_model = responseSchema)
def create_posts(payload:postSchema,db:Session = Depends(get_db)):

    new_data = models.PostTable(
        **payload.dict()
    )
    db.add(new_data)
    db.commit()
    db.refresh(new_data)

    return new_data


#going to retrive one post w.r.t id
#if we give some random id which is not included in data list then it will return numm , but status code will be 200 ok , but i want 400 not found code
@router.get("/posts/{id}",response_model = responseSchema)
def retrive_one_post(id:int,db: Session = Depends(get_db)):

    post = db.query(models.PostTable).filter(models.PostTable.id == str(id)).first()

    if not post:
        raise HTTPException(status_code = 404,detail = "Item Not Found")
    
    return post


# letd delete now
@router.delete('/posts/{id}',response_model = responseSchema)
def del_post(id: int,db:Session = Depends(get_db)):

    post = db.query(models.PostTable).filter(models.PostTable.id == str(id))
    if post.first() == None:
        raise HTTPException(status_code = 404,detail = "Item Not Found")
    
    post.delete(synchronize_session = False)
    db.commit()
    return Response(status_code = 204) 


# update posts
@router.put('/posts/{id}',response_model = responseSchema)
def update(id:int,payload:postSchema,db:Session = Depends(get_db)):
    post_query = db.query(models.PostTable).filter(models.PostTable.id == str(id))
    post = post_query.first()
    if post == None:
        raise HTTPException(status_code = 404,detail = "Item Not Found")
    
    post_query.update(payload.dict(),synchronize_session = False)
    db.commit()
    
    return post_query.first()