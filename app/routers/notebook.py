from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.get_db import get_db
from app.schemas.notebook import NotebookSchema
from app.services.notebook import add_notebook
from app.models import User
from app.services.auth import get_current_user

router = APIRouter()


@router.post('/add-notebook/', response_model=NotebookSchema)
def add_notebook_endpoint(notebook: NotebookSchema, db: Session = Depends(get_db), user: User = Depends(get_current_user)):
    return add_notebook(db=db, notebook=notebook, user=user)
