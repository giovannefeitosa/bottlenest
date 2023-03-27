from bottlenest.core.NestProvider import NestProvider
from .NestRoute import NestRoute

# TODO: add support for route prefix


class NestController(NestProvider):
    __name__ = 'NestController'

    def __init__(self, providerClass, moduleContext):
        print(f"NestController init")
        # moduleContext.getOrCreateProvider(self.__name__, self)
        # transport = moduleContext.getOrCreateTransport(self.transport)
        # instance = providerClass(moduleContext)
        # for route in self.routes:
        #     route = NestRoute(route)
        #     transport.addRoute(route)
        pass
