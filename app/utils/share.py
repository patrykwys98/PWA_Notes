from app.models.share import Share
from app.models.user import User
from app.models.note import Note
from sqlalchemy import and_, or_


def is_owner(db, user_id, note_id):
    return db.query(Note).filter(and_(Note.id == note_id, Note.owner_id == user_id)).first()


def can_share(db, user_id, note_id):
    return db.query(Share).filter(and_(Share.note_id == note_id, Share.user_id == user_id, Share.can_share == True)).first()

def not_owner_and_not_can_share(db, user_id, note_id):
    return not is_owner(db, user_id, note_id) and not can_share(db, user_id, note_id)