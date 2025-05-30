import asyncio
import os

from jinja2 import Environment, PackageLoader, select_autoescape
from ping3 import ping
from sanic import Sanic
from sanic.response import html, stream, text
from waky.conf import Config
from waky.core.inventory import Inventory
from waky.logging_config import configure_logging

configure_logging()

# define the environment for the Jinja2 templates
env = Environment(loader=PackageLoader("waky", "templates"), autoescape=select_autoescape(["html", "xml", "tpl"]))


# a function for loading an HTML template from the Jinja environment
def template(tpl, **kwargs):
    template = env.get_template(tpl)
    return html(template.render(kwargs))


config = Config()
app_home = os.path.dirname(os.path.abspath(__file__))
app = Sanic("waky")
app.static("/static", app_home + "/static")
inventory = Inventory()
inventory.load(config.devices)
inventory.run()


@app.route("/")
async def index(request):
    return template("index.html", title="Waky", devices=inventory.devices.values())


@app.route("/hosts")
async def hosts(request):
    return text(app.config.HOSTS)


@app.route("/ping/<host>")
async def ping_handler(request, host):
    async def ping_streaming_fn(response):
        while True:
            await response.write(str(round(ping(host, unit="ms"), 3)) + "\n")
            await asyncio.sleep(1)

    return stream(ping_streaming_fn, content_type="text/plain; charset=utf-8", chunked=True)


def main():
    app.run(host=config.listen, port=config.port, debug=config.debug)


if __name__ == "__main__":
    main()
