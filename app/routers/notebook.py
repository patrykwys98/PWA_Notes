from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.get_db import get_db
from app.schemas.notebook import NotebookSchema
from app.services.notebook import add_notebook

router = APIRouter()


@router.post('/add-notebook/', response_model=NotebookSchema)
def add_notebook_endpoint(notebook: NotebookSchema, db: Session = Depends(get_db)):
    return add_notebook(db=db, notebook=notebook)
