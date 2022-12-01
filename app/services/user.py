from sqlalchemy.orm import Session

import app.services.auth as auth
from app.models.user import User
from app.schemas.user import CreateUserSchema


async def get_user(db: Session, username: str):
    return db.query(User).filter(User.email == username).first()


async def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(User).offset(skip).limit(limit).all()


async def create_user(db: Session, user: CreateUserSchema):
    db_user = User(username=user.email, email=user.email,
                   password=auth.get_password_hash(user.password))
    print("create user", auth.get_password_hash(user.password))
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
