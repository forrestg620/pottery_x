from fastapi import APIRouter

router = APIRouter()

@router.get("/{user_id}")
def get_user(user_id: int):
    return {"id": user_id, "username": f"user_{user_id}", "bio": "Pottery enthusiast"}
