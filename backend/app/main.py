from fastapi import FastAPI
from app.api import posts, users

app = FastAPI(title="Pottery Sharing Platform")

# Routers
app.include_router(posts.router, prefix="/posts", tags=["Posts"])
app.include_router(users.router, prefix="/users", tags=["Users"])

@app.get("/")
def read_root():
    return {"message": "Welcome to the Pottery Sharing Platform!"}
