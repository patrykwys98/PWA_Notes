from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.db.get_db import get_db
from app.schemas.user import CreateUserSchema, UserSchema, UserForShareNoteSchema
from app.services import user as UserService
from app.services.auth import get_current_user
from app.models import User

router = APIRouter()


@router.post("/create-user/", response_model=UserSchema)
async def create_user(user: CreateUserSchema, db: Session = Depends(get_db)):
    db_user = await UserService.get_user(db, username=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return await UserService.create_user(db=db, user=user)


@router.get("/get-users-for-share/", response_model=list[UserForShareNoteSchema],
)
async def get_users_for_share(
    db: Session = Depends(get_db),
 ):
    return await UserService.get_users_for_share(db=db)
