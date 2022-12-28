from sqlalchemy.orm import Session
from fastapi import Depends, HTTPException, status
from app.models.user import User
from app.schemas.user import UserSchema

from app.models.share import Share
from app.schemas.share import ShareNoteGetSchema
from sqlalchemy import and_, or_

async def share_note(shared_note: ShareNoteGetSchema, db: Session):
    """
    TODO: DONT SHARE TO YOURSELF AND MAKE IT EASIEST
    """
    if type(shared_note.user_id) is list:
        for user_id in shared_note.user_id:
            duplicate = db.query(Share).filter(and_(Share.note_id == shared_note.note_id, Share.user_id == user_id)).first()
            if duplicate:
                raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Already shared for user_id: " + str(user_id))
            else: 
                db_share = Share(**shared_note.dict())
            db_share.user_id = user_id
            db.add(db_share)
            db.commit()
            db.refresh(db_share)
            return db_share
    else: 
        duplicate = db.query(Share).filter(and_(Share.note_id == shared_note.note_id, Share.user_id == shared_note.user_id)).first()
        if duplicate:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Already shared for user_id: " + str(shared_note.user_id))
        db_share = Share(**shared_note.dict())
        db.add(db_share)
        db.commit()
        db.refresh(db_share)
        return db_share

