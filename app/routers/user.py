from ..schemas import resUser,UserSchema
from sqlalchemy.orm import Session
from fastapi import Depends,HTTPException,APIRouter
from ..database import get_db
from .. import models
from ..utils import hash

router = APIRouter(tags = ['user'])

@router.post('/users',status_code = 201,response_model = resUser)
def create_user(jsonPayload:UserSchema, db : Session = Depends(get_db)):

    #hashing the password
    jsonPayload.password = hash(jsonPayload.password)
    json_inserted = models.UserTable(email = jsonPayload.email,password = jsonPayload.password) #models.User(email=user.email, hashed_password=fake_hashed_password) format
    db.add(json_inserted)
    db.commit()
    db.refresh(json_inserted)
    return json_inserted

@router.get('/users/{id}',response_model = resUser)
def get_user(id:int,db:Session = Depends(get_db)):
    user = db.query(models.UserTable).filter(models.UserTable.id == id).first()

    if not user:
        raise HTTPException(status_code = 404,detail = f'user with {id} not there')
    #resUser.message = "status_susscessful"
    return user
