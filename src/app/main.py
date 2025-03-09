from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.core.config import settings


def get_application():
    _app = FastAPI(
        title=settings.PROJECT_NAME,
        description=settings.PROJECT_DESCRIPTION,
        version="0.1"
    )

    _app.add_middleware(
        CORSMiddleware,
        allow_origins=[str(origin) for origin in settings.BACKEND_CORS_ORIGINS],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    return _app


app = get_application()

@app.get('/', status_code=200)
async def home():
    data = {
        'name': settings.PROJECT_NAME,
        'description': settings.PROJECT_DESCRIPTION,
        'version': settings.PROJECT_VERSION
    }
    return { 'data': data }
