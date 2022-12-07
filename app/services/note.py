from sqlalchemy.orm import Session

from app.models.note import Note
from app.schemas.note import NoteSchema
from sqlalchemy_utils import Ltree


async def add_note(db: Session, note: NoteSchema):
    db_note = Note(title=note.title, content=note.content,
                   notebook_id=note.notebook_id, path=Ltree(note.path))
    db.add(db_note)
    db.commit()
    db.refresh(db_note)
    return db_note


async def get_notes(db: Session, notebook_id: int):
    notes = db.query(Note).filter(Note.notebook_id == notebook_id).all()
    if not notes:
        return []
    return notes


async def get_note(db: Session, note_id: int):
    note = db.query(Note).filter(Note.id == note_id).first()
    return note


async def delete_note(db: Session, note_id: int):
    note = db.query(Note).filter(Note.id == note_id).first()
    db.delete(note)
    db.commit()
    return note


async def update_note(db: Session, note_id: int, note: NoteSchema):
    db_note = db.query(Note).filter(Note.id == note_id).first()
    db_note.title = note.title
    db_note.content = note.content
    db.commit()
    db.refresh(db_note)
    return db_note
