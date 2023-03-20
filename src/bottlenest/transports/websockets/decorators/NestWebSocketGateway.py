from bottlenest.metaClasses.NestProvider import NestProvider


class NestWebSocketGateway(metaclass=NestProvider):
    def __init__(self, cls):
        self.cls = cls
        self.name = cls.__name__
        # self.port = port
        # self.namespace = namespace

    def setup(self, module, context):
        self.module = module
        self.context = context
        self.serviceContext = NestWebSocketGatewayContext(self)
        self.provider = self.cls(self.serviceContext)
        eventNames = [name for name in dir(self.provider) if type(
            getattr(self.provider, name)).__name__ == 'NestSubscribeMessage']
        for name in eventNames:
            route = getattr(self.provider, name)
            route.setup(self.provider, context)


# this context is given to the gateway
class NestWebSocketGatewayContext:
    def __init__(self, provider):
        self.provider = provider

    #! The following get and inject functions are duplicated
    #! websockets.decorators.NestWebSocketGateway
    #! http.decorators.NestController

    def get(self, key):
        getName = f"{self.provider.module.name}.{key}"
        return self.provider.appContext.get(getName)

    def inject(self, injectable):
        key = injectable.__name__
        getName = f"{self.provider.module.name}.{key}"
        provider = self.provider.appContext.get(getName)
        if provider is None:
            raise Exception(f"Provider not found: {getName}")
        return provider.instance
