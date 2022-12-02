from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.get_db import get_db
from app.models import User
from app.schemas.notebook import NotebookSchema, NotebooksSchema
from app.services.auth import get_current_user
from app.services.notebook import add_notebook, get_notebooks

router = APIRouter()


@router.post('/add-notebook/', response_model=NotebookSchema)
async def add_notebook_endpoint(
    notebook: NotebookSchema,
    db: Session = Depends(get_db),
    user: User = Depends(get_current_user)
):
    return await add_notebook(db=db, notebook=notebook, user=user)


@router.get('/get-notebooks/')
async def get_notebooks_endpoint(
    db: Session = Depends(get_db),
    user: User = Depends(get_current_user)
):
    # TODO: PACK IN SCHEMA, RESPONSE SCHEMA
    return await get_notebooks(db=db, user=user)
