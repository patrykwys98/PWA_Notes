from sqlalchemy.orm import Session

from app.models.notebook import Notebook
from app.schemas.notebook import NotebookSchema, NotebooksSchema
from app.schemas.user import UserSchema


async def add_notebook(db: Session, notebook: NotebookSchema, user: UserSchema):
    db_notebook = Notebook(title=notebook.title, owner_id=user.id)
    db.add(db_notebook)
    db.commit()
    db.refresh(db_notebook)
    return db_notebook


async def get_notebooks(db: Session, user: UserSchema):
    notes = db.query(Notebook).filter_by(owner_id=user.id)
    #TODO: SCHEMA
    return list(map(NotebookSchema.from_orm, notes))
