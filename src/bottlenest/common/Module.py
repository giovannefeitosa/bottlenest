def Module(controllers=[], imports=[], providers=[]):
    def wrapper(moduleClass):
        return NestModule(
            moduleClass=moduleClass,
            imports=imports,
            controllers=controllers,
            providers=providers,
        )
    return wrapper


class NestModule:
    def __init__(self, moduleClass, imports, controllers, providers):
        self.name = moduleClass.__name__
        self.imports = imports
        self.controllers = controllers
        # self.moduleClass = moduleClass
        # self.moduleInstance = moduleClass()
        self.name = moduleClass.__name__
        self.providers = providers
        print(f"NestModule init", [self.name])

    def initProviders(self, module=None, container=None):
        theModule = module if module else self
        for imp in self.imports:
            imp.initProviders(theModule, container)
        for provider in self.providers:
            provider.initProvider(theModule, container)

    def initControllers(self, container):
        for imp in self.imports:
            imp.initControllers(container)
        for cont in self.controllers:
            cont.initController(container)
