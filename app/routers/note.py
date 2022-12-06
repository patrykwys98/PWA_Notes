from fastapi import APIRouter, Depends, HTTPException, Response, status
from sqlalchemy.orm import Session

from app.db.get_db import get_db
from app.schemas.note import NoteSchema
from app.services.note import add_note, get_notes, get_note, delete_note, update_note

router = APIRouter()


@router.post('/add-note/', response_model=NoteSchema)
async def add_note_endpoint(note: NoteSchema, db: Session = Depends(get_db)):
    return await add_note(db=db, note=note)


@router.get('/get-notes/{notebook_id}')
async def get_notes_endpoint(notebook_id: int, db: Session = Depends(get_db)):
    return await get_notes(db=db, notebook_id=notebook_id)


@router.get('/get-note/{note_id}')
async def get_note_endpoint(note_id: int, db: Session = Depends(get_db)):
    return await get_note(db=db, note_id=note_id)


@router.delete('/delete-note/{note_id}')
async def delete_note_endpoint(note_id: int, db: Session = Depends(get_db)):
    return await delete_note(db=db, note_id=note_id)


@router.put('/update-note/{note_id}')
async def update_note_endpoint(note_id: int, note: NoteSchema, db: Session = Depends(get_db)):
    return await update_note(db=db, note_id=note_id, note=note)
