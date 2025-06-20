import asyncio
from backend.nlq import nlq, NLQRequest


def test_nlq():
    res = asyncio.run(nlq(NLQRequest(prompt="roads")))
    assert "SELECT" in res["sql"]
    assert len(res["bbox"]) == 4
