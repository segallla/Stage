import sqlite3
import asyncio
from typing import Any, List


class Database:
    """Simplified async wrapper around sqlite3."""

    def __init__(self, url: str):
        self.url = url.split("///")[-1]
        self._conn: sqlite3.Connection | None = None

    async def connect(self) -> None:
        self._conn = sqlite3.connect(self.url)
        self._conn.execute("PRAGMA foreign_keys = ON")

    async def fetch_all(self, query: str, args: List[Any] | None = None) -> List[tuple]:
        assert self._conn
        return await asyncio.to_thread(self._conn.execute, query, args or []).fetchall()

    async def execute(self, query: str, args: List[Any] | None = None) -> None:
        assert self._conn
        await asyncio.to_thread(self._conn.execute, query, args or [])
        await asyncio.to_thread(self._conn.commit)


async def get_db(settings) -> Database:
    db = Database(settings.database_url)
    await db.connect()
    return db
