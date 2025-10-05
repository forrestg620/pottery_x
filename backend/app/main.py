import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api import posts, users

app = FastAPI(title="Pottery Sharing Platform")

origins = os.getenv("CORS_ORIGINS", "").split(",") if os.getenv("CORS_ORIGINS") else ["http://localhost:5173"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(posts.router, prefix="/posts", tags=["Posts"])
app.include_router(users.router, prefix="/users", tags=["Users"])

@app.get("/")
def root():
    return {"ok": True}