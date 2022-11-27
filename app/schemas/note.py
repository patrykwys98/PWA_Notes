from pydantic import BaseModel


class Note(BaseModel):
    title: str
    content: str
    notebook_id: int

    class Config:
        orm_mode = True



