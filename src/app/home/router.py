# app/home/router.py
from fastapi import APIRouter, status
from app.core.config import settings
from app.home.models import HomeResponse

router = APIRouter()


@router.get("/", response_model=HomeResponse, status_code=status.HTTP_200_OK)
async def home():
    return {
        "data": {
            "name": settings.PROJECT_NAME,
            "description": settings.PROJECT_DESCRIPTION,
            "version": settings.PROJECT_VERSION,
        }
    }
