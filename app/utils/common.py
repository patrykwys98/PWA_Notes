from sqlalchemy.orm import Session

from app.models.note import Note


def is_note_owner(
    db: Session,
    user_id: int,
    note_id: int
) -> bool:
    return db.query(Note).filter(Note.id == note_id, Note.owner_id == user_id).first() is not None
