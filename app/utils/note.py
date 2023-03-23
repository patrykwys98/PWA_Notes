import spacy
from bs4 import BeautifulSoup
from spacy import displacy
from sqlalchemy import and_, or_
from spacy.language import Language

from app.models.note import Note
from app.models.share import Share
from app.models.user import User
from app.utils.common import is_note_owner


def can_edit(db, user_id, note_id):
    return db.query(Share).filter(and_(Share.note_id == note_id, Share.user_id == user_id, Share.can_edit == True)).first()

def can_delete(db, user_id, note_id):
    return db.query(Share).filter(and_(Share.note_id == note_id, Share.user_id == user_id, Share.can_delete == True)).first()

def can_view(db, user_id, note_id):
    return db.query(Share).filter(and_(Share.note_id == note_id, Share.user_id == user_id, Share.can_view == True)).first()

def not_owner_and_not_can_edit(db, user_id, note_id):
    return not is_note_owner(db, user_id, note_id) and not can_edit(db, user_id, note_id)

def not_owner_and_not_can_delete(db, user_id, note_id):
    return not is_note_owner(db, user_id, note_id) and not can_delete(db, user_id, note_id)

def not_owner_and_not_can_view(db, user_id, note_id):
    return not is_note_owner(db, user_id, note_id) and not can_view(db, user_id, note_id)
