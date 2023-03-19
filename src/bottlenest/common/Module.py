def Module(controllers=[], imports=[], providers=[]):
    def wrapper(moduleClass):
        return NestModule(
            moduleClass=moduleClass,
            imports=imports,
            controllers=controllers,
            providers=providers,
        )
    return wrapper


class NestModule(object):
    def __init__(self, moduleClass, imports, controllers, providers):
        self.name = moduleClass.__name__
        self.imports = imports
        self.controllers = controllers
        # self.moduleClass = moduleClass
        # self.moduleInstance = moduleClass()
        self.name = moduleClass.__name__
        self.providers = providers
        self.module = moduleClass()
        print(f"NestModule init", [self.name])

    def initProviders(self, module, container):
        for imp in self.imports:
            imp.initProviders(imp, container)
        for provider in self.providers:
            provider.initProvider(module, container)

    def initControllers(self, module, container):
        for imp in self.imports:
            imp.initControllers(imp, container)
        for cont in self.controllers:
            cont.initController(module, container)

    # proxy static methods
    def __getattr__(self, name):
        return getattr(self.module, name)
