from fastapi import APIRouter, Depends, HTTPException, Response, status
from sqlalchemy.orm import Session

from app.db.get_db import get_db
from app.models import User
from app.schemas.share import (ShareNoteCreateSchema, ShareNoteUpdateSchema,
                               UnshareNoteSchema)
from app.services.auth import get_current_user
from app.services.share import (get_share_info_about_note, share_note,
                                unshare_note_for_user,
                                update_share_note_for_user)

router = APIRouter()


@router.post('/share-note/')
async def share_note_endpoint(
    shared_note: ShareNoteCreateSchema,
    db: Session = Depends(get_db),
    user: User = Depends(get_current_user)
):
    return await share_note(db=db, shared_note=shared_note, user=user)


@router.get('/get-share-info-about-note/{note_id}/')
async def get_share_info_about_note_endpoint(
    note_id: int,
    db: Session = Depends(get_db),
    user: User = Depends(get_current_user)
):
    return await get_share_info_about_note(db=db, note_id=note_id, user=user)


@router.post('/unshare-note-for-user/')
async def unshare_note_for_user_endpoint(
    shared_note: UnshareNoteSchema,
    db: Session = Depends(get_db),
    user: User = Depends(get_current_user)
):
    return await unshare_note_for_user(db=db, shared_note=shared_note, user=user)


@router.post('/update-share-note-for-user/')
async def update_share_note_for_user_endpoint(
    shared_note: ShareNoteUpdateSchema,
    db: Session = Depends(get_db),
    user: User = Depends(get_current_user)
):
    return await update_share_note_for_user(db=db, shared_note=shared_note, user=user)
