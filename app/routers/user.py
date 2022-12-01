from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.db.get_db import get_db
from app.schemas.user import CreateUserSchema, UserSchema
from app.services import user as UserService

router = APIRouter()


@router.post("/users/", response_model=UserSchema)
async def create_user(user: CreateUserSchema, db: Session = Depends(get_db)):
    db_user = await UserService.get_user(db, username=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return await UserService.create_user(db=db, user=user)
