import eventlet
import socketio
from bottlenest.metaClasses.NestProvider import NestProvider
from bottlenest.transports.websockets.decorators.NestSubscribeMessage import NestSubscribeMessage


class NestWebSocketGateway(NestProvider):
    __name__ = 'NestWebSocketGateway'

    def __init__(self, cls, port=4001, namespace=None):
        self.cls = cls
        self.port = port
        self.namespace = namespace
        super().__init__(cls)

    def eventName(self):
        return NestSubscribeMessage.__name__

    def setup(self, module, context):
        self.module = module
        self.context = context

        async def _run():
            async def _server(websocket):
                self.context.set('socket', websocket)
                websocket.emit('message', 'Hello from the server')
            async with websockets.serve(_server, "localhost", self.port):
                await asyncio.Future()  # run forever
        asyncio.run(_run())
        super(NestProvider, self).setup(self.module, self.context)
