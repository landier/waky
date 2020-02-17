import asyncio
import os

from ping3 import ping
from sanic import Sanic
from sanic.response import json, stream, text
from sanic_brogz import Compress

app = Sanic("waky")
Compress(app)


@app.route("/")
async def index(request):
    return json({"hello": "world"})


@app.route("/hosts")
async def hosts(request):
    return text(app.config.HOSTS)


@app.route("/ping/<host>")
async def ping_handler(request, host):
    async def ping_streaming_fn(response):
        while True:
            await response.write(str(round(ping(host, unit="ms"), 3)) + "\n")
            await asyncio.sleep(1)

    return stream(ping_streaming_fn, content_type="text", chunked=True)


def main():
    if "WAKY_CONF" in os.environ:
        app.config.from_envvar("WAKY_CONF")
    debug = app.config.get("DEBUG", False)
    listening = app.config.get("LISTENING", "0.0.0.0")
    port = app.config.get("PORT", 8888)
    app.run(host=listening, port=port, debug=debug)


if __name__ == "__main__":
    main()
