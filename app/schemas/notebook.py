from pydantic import BaseModel

from app.schemas.note import NoteSchema


class BaseNotebookSchema(BaseModel):
    """
    Base Note Schema
    """
    title: str

    class Config:
        orm_mode = True


class NotebookSchema(BaseNotebookSchema):
    """
    Base Notebook Schema
    """
    owner_id: int
    notes: list[NoteSchema] = []


class AddNotebookSchema(BaseNotebookSchema):
    """
    Add Notebook Schema
    """


class GetNotebooksListSchema(BaseNotebookSchema):
    """
    Get Notebooks List Schema
    """
    id: int

# FIXME


class NotebooksSchema(BaseModel):
    """
    Notebooks schema
    """

    notebooks: list[NotebookSchema] = []

    class Config:
        orm_mode = True
