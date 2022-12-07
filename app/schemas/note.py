from pydantic import BaseModel
from typing import Any


class NoteSchema(BaseModel):
    """
    Base Note Schema
    """
    title: str
    content: str
    notebook_id: int
    path: Any = None

    class Config:
        orm_mode = True
