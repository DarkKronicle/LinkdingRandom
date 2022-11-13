from datetime import datetime

import aiohttp.web_request
from aiohttp import web
from aiolinkding import Client

from web.websites import Websites, Website


class RandomWebsiteApp:

    def __init__(self, link_url, link_token, query):
        self.client = Client(link_url, link_token)
        self.websites = None
        self.last_update: datetime = None
        self.query = query

    async def rebuild_websites(self):
        self.websites = Websites()
        bookmarks = await self.client.bookmarks.async_get_all(query=self.query)
        for b in bookmarks['results']:
            self.websites.add(Website(b['url'], 1))

    def get_random_website(self):
        return self.websites.get_random()

    async def on_get(self, request: aiohttp.web_request.Request):
        # context = request.match_info['redirect_context']
        if self.last_update is None or (datetime.now() - self.last_update).total_seconds() > 3600:
            await self.rebuild_websites()
        return web.HTTPFound(location=self.get_random_website().url)
