from flask import request
from functools import wraps


class NestController:
    def __init__(self, cls):
        self.name = cls.__name__
        self.cls = cls

    def initController(self, module, appContext):
        self.module = module
        self.appContext = appContext
        self.controllerContext = NestControllerContext(self)
        self.controller = self.cls(self.controllerContext)
        routeNames = [name for name in dir(self.controller) if type(
            getattr(self.controller, name)).__name__ == 'NestRoute']
        for routeName in routeNames:
            route = getattr(self.controller, routeName)
            route.initRoute(self.controller, appContext)


# this context is given to the controller
class NestControllerContext:
    def __init__(self, nestController):
        self.nestController = nestController

    def get(self, key):
        getName = f"{self.nestController.module.name}.{key}"
        return self.nestController.appContext.get(getName)

    def inject(self, injectable):
        key = injectable.__name__
        getName = f"{self.nestController.module.name}.{key}"
        provider = self.nestController.appContext.get(getName)
        if provider is None:
            raise Exception(f"Provider not found: {getName}")
        return provider.instance
