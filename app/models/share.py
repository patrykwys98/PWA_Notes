from sqlalchemy import (Boolean, Column, DateTime, ForeignKey, Index, Integer,
                        Sequence)
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from app.db.database import Base


class Share(Base):
    __tablename__ = 'share'
    note_id = Column(Integer, ForeignKey("note.id"), primary_key=True)
    user_id = Column(Integer, ForeignKey("user.id"), primary_key=True)
    can_edit = Column(Boolean, default=False)
    can_delete = Column(Boolean, default=False)
    can_share = Column(Boolean, default=False)
    time_created = Column(DateTime(timezone=True), server_default=func.now())
    time_updated = Column(DateTime(timezone=True), onupdate=func.now(), nullable=True)

    

    note = relationship("Note", back_populates="shared", cascade="all, delete")
    user = relationship("User", back_populates="shared")



