import asyncio

from aiohttp import web
import toml

from web.app import RandomWebsiteApp


async def init(conf):
    app = web.Application()
    receiver = RandomWebsiteApp(conf['link_url'], conf['link_token'], conf['query'])
    app.router.add_get(r"/{redirect_context:.*}", receiver.on_get, name='redirect')
    return app


def main():
    with open("config.toml", 'r') as r:
        conf = toml.load(r)
    loop = asyncio.get_event_loop()
    app = loop.run_until_complete(init(conf))
    web.run_app(app, port=conf['port'])


if __name__ == '__main__':
    main()
