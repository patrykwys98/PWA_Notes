import os

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routers import auth, note, share, user

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

#! Routes
app.include_router(note.router, tags=['Note'], prefix='/api/note')
app.include_router(user.router, tags=['User'], prefix='/api/user')
app.include_router(auth.router, tags=['Auth'], prefix='/api/auth')
app.include_router(share.router, tags=['Share'], prefix='/api/share')

@app.get("/")
async def root():
    return {'message': 'Hello world'}
