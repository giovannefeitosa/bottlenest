from bottlenest.core.NestProvider import NestProvider
from .NestRoute import NestRoute

# TODO: add support for route prefix


class NestController(NestProvider):
    __name__ = 'NestController'

    def __init__(self, providerClass, moduleContext):
        print(f"NestController init")
        self.moduleContext = moduleContext
        # TODO: I should pass moduleContext here (conditionally)
        self.provider = providerClass()
        # moduleContext.getOrCreateProvider(self.__name__, self)
        # transport = moduleContext.getOrCreateTransport(self.transport)
        # instance = providerClass(moduleContext)
        # for route in self.routes:
        #     route = NestRoute(route)
        #     transport.addRoute(route)

    def _getRoutes(self, provider):
        for key in dir(provider):
            if type(getattr(provider, key)).__name__ == 'NestRoute':
                yield getattr(provider, key)

    def _getEventNames(self):
        eventClassName = self.eventName()
        eventNames = dir(self.classInstance)
        eventNames = [name for name in eventNames if type(
            getattr(self.classInstance, name)).__name__ == eventClassName]
        return eventNames

    def listen(self, pool):
        print(f"NestController listen")
        flaskApp = self.moduleContext.getDefaultHttpTransport().getFlaskApp()
        for route in self._getRoutes(self.provider):
            route.setupRoute(self.provider, flaskApp)
        # transport = self.moduleContext.getOrCreateTransport(self.transport)
        # transport.listen(pool, self.callback)
