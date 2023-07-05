from pydantic import BaseModel
from typing import List, Optional

class ShareNoteBaseSchema(BaseModel):
    note_id: Optional[int] = None
    can_edit: Optional[bool] = False
    can_delete: Optional[bool] = False
    can_share: Optional[bool] = False
    can_view: Optional[bool] = False

    class Config:
        orm_mode = True


class ShareNoteCreateSchema(ShareNoteBaseSchema):
    user_id: Optional[List[int]] = None


class ShareNoteGetSchema(ShareNoteBaseSchema):
    user_id: Optional[int] = None


class ShareNoteUpdateSchema(ShareNoteGetSchema):
    pass


class UnshareNoteSchema(BaseModel):
    note_id: int
    user_id: int

    class Config:
        orm_mode = True
