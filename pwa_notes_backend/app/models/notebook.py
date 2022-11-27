from sqlalchemy import Column, DateTime, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from app.models.base import Base


class Notebook(Base):
    __tablename__ = 'notebook'
    id = Column(Integer, primary_key=True)
    title = Column(String)
    time_created = Column(DateTime(timezone=True), server_default=func.now())
    time_updated = Column(DateTime(timezone=True), onupdate=func.now())