from sqlalchemy.orm import Session

from app.models.note import Note
from app.models.share import Share
from app.models.user import User
from app.utils.common import is_note_owner


def is_owner(
    db: Session,
    user_id: int,
    note_id: int
) -> Note:
    return db.query(Note).filter(Note.id == note_id, Note.owner_id == user_id).first()


def can_share(
    db: Session,
    user_id: int,
    note_id: int
) -> Share:
    return db.query(Share).filter(Share.note_id == note_id, Share.user_id == user_id, Share.can_share).first()


def not_owner_and_not_can_share(
    db: Session,
    user_id: int,
    note_id: int
) -> bool:
    return not is_owner(db, user_id, note_id) and not can_share(db, user_id, note_id)
