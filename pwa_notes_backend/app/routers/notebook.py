from fastapi import Depends, APIRouter
from sqlalchemy.orm import Session

from app.schemas.notebook import Notebook as NotebookSchema
from app.services.notebook import add_notebook

from app.db.get_db import get_db


router = APIRouter()


@router.post('/add-notebook/', response_model=NotebookSchema)
def add_notebook_endpoint(notebook: NotebookSchema, db: Session = Depends(get_db)):
    return add_notebook(db=db, notebook=notebook)

