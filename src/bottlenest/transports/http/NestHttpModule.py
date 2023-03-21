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

    def setup(self, context):
        # run setup on providers
        # these are the most important ones
        for provider in self.providers:
            provider.setup(self, context)
        # run setup on controllers
        # this is only used for HttpTransport
        for controller in self.controllers:
            controller.setup(self, context)
        # run setup on any imported modules
        for module in self.imports:
            module.setup(context)

    # proxy static methods
    def __getattr__(self, name):
        return getattr(self.module, name)
