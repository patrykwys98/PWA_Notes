from fastapi import Depends, HTTPException, status
from sqlalchemy import and_, or_
from sqlalchemy.orm import Session

from app.models.share import Share
from app.models.user import User
from app.schemas.share import ShareNoteGetSchema, UnshareNoteSchema
from app.schemas.user import UserSchema
from app.utils.share import not_owner_and_not_can_share


async def share_note(shared_note: ShareNoteGetSchema, db: Session, user: UserSchema):
    if not_owner_and_not_can_share(db, user.id, shared_note.note_id):
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                            detail="You can't share this note")
    for user_id in shared_note.user_id:
        duplicate = db.query(Share).filter(and_(Share.note_id == shared_note.note_id, Share.user_id == user_id)).first()
        if duplicate:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Already shared for user_id: " + str(user_id))
        else: 
            db_share = Share(**shared_note.dict())
            db_share.can_view = True
            db_share.user_id = user_id
            db.add(db_share)
            db.commit()
            db.refresh(db_share)
    return {'message': 'Note shared'}
    


async def get_share_info_about_note(db: Session, note_id: int, user: UserSchema):
    if not_owner_and_not_can_share(db, user.id, note_id):
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                            detail="You can't get info about this note")
    db_query = db.query(Share).filter(and_(Share.note_id == note_id)).all()
    for share in db_query:
       share.username = db.query(User).filter(User.id == share.user_id).first().username
    return db_query


async def unshare_note_for_user(shared_note: UnshareNoteSchema, db: Session, user: UserSchema):
    if not_owner_and_not_can_share(db, user.id, shared_note.note_id):
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                            detail="You can't unshare this note")
    db_share = db.query(Share).filter(and_(Share.note_id == shared_note.note_id, Share.user_id == shared_note.user_id)).first()
    if not db_share:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Not shared for user_id: " + str(shared_note.user_id))
    else:
        db_share.can_view = False
        db.commit()
        db.refresh(db_share)
    return {'message': 'Note unshared'}


async def update_share_note_for_user(shared_note: UnshareNoteSchema, db: Session, user: UserSchema):
    if not_owner_and_not_can_share(db, user.id, shared_note.note_id):
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                            detail="You can't update share this note")
    db_share = db.query(Share).filter(and_(Share.note_id == shared_note.note_id, Share.user_id == shared_note.user_id)).first()
    if not db_share:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Not shared for user_id: " + str(shared_note.user_id))
    else:
        db_share.can_view = shared_note.can_view
        db_share.can_edit = shared_note.can_edit
        db_share.can_delete = shared_note.can_delete
        db_share.can_share = shared_note.can_share
        db.commit()
        db.refresh(db_share)
    return {'message': 'Note updated'}