"""
This module defines a settings class using Pydantic for managing environment variables.
"""

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    #Settings class for managing environment variables.
    DATABASE_HOST: str = "db"
    POSTGRES_USER: str = "root"
    POSTGRES_PASSWORD: str = "root"
    POSTGRES_DB: str = "root"
    secret_key: str = "$oE@{aG(9:8£EdxQ=7o)EJa3"

    class Config:
        #Configuration settings.
        env_file = ".env"

settings = Settings()