from flask import request
from functools import wraps


def Controller():
    def wrapper(controllerClass):
        return NestController(
            controllerClass=controllerClass,
        )
    return wrapper


class NestController:
    def __init__(self, controllerClass):
        self.name = controllerClass.__name__
        self.controllerClass = controllerClass
        # print("-----------------xxx> ", self.controller())

    def initController(self, module, appContext):
        self.module = module
        self.appContext = appContext
        self.controllerContext = NestControllerContext(self)
        self.controller = self.controllerClass(self.controllerContext)
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


def Get(path):
    print(f"get defined {path}")

    def wrapper(func):
        return NestRoute(path=path, method='GET', callback=func)
    return wrapper


def Post(path):
    print(f"post defined {path}")

    def wrapper(func):
        return NestRoute(path=path, method='POST', callback=func)
    return wrapper


class NestRoute:
    def __init__(self, path, method, callback):
        self.callback = callback
        self.path = self.nestjsToFlaskPath(path)
        self.method = method

    def initRoute(self, controller, context):
        print(f"init route {self.path}")
        app = context.get('app')
        app.add_url_rule(
            self.path,
            methods=[self.method],
            view_func=self.callbackWrapper(controller),
        )

    def callbackWrapper(self, controller):
        @wraps(self.callback)
        def wrapped(*args, **kwargs):
            return self.callback(controller, NestRequest(request))
            # return self.callback(context)
        return wrapped

    # Flask routing is different than NestJS routing
    def nestjsToFlaskPath(self, path: str) -> str:
        result = ''
        parts = path.split('/')
        for part in parts:
            if part.startswith(':'):
                result += '/<' + part[1:] + '>'
            else:
                result += '/' + part
        return result[1:]


class NestRequest:
    def __init__(self, request):
        self.request = request
        self.params = NestRequestParams(self.request)
        self.query = {}
        self.body = request.get_json(silent=True, force=True)
        self.headers = {}

        if self.body is None:
            self.body = {}


class NestRequestParams(object):
    def __init__(self, request):
        super(NestRequestParams, self).__init__()
        self.request = request

    def __getattribute__(self, __name: str):
        if __name == 'request':
            return super(NestRequestParams, self).__getattribute__(__name)
        else:
            return self.request.view_args[__name]
            # return self.request.args.get(__name, type=str)
