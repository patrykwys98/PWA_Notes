from pydantic import BaseModel


class ShareNoteBaseSchema(BaseModel):
    note_id: int | None = None
    can_edit: bool | None = False
    can_delete: bool | None = False
    can_share: bool | None = False
    can_view: bool | None = False

    class Config:
        orm_mode = True


class ShareNoteCreateSchema(ShareNoteBaseSchema):
    """
    Share Create Schema
    """
    user_id: list[int] | None = None

class ShareNoteGetSchema(ShareNoteBaseSchema):
    """
    Share Get Schema
    """
    user_id: int | None = None

    class Config:
        orm_mode = True

class ShareNoteUpdateSchema(ShareNoteGetSchema):
    """
    Share Update Schema
    """
    pass

class UnshareNoteSchema(BaseModel):
    """
    Unshare Schema
    """
    note_id: int
    user_id: int

    class Config:
        orm_mode = True