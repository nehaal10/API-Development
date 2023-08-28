from fastapi import APIRouter,Depends,status,HTTPException,responses
from ..database import get_db
from sqlalchemy.orm import Session
from ..schemas import loginSchema
from .. import models
from ..utils import verify
from ..auth2 import jwtToken

router = APIRouter(tags=["AUTH"])

@router.post('/login')
def login(jsonPayload:loginSchema,db: Session = Depends(get_db)):
    user = db.query(models.UserTable).filter(models.UserTable.email == jsonPayload.email).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f'Invalid credentials')
    
    if not verify(jsonPayload.password,user.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f'Invalid credentials')
    
    token = jwtToken({"user_id":user.id})
    return {"user_token":token,"token_type":"bearer"}
    
    

