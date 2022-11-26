from pydantic import BaseModel

from typing import Sequence


class NoteBase(BaseModel):
    title: str
    text: str


class NoteCreate(NoteBase):
    title: str
    submitter_id: int


class NoteUpdate(NoteBase):
    id: int


class NoteUpdateRestricted(BaseModel):
    id: int
    title: str


# Properties shared by models stored in DB
class NoteInDBBase(NoteBase):
    id: int
    submitter_id: int

    class Config:
        orm_mode = True


# Properties to return to client
class Note(NoteInDBBase):
    pass


# Properties properties stored in DB
class NoteInDB(NoteInDBBase):
    pass


class NoteSearchResults(BaseModel):
    results: Sequence[Note]