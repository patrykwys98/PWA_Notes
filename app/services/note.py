from sqlalchemy.orm import Session

from app.models.note import Note

from app.schemas.note import NoteSchema


class NoteService(NoteSchema):
    """
    Note Service
    """
    def add_note(db: Session, note: NoteSchema):
        db_note = Note(title=note.title, content=note.content,
                       notebook_id=note.notebook_id)
        db.add(db_note)
        db.commit()
        db.refresh(db_note)
        return db_note
