from sqlalchemy.orm import Session

from app.models.note import Note
from app.models.share import Share
from app.models.user import User
from app.utils.common import is_note_owner


def can_edit(db: Session, user_id: int, note_id: int) -> Share:
    return db.query(Share).filter(Share.note_id == note_id, Share.user_id == user_id, Share.can_edit).first()


def can_delete(db: Session, user_id: int, note_id: int) -> Share:
    return db.query(Share).filter(Share.note_id == note_id, Share.user_id == user_id, Share.can_delete).first()


def can_view(db: Session, user_id: int, note_id: int) -> Share:
    return db.query(Share).filter(Share.note_id == note_id, Share.user_id == user_id, Share.can_view).first()


def not_owner_and_not_can_edit(db: Session, user_id: int, note_id: int) -> bool:
    return not is_note_owner(db, user_id, note_id) and not can_edit(db, user_id, note_id)


def not_owner_and_not_can_delete(db: Session, user_id: int, note_id: int) -> bool:
    return not is_note_owner(db, user_id, note_id) and not can_delete(db, user_id, note_id)


def not_owner_and_not_can_view(db: Session, user_id: int, note_id: int) -> bool:
    return not is_note_owner(db, user_id, note_id) and not can_view(db, user_id, note_id)
