from fastapi import APIRouter, Depends, HTTPException, Response, status
from sqlalchemy.orm import Session

from app.db.get_db import get_db
from app.models import User
from app.schemas.note import (NoteCreateSchema, NoteRenameSchema, NoteSchema,
                              NotesToTreeSchema)
from app.services.auth import get_current_user
from app.services.note import (add_note, delete_note, get_note,
                               get_notes_and_shared_notes, rename_note,
                               search_in_title_and_content, update_note,
                               update_tree_structure)

router = APIRouter()


@router.post('/add-note/')
async def add_note_endpoint(
    note: NoteCreateSchema,
    db: Session = Depends(get_db),
    user: User = Depends(get_current_user)
):
    return await add_note(db=db, note=note, user=user)


@router.get('/get-note/{note_id}/')
async def get_note_endpoint(
    note_id: int,
    db: Session = Depends(get_db),
    user: User = Depends(get_current_user)
):
    return await get_note(db=db, note_id=note_id, user=user)


@router.delete('/delete-note/{note_id}/')
async def delete_note_endpoint(
    note_id: int,
    db: Session = Depends(get_db),
    user: User = Depends(get_current_user)
):
    return await delete_note(db=db, note_id=note_id, user=user)


@router.put('/update-note/{note_id}/')
async def update_note_endpoint(
    note_id: int,
    note: NoteSchema,
    db: Session = Depends(get_db),
    user: User = Depends(get_current_user)
):
    return await update_note(db=db, note_id=note_id, note=note, user=user)


@router.post('/update-tree-structure/')
async def update_tree_structure_endpoint(
    q: list[NotesToTreeSchema],
    db: Session = Depends(get_db),
    user: User = Depends(get_current_user)
):
    return await update_tree_structure(db=db, q=q, user=user)


@router.put('/rename-note/{note_id}/')
async def rename_note_endpoint(
    note_id: int,
    title: NoteRenameSchema,
    db: Session = Depends(get_db),
    user: User = Depends(get_current_user)
):
    return await rename_note(db=db, note_id=note_id, title=title.title, user=user)


@router.get('/get-notes-and-shared-notes/')
async def get_notes_and_shared_notes_endpoint(
    db: Session = Depends(get_db),
    user: User = Depends(get_current_user)
):
    return await get_notes_and_shared_notes(db=db, user=user)


@router.get('/search-in-title-and-content/{query}/')
async def search_in_title_and_content_endpoint(
    query: str,
    db: Session = Depends(get_db),
    user: User = Depends(get_current_user)
):
    return await search_in_title_and_content(db=db, query=query, user=user)
