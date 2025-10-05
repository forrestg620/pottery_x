from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def list_posts():
    return [
        {"id": 1, "title": "My first pottery bowl", "tag": "Showcase"},
        {"id": 2, "title": "How to glaze properly", "tag": "Instruction"}
    ]
