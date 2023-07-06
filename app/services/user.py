from sqlalchemy.orm import Session

import app.services.auth as auth
from app.models.user import User
from app.schemas.user import CreateUserSchema, UserSchema


async def get_user(db: Session, username: str) -> User:
    return db.query(User).filter(User.email == username).first()


async def get_users(db: Session, skip: int = 0, limit: int = 100) -> list[User]:
    return db.query(User).offset(skip).limit(limit).all()


async def create_user(db: Session, user: CreateUserSchema) -> User:
    db_user = User(
        username=user.email,
        email=user.email,
        password=auth.get_password_hash(user.password)
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


async def delete_user(db: Session, user_id: int) -> User:
    user = db.query(User).filter(User.id == user_id).first()
    db.delete(user)
    db.commit()
    return user


async def update_user(db: Session, user_id: int, user: CreateUserSchema) -> User:
    db_user = db.query(User).filter(User.id == user_id).first()
    db_user.username = user.email
    db_user.email = user.email
    db_user.password = auth.get_password_hash(user.password)
    db.commit()
    db.refresh(db_user)
    return db_user


async def get_user_by_id(db: Session, user_id: int) -> User:
    return db.query(User).filter(User.id == user_id).first()


async def get_users_for_share(
    db: Session,
    user: UserSchema,
    skip: int = 0,
    limit: int = 100
) -> list[User]:
    users = db.query(User).offset(skip).limit(limit).all()
    return [u for u in users if u.id != user.id]
