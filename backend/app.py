from fastapi import FastAPI
from .nlq import router as nlq_router
from .upload import router as upload_router
from .models import datasources

app = FastAPI(title="Open Geo Copilot")


@app.get("/healthz")
async def healthz():
    return {"status": "ok"}


@app.get("/datasources")
async def get_datasources():
    return datasources


app.include_router(nlq_router)
app.include_router(upload_router)
