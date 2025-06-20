from fastapi import Depends
from .config import get_settings, Settings
from .db import get_db, Database


async def settings_dep() -> Settings:
    return get_settings()


async def db_dep(settings: Settings = Depends(settings_dep)) -> Database:
    db = await get_db(settings)
    return db
