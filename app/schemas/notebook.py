from pydantic import BaseModel

from app.schemas.note import NoteSchema


class NotebookSchema(BaseModel):
    """
    Base Notebook Schema
    """
    title: str
    owner_id: int
    notes: list[NoteSchema] = []

    class Config:
        orm_mode = True


class NotebooksSchema(BaseModel):
    """
    Notebooks schema
    """
    # FIXME
    notebooks: list[NotebookSchema] = []

    class Config:
        orm_mode = True
