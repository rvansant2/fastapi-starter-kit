# app/api/home.py
from fastapi import APIRouter
from app.core.config import settings

router = APIRouter()

@router.get("/", status_code=200)
async def home():
    return {
        "data": {
            "name": settings.PROJECT_NAME,
            "description": settings.PROJECT_DESCRIPTION,
            "version": settings.PROJECT_VERSION,
        }
    }