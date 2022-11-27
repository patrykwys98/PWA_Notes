import os
from fastapi import FastAPI

from app.routers import note, notebook


app = FastAPI()

app.include_router(note.router, tags=['Note'], prefix='/api/note')
app.include_router(notebook.router, tags=['Notebook'], prefix='/api/notebook')

@app.get("/")
async def root():
    return {'message': 'Hello world'}





