from fastapi import HTTPException, status
from sqlalchemy import and_, func, or_
from sqlalchemy.orm import Session

from app.models.note import Note
from app.schemas.note import NoteSchema, NotesToTreeSchema
from app.schemas.user import UserSchema


async def add_note(db: Session, note: NoteSchema, user: UserSchema):
    db_note = Note(title=note.title, content=note.content,
                   child_id=note.child_id, owner_id=user.id)
    db.add(db_note)
    db.commit()
    db.refresh(db_note)
    return db_note


# async def get_notes(db: Session, ):
#     notes = db.query(Note).filter().all()
#     if not notes:
#         return []
#     return notes


async def get_note(db: Session, note_id: int, user: UserSchema):
    note = db.query(Note).filter(
        and_(Note.id == note_id, Note.owner_id == user.id)).first()
    return note


async def delete_note(db: Session, note_id: int, user: UserSchema):
    note = db.query(Note).filter(
        and_(Note.id == note_id, user.id == user.id)).first()
    db.delete(note)
    db.commit()
    return note


async def update_note(db: Session, note_id: int, note: NoteSchema, user: UserSchema):
    db_note = db.query(Note).filter(
        and_(Note.id == note_id, Note.owner_id == user.id)).first()
    db_note.title = note.title
    db_note.content = note.content
    # db_note.children = note.children
    db_note.child_id = note.child_id
    db.commit()
    db.refresh(db_note)
    return db_note


async def get_notes_tree(db: Session, user: UserSchema):
    notes = db.query(Note).filter(Note.owner_id == user.id).all()
    # notes_to_return = []
    # childs_ids = []
    # if not notes:
    #     return []
    # for note in notes:
    #     childrens = [child for child in notes if child.child_id == note.id]
    #     if childrens:
    #         for child in childrens:
    #             childs_ids.append(child.id)
    #     note.children = childrens
    #     if note.id not in childs_ids:
    #         notes_to_return.append(note)

    return list(map(lambda x: NotesToTreeSchema.from_orm(x), notes))


async def update_tree_structure(db: Session, q: list[NotesToTreeSchema], user: UserSchema):
    for note in q:
        db_note = db.query(Note).filter(
            and_(Note.id == note.id, Note.owner_id == user.id)).first()
        db_note.child_id = note.child_id
        db.commit()
        db.refresh(db_note)
    return note
