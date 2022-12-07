from sqlalchemy import Column, DateTime, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from sqlalchemy_utils import LtreeType

from app.db.database import Base


class Note(Base):
    __tablename__ = 'note'
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    content = Column(String)
    time_created = Column(DateTime(timezone=True), server_default=func.now())
    time_updated = Column(DateTime(timezone=True), onupdate=func.now())
    notebook_id = Column(Integer, ForeignKey("notebook.id"))
    path = Column(LtreeType, nullable=False)

    notebook = relationship("Notebook", back_populates="notes")

    def __str__(self):
        return self.name

    def __repr__(self):
        return 'Node({})'.format(self.name)
