import eventlet
import socketio
from bottlenest.core.NestProvider import NestProvider

servers = []


class NestWebSocketGateway(NestProvider):
    __name__ = 'NestWebSocketGateway'

    def __init__(self, gatewayClass, moduleContext, port=4001, namespace=None):
        self.port = port
        self.namespace = namespace
        self.providerClass = gatewayClass
        self.providerName = gatewayClass.__name__
        self.moduleContext = moduleContext
        # TODO: send moduleContext to gatewayClass(moduleContext)
        # conditionally
        try:
            self.provider = self.providerClass()
        except TypeError:
            self.provider = self.providerClass(moduleContext)

    # def getName(self):
    #     return self.providerClass.__name__

    # def eventName(self):
    #     return NestSubscribeMessage.__name__

    # called from whithin the module's setup
    # def setupProvider(self, module, context):
    #     print(f"NestSocketGateway setupProvider {self.providerName}")
    #     self.module = module
    #     self.context = context
    #     # get sio from WebsocketsTransport
    #     # WebsocketsFactory.registerGateway(self, context)
    #     self._setupProvider(module, context)

    def listen(self, pool):
        print(f"NestSocketGateway listen {self.providerName}")

        def _startWebsocketsServer():
            print("starting websockets server")
            sio = socketio.Server()
            app = socketio.WSGIApp(sio)
            eventlet.wsgi.server(eventlet.listen(('', self.port)), app)
        pool.spawn(_startWebsocketsServer)
