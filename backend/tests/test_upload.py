import json
import asyncio
from backend.upload import upload

class FakeRequest:
    def __init__(self, data: bytes):
        self.data = data
    async def body(self) -> bytes:
        return self.data

class FakeDB:
    async def execute(self, *args, **kwargs):
        pass

def test_upload():
    req = FakeRequest(json.dumps({"type":"FeatureCollection","features":[]}).encode())
    res = asyncio.run(upload(request=req, db=FakeDB()))
    assert res["status"] == "ok"
