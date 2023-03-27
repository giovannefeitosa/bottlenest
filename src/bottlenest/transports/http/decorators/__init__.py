# from ..NestHttpModule import NestHttpModule
from bottlenest.core.NestModule import NestModule
from .NestController import NestController
from .NestRoute import NestRoute


def Module(controllers=[], providers=[], imports=[]):
    def wrapper(moduleClass):
        def inner(appContext):
            return NestModule(
                moduleClass=moduleClass,
                imports=imports,
                providers=providers,
                controllers=controllers,
                appContext=appContext,
            )
        return inner
    return wrapper


def Controller():
    def wrapper(controllerClass):
        def inner(moduleContext):
            return NestController(
                controllerClass,
                moduleContext,
            )
        return inner
    return wrapper


def Get(path):
    print(f"get defined {path}")

    def wrapper(func):
        def inner(TODO):
            return NestRoute(
                callback=func,
                path=path,
                method='GET',
            )
    return wrapper


def Post(path):
    print(f"post defined {path}")

    def wrapper(func):
        def inner(TODO):
            return NestRoute(
                callback=func,
                path=path,
                method='POST',
            )
    return wrapper


def Put(path):
    print(f"put defined {path}")

    def wrapper(func):
        def inner(TODO):
            return NestRoute(
                callback=func,
                path=path,
                method='PUT',
            )
    return wrapper


def Delete(path):
    print(f"delete defined {path}")

    def wrapper(func):
        def inner(TODO):
            return NestRoute(
                callback=func,
                path=path,
                method='DELETE',
            )
    return wrapper


def Patch(path):
    print(f"patch defined {path}")

    def wrapper(func):
        def inner(TODO):
            return NestRoute(
                callback=func,
                path=path,
                method='PATCH',
            )
    return wrapper
