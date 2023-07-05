from pydantic import BaseModel


class UserSchema(BaseModel):
    email: str

    class Config:
        orm_mode = True


class CreateUserSchema(UserSchema):
    password: str


class AuthUserSchema(UserSchema):
    password: str


class UserForShareNoteSchema(BaseModel):
    id: int
    email: str

    class Config:
        orm_mode = True
