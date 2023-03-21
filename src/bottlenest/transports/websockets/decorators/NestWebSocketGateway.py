from bottlenest.metaClasses.NestProvider import NestProvider
from .NestSubscribeMessage import NestSubscribeMessage
from ..factories.WebsocketsFactory import WebsocketsFactory

servers = []


class NestWebSocketGateway(NestProvider):
    __name__ = 'NestWebSocketGateway'

    def __init__(self, cls, port=4001, namespace=None):
        self.cls = cls
        self.port = port
        self.namespace = namespace

    def getName(self):
        return self.cls.__name__

    def eventName(self):
        return NestSubscribeMessage.__name__

    # called from whithin the module's setup
    def setup(self, module, context):
        self.module = module
        self.context = context
        # get sio from WebsocketsTransport
        WebsocketsFactory.registerGateway(self, context)
        self._setup(module, context)
