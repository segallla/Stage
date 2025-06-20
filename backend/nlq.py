from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()


class NLQRequest(BaseModel):
    prompt: str


@router.post("/nlq")
async def nlq(req: NLQRequest):
    """Return fake SQL and bbox for prompt."""
    sql = "SELECT * FROM roads" if "road" in req.prompt else "SELECT 1"
    return {"sql": sql, "tiles_url": "http://tiles/{z}/{x}/{y}", "bbox": [-180, -90, 180, 90], "summary": "demo"}
