import os
from fastapi import FastAPI

from app.routers import note, notebook, user


app = FastAPI()

#! Routes
app.include_router(note.router, tags=['Note'], prefix='/api/note')
app.include_router(notebook.router, tags=['Notebook'], prefix='/api/notebook')
app.include_router(user.router, tags=['User'], prefix='/api/user')


@app.get("/")
async def root():
    return {'message': 'Hello world'}
