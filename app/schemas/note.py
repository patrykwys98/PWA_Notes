from pydantic import BaseModel


class NoteSchema(BaseModel):
    """
    Base Note Schema
    """
    title: str
    content: str
    notebook_id: int

    class Config:
        orm_mode = True
