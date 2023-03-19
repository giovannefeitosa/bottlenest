class NestHttpModule(object):
    def __init__(self, moduleClass, imports, controllers, providers):
        self.name = moduleClass.__name__
        self.imports = imports
        self.controllers = controllers
        # self.moduleClass = moduleClass
        # self.moduleInstance = moduleClass()
        self.name = moduleClass.__name__
        print("moduleClass", moduleClass)
        self.providers = providers
        self.module = moduleClass()
        print(f"NestModule init", [self.name])

    def init(self, context):
        self.initProviders(context)
        self.initControllers(context)

    def initProviders(self, context):
        for imp in self.imports:
            imp.initProviders(context)
        for provider in self.providers:
            provider.initProvider(self, context)

    def initControllers(self, context):
        for imp in self.imports:
            imp.initControllers(context)
        for cont in self.controllers:
            cont.initController(self, context)

    # proxy static methods
    def __getattr__(self, name):
        return getattr(self.module, name)
