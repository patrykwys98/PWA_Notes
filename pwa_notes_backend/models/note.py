from sqlalchemy import Column, DateTime, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

Base = declarative_base()

class Note(Base):
    __tablename__ = 'note'
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    content = Column(String)
    time_created = Column(DateTime(timezone=True), server_default=func.now())
    time_updated = Column(DateTime(timezone=True), onupdate=func.now())
    notebook_id = Column(Integer, ForeignKey("notebook.id"))
    notebook = relationship("Notebook")


class Notebook(Base):
    __tablename__ = 'notebook'
    title = Column(String)
    time_created = Column(DateTime(timezone=True), server_default=func.now())
    time_updated = Column(DateTime(timezone=True), onupdate=func.now())