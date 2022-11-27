from pydantic import BaseModel


class Notebook(BaseModel):
    title: str

    class Config:
        orm_mode = True