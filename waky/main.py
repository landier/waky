import os
from sanic import Sanic
from sanic.response import json

app = Sanic("waky")

@app.route("/")
async def test(request):
    return json({"hello": "world"})

def main():
    if 'WAKY_CONF' in os.environ:
        app.config.from_envvar('WAKY_CONF')
    debug = app.config.get("DEBUG", False)
    listening = app.config.get("LISTENING", "0.0.0.0")
    port = app.config.get("PORT", 8000)
    app.run(host=listening, port=port, debug=debug)

if __name__ == "__main__":
    main()
