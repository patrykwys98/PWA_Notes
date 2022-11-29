import os

from fastapi import FastAPI

from app.routers import auth, note, notebook, user

app = FastAPI()

#! Routes
app.include_router(note.router, tags=['Note'], prefix='/api/note')
app.include_router(notebook.router, tags=['Notebook'], prefix='/api/notebook')
app.include_router(user.router, tags=['User'], prefix='/api/user')
app.include_router(auth.router, tags=['Auth'], prefix='/api/auth')


@app.get("/")
async def root():
    return {'message': 'Hello world'}
