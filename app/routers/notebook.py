from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.get_db import get_db
from app.models import User
from app.schemas.notebook import NotebookSchema, AddNotebookSchema
from app.services.auth import get_current_user
from app.services.notebook import add_notebook, get_notebooks, get_notebook, delete_notebook, update_notebook

router = APIRouter()


@router.post('/add-notebook/', response_model=AddNotebookSchema)
async def add_notebook_endpoint(
    notebook: AddNotebookSchema,
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


@router.get('/get-notebook/{notebook_id}')
async def get_notebook_endpoint(
    notebook_id: int,
    db: Session = Depends(get_db),
    user: User = Depends(get_current_user)
):
    return await get_notebook(db=db, notebook_id=notebook_id, user=user)


@router.delete('/delete-notebook/{notebook_id}')
async def delete_notebook_endpoint(
    notebook_id: int,
    db: Session = Depends(get_db),
    user: User = Depends(get_current_user)
):
    return await delete_notebook(db=db, notebook_id=notebook_id, user=user)


@router.put('/update-notebook/{notebook_id}')
async def update_notebook_endpoint(
    notebook_id: int,
    notebook: NotebookSchema,
    db: Session = Depends(get_db),
    user: User = Depends(get_current_user)
):
    return await update_notebook(db=db, notebook_id=notebook_id, notebook=notebook, user=user)
