import asyncio
from typing import Optional

from fastapi import FastAPI
from fastapi.responses import StreamingResponse


app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}


async def ping_streaming_fn():
    while True:
        yield "bim\n"
        await asyncio.sleep(0.01)


@app.get("/ping/{host}")
async def ping_handler(host):
    return StreamingResponse(
        ping_streaming_fn(), media_type="text/plain; charset=utf-8"
    )
