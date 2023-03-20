from flask import request
from functools import wraps
from bottlenest.metaClasses.NestProvider import NestProvider

# TODO: add support for route prefix


class NestController(metaclass=NestProvider):
    def __init__(self, cls):
        self.cls = cls
        self.name = cls.__name__

    def setup(self, module, context):
        # TODO: Essa função deve setar o socket no serviceContext
        # TODO: para dentro do cls ser possivel acessar a CONEXÃO ATUAL
        # TODO: -------------
        # TODO: Mas aí pensei de antes, fazer uma OOP decente
        # NestController e NestWebSocketGateway
        # self.module = module
        # self.context = context
        # self.serviceContext = NestControllerContext(self)
        # self.provider = self.cls(self.serviceContext)
        # eventNames = [name for name in dir(self.provider) if type(
        #     getattr(self.provider, name)).__name__ == 'NestRoute']
        # for eventName in eventNames:
        #     service = getattr(self.provider, eventName)
        #     service.setup(self.provider, context)
        return NestControllerContext(module, context)


# this context is given to the controller
class NestControllerContext:
    def __init__(self, provider):
        self.provider = provider

    #! The following get and inject functions are duplicated
    #! websockets.decorators.NestWebSocketGateway
    #! http.decorators.NestController

    def get(self, key):
        getName = f"{self.provider.module.name}.{key}"
        return self.provider.context.get(getName)

    def inject(self, injectable):
        key = injectable.__name__
        getName = f"{self.provider.module.name}.{key}"
        provider = self.provider.context.get(getName)
        if provider is None:
            raise Exception(f"Provider not found: {getName}")
        return provider.instance
