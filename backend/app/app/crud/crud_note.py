

from typing import Union

from sqlalchemy.orm import Session

from app.crud.base import CRUDBase
from app.models.note import Note
from app.models.user import User
from app.schemas.note import NoteCreate, NoteUpdateRestricted, NoteUpdate


class CRUDNote(CRUDBase[Note, NoteCreate, NoteUpdate]):
    def update(
        self,
        db: Session,
        *,
        db_obj: User,
        obj_in: Union[NoteUpdate, NoteUpdateRestricted]
    ) -> Note:
        db_obj = super().update(db, db_obj=db_obj, obj_in=obj_in)
        return db_obj


recipe = CRUDNote(Note)