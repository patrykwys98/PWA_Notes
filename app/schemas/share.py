from pydantic import BaseModel

class ShareNoteBaseSchema(BaseModel):
    note_id: int | None = None
    can_edit: bool | None = False
    can_delete: bool | None = False
    can_share: bool | None = False

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