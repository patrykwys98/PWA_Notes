from sqlalchemy.orm import Session

from app.models.notebook import Notebook
from app.schemas.notebook import NotebookSchema


def add_notebook(db: Session, notebook: NotebookSchema):
    db_notebook = Notebook(title=notebook.title)
    db.add(db_notebook)
    db.commit()
    return db_notebook
