import socket

import aiohttp
import asyncio
import aiofiles


class Downloader:
    def __init__(self, loop):
        self.loop = loop

    async def save(self, data, post):
        async with aiofiles.open("{}.jpg".format(post['node']['id']), 'wb', loop=self.loop) as f:
            return await f.write(data)

    async def download(self, session, post):
        with aiohttp.Timeout(10):
            async with session.get(post['node']['images']['standard_resolution']['url']) as response:
                if response.status != 200:
                    raise Exception('Bad status code {}'.format(response.status))
                return await response.read()

    async def process(self, session, post):
        image_data = await self.download(session, post)
        return await self.save(image_data, post)

    async def create_tasks(self, posts):
        async with aiohttp.ClientSession(loop=self.loop,
                                         connector=aiohttp.TCPConnector(family=socket.AF_INET)) as session:
            tasks = [self.process(session, post) for post in posts]
            await asyncio.gather(*tasks, return_exceptions=True)

    def start_processing(self, posts):
        self.loop.run_until_complete(self.create_tasks(posts))
