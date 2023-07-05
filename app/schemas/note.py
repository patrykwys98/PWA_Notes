from typing import List, Optional

from pydantic import BaseModel

from app.schemas.share import ShareNoteGetSchema


class NoteSchema(BaseModel):
    title: str
    content: str
    child_id: Optional[int] = None
    tags: Optional[str] = None

    class Config:
        orm_mode = True


class NoteAllSchema(BaseModel):
    id: int
    title: str
    content: str
    tags: Optional[str] = None
    child_id: Optional[int] = None

    class Config:
        orm_mode = True


class NotesToTreeSchema(BaseModel):
    id: int
    title: str
    child_id: Optional[int] = None

    class Config:
        orm_mode = True


class NoteCreateSchema(BaseModel):
    title: str
    content: Optional[str] = None
    child_id: Optional[int] = None


class NoteRenameSchema(BaseModel):
    title: str


class SharedNoteSchema(BaseModel):
    id: int
    title: str
    child_id: Optional[int] = None
    shared: ShareNoteGetSchema

    class Config:
        orm_mode = True


class NotesAndSharedNotesSchema(BaseModel):
    notes: List[NotesToTreeSchema]
    shared: Optional[List[SharedNoteSchema]] = None

    class Config:
        orm_mode = True
