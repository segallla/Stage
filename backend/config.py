from pydantic import BaseSettings


class Settings(BaseSettings):
    """Application settings."""

    database_url: str = "sqlite+aiosqlite:///./test.db"
    openai_api_key: str = ""

    class Config:
        env_file = ".env"


def get_settings() -> Settings:
    """Return settings singleton."""
    return Settings()
