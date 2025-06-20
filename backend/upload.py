import json
from fastapi import APIRouter, HTTPException, status, Depends, Request
from .deps import db_dep

router = APIRouter()


@router.post("/upload", status_code=status.HTTP_201_CREATED)
async def upload(request: Request, db=Depends(db_dep)):
    """Accept GeoJSON uploads as raw body."""
    data = await request.body()
    if len(data) > 10 * 1024 * 1024:
        raise HTTPException(413, "File too large")
    try:
        json.loads(data)
    except json.JSONDecodeError as exc:
        raise HTTPException(400, "Invalid JSON") from exc
    await db.execute("CREATE TABLE IF NOT EXISTS uploads (id INTEGER)")
    return {"status": "ok"}
