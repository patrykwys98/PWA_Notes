import os
from fastapi import FastAPI
from fastapi_sqlalchemy import DBSessionMiddleware, db

from dotenv import load_dotenv
from app.schemas.note import Note as NoteSchema
from app.schemas.notebook import Notebook as NotebookSchema
from app.models.note import Note
from app.models.notebook import Notebook

load_dotenv(".env")

app = FastAPI()
app.add_middleware(DBSessionMiddleware, db_url=os.environ['DATABASE_URL'])

@app.get("/")
async def root():
    return {'message': 'Hello world'}


@app.post('/add-note/', response_model=NoteSchema)
def add_note(note: NoteSchema):
    db_note = Note(title=note.title, content=note.content, notebook_id=note.notebook_id)
    db.session.add(db_note)
    db.session.commit()
    return db_note


@app.post('/add-notebook/', response_model=NotebookSchema)
def add_notebook(notebook: NotebookSchema):
    db_notebook = Notebook(title=notebook.title)
    db.session.add(db_notebook)
    db.session.commit()
    return db_notebook


@app.get("/notes/")
def get_books():
    notes = db.session.query(Note).all()

    return notes
