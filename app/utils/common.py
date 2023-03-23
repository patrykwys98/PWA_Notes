from sqlalchemy import and_, or_

from app.models.note import Note
from app.models.share import Share
from app.models.user import User


def is_note_owner(db, user_id, note_id):
    return db.query(Note).filter(and_(Note.id == note_id, Note.owner_id == user_id)).first()
