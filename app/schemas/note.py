from typing import Any

from pydantic import BaseModel


class NoteSchema(BaseModel):
    """
    Base Note Schema
    """
    title: str
    content: str
    # childrens: Any = None
    child_id: int = None

    class Config:
        orm_mode = True


class NoteAllSchema(BaseModel):
    """
    Base Note Schema
    """
    id: int
    title: str
    content: str
    notebook_id: int
    child_id: int = None

    class Config:
        orm_mode = True


class NotesToTreeSchema(BaseModel):
    """
    Base Note Schema
    """
    id: int
    title: str
    # children: bool = False
    child_id: int = None

    class Config:
        orm_mode = True


class NoteCreateSchema(BaseModel):
    title: str
    content: str = None
    child_id: int = None


class NoteRenameSchema(BaseModel):
    title: str