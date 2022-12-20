from sqlalchemy import (Column, DateTime, ForeignKey, Index, Integer, Sequence,
                        String)
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from app.db.database import Base, engine


class Note(Base):
    __tablename__ = 'note'
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    content = Column(String, nullable=True)
    time_created = Column(DateTime(timezone=True), server_default=func.now())
    time_updated = Column(DateTime(timezone=True), onupdate=func.now())
    owner_id = Column(Integer, ForeignKey("user.id"))

    child_id = Column(Integer, ForeignKey('note.id'), nullable=True)
    children = relationship('Note', remote_side=[id], uselist=True)

    owner = relationship("User", back_populates="notes")
