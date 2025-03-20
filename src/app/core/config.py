from typing import Any, List, Optional, Union

from pydantic import AnyHttpUrl, PostgresDsn, field_validator, FieldValidationInfo
from pydantic_settings import BaseSettings
import os

ENVIRONMENT = os.getenv("ENVIRONMENT", "development")


class Settings(BaseSettings):
    PROJECT_NAME: str
    PROJECT_DESCRIPTION: str
    PROJECT_VERSION: str
    BACKEND_CORS_ORIGINS: List[AnyHttpUrl] = []
    API_PORT: str
    JWT_SECRET_KEY: str

    @field_validator("BACKEND_CORS_ORIGINS", mode="before")
    def assemble_cors_origins(cls, v: Union[str, List[str]]) -> Union[List[str], str]:
        if isinstance(v, str) and not v.startswith("["):
            return [i.strip() for i in v.split(",")]
        elif isinstance(v, (list, str)):
            return v
        raise ValueError(v)

    POSTGRES_SERVER: str
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_DB: str
    DATABASE_URI: Optional[PostgresDsn] = None

    @field_validator("DATABASE_URI", mode="before")
    def assemble_db_connection(cls, v: Optional[str], info: FieldValidationInfo) -> Any:
        if isinstance(v, str):
            return v
        user = info.data.get("POSTGRES_USER")
        password = info.data.get("POSTGRES_PASSWORD")
        host = info.data.get("POSTGRES_SERVER")
        db = info.data.get("POSTGRES_DB") or ""

        # Conditional for init_db.py file
        if ENVIRONMENT != "docker":
            host = "localhost"

        return f"postgresql://{user}:{password}@{host}/{db}"

    class Config:
        case_sensitive = True
        env_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "..", ".env")
        # print(env_file)


settings = Settings()
