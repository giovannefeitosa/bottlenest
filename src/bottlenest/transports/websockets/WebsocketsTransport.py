import asyncio
from websockets import connect


class WebsocketsTransport:
    def __init__(self, url="ws://localhost:8765"):
        self.url = url

    def setup(self, context):
        self.context = context

    def listen(self, callback):
        self.ws = connect(self.url)
        self.context.set('ws', self.ws)
        asyncio.run(self.startServer)
        callback()

    async def startServer(self):
        await self.ws.recv()
