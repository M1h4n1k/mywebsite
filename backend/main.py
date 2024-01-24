from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from routes import router
from fastapi.middleware.cors import CORSMiddleware
import os

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost", "http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
if not os.path.exists('uploads'):
    os.makedirs('uploads')
# should be done with nginx
app.mount("/uploads", StaticFiles(directory="uploads"), name="uploads")

app.include_router(router)
