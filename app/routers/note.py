from fastapi import Depends, HTTPException, status, APIRouter, Response
from sqlalchemy.orm import Session

from app.schemas.note import NoteSchema
from app.db.get_db import get_db

from app.services.note import NoteService


router = APIRouter()


@router.post('/add-note/', response_model=NoteSchema)
def add_note_endpoint(note: NoteSchema, db: Session = Depends(get_db)):
    return NoteService.add_note(db=db, note=note)
