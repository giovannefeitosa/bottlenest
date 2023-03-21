class NestHttpModule(object):
    def __init__(self, moduleClass, imports, controllers, providers):
        # module default options
        self.imports = imports
        self.controllers = controllers
        self.providers = providers
        # module variables
        self.moduleName = moduleClass.__name__
        self.moduleInstance = moduleClass()
        print(f"NestModule init", [self.moduleName])

    # called automatically
    # when you run NestFactory.createMicroservice
    # (inside NestApplicationContext)
    def setup(self, moduleContext):
        # run setup on providers
        # these are the most important ones
        for provider in self.providers:
            provider.setup(self, moduleContext)
        # run setup on controllers
        # this is only used for HttpTransport
        for controller in self.controllers:
            controller.setup(self, moduleContext)
        # run setup on any imported modules
        # ? maybe ths modules need to get something like moduleContext.submodule()
        for module in self.imports:
            module.setup(moduleContext)

    # proxy static methods
    def __getattr__(self, name):
        return getattr(self.moduleInstance, name)
