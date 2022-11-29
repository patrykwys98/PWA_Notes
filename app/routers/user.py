from fastapi import Depends, APIRouter, HTTPException
from sqlalchemy.orm import Session

from app.schemas.user import UserSchema, CreateUserSchema
from app.services.user import UserService
from app.db.get_db import get_db


router = APIRouter()


@router.post("/users/", response_model=UserSchema)
def create_user(user: CreateUserSchema, db: Session = Depends(get_db)):
    db_user = UserService.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return UserService.create_user(db=db, user=user)
