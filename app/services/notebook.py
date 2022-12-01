from sqlalchemy.orm import Session

from app.models.notebook import Notebook
from app.schemas.notebook import NotebookSchema
from app.schemas.user import UserSchema


def add_notebook(db: Session, notebook: NotebookSchema, user: UserSchema):
    db_notebook = Notebook(title=notebook.title, owner_id=user.id)
    db.add(db_notebook)
    db.commit()
    return db_notebook
