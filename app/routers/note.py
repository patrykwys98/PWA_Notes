from fastapi import APIRouter, Depends, HTTPException, Response, status
from sqlalchemy.orm import Session

from app.db.get_db import get_db
from app.schemas.note import NoteSchema
from app.services.note import add_note

router = APIRouter()


@router.post('/add-note/', response_model=NoteSchema)
async def add_note_endpoint(note: NoteSchema, db: Session = Depends(get_db)):
    return await add_note(db=db, note=note)
