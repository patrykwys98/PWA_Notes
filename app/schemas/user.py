from pydantic import BaseModel

from app.schemas.notebook import NotebookSchema


class UserSchema(BaseModel):
    """
    User Base Schema
    """
    email: str
    # notebooks: list[NotebookSchema] = []

    class Config:
        orm_mode = True


class CreateUserSchema(UserSchema):
    """
    Create User Schema
    """
    password: str


class AuthUserSchema(UserSchema):
    """
    Auth user schema (with password)
    """
    password: str
