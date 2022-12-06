from sqlalchemy.orm import Session

from app.models.notebook import Notebook
from app.schemas.notebook import NotebookSchema, GetNotebooksListSchema
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
    return list(map(GetNotebooksListSchema.from_orm, notes))


async def get_notebook(db: Session, notebook_id: int, user: UserSchema):
    notebook = db.query(Notebook).filter_by(
        id=notebook_id, owner_id=user.id).first()
    return notebook


async def delete_notebook(db: Session, notebook_id: int, user: UserSchema):
    notebook = db.query(Notebook).filter_by(
        id=notebook_id, owner_id=user.id).first()
    db.delete(notebook)
    db.commit()
    return notebook


async def update_notebook(db: Session, notebook_id: int, notebook: NotebookSchema, user: UserSchema):
    db_notebook = db.query(Notebook).filter_by(
        id=notebook_id, owner_id=user.id).first()
    db_notebook.title = notebook.title
    db.commit()
    db.refresh(db_notebook)
    return db_notebook
