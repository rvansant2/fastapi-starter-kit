from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

from app.core.config import settings
from app.home.router import router as home_router


def create_app() -> FastAPI:
    # Instantiate FastAPI
    app = FastAPI(
        title=settings.PROJECT_NAME,
        description=settings.PROJECT_DESCRIPTION,
        version=settings.PROJECT_VERSION
    )
    # Configure CORS middleware
    app.add_middleware(
        CORSMiddleware,
        allow_origins=[str(origin) for origin in settings.BACKEND_CORS_ORIGINS],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    # Include the home route without a prefix
    app.include_router(home_router, prefix="", tags=["home"])

    return app


app = create_app()

if __name__ == "main":
    # For development only reload=True
    uvicorn.run(
        "app.main:app",
        host="0.0.0.0",
        port=int(settings.API_PORT),
        reload=True
    )
