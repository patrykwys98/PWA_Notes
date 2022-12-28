from fastapi import APIRouter, Depends, HTTPException, Response, status
from sqlalchemy.orm import Session

from app.db.get_db import get_db
from app.models import User
from app.schemas.share import ShareNoteCreateSchema
from app.services.auth import get_current_user
from app.services.share import share_note

router = APIRouter()

@router.post('/share-note/')
async def share_note_endpoint(
    shared_note: ShareNoteCreateSchema, 
    db: Session = Depends(get_db), 
    user: User = Depends(get_current_user)
):
    return await share_note(db=db, shared_note=shared_note, user=user)
