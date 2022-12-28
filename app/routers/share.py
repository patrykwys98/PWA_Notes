from fastapi import APIRouter, Depends, HTTPException, Response, status
from sqlalchemy.orm import Session

from app.db.get_db import get_db
from app.services.share import share_note
from app.schemas.share import ShareNoteCreateSchema

router = APIRouter()

@router.post('/share-note/')
async def share_note_endpoint(
    shared_note: ShareNoteCreateSchema, 
    db: Session = Depends(get_db), 
    # user: User = Depends(get_current_user)
):
    return await share_note(db=db, shared_note=shared_note)
