from .HttpTransport import HttpTransport


class NestHttpModule(object):
    def __init__(self, moduleClass, imports, controllers, providers):
        self.isEnabled = False
        # module default options
        self.imports = imports
        self.controllers = controllers
        self.providers = providers
        # module variables
        self.moduleName = moduleClass.__name__
        self.moduleInstance = moduleClass()
        print(f"NestModule init", [self.moduleName])

    def enableModule(self):
        print(f"NestHttpModule enableModule {self.moduleName}")
        self.isEnabled = True
        for module in self.imports:
            print(f"enableModule", [module.moduleName])
            module.enableModule()
        for provider in self.providers:
            print(f"enableProvider", [provider.getName()])
            provider.enableProvider()

    # called automatically
    # when you run NestFactory.createMicroservice
    # (inside NestApplicationContext)
    def setupModule(self, appContext, moduleContext, transport):
        print(f"NestHttpModule setupModule {self.moduleName}")
        if not self.isEnabled:
            raise Exception(f"Module not enabled: {self.moduleName}")
        # Calls NestInputTransport.setupTransport()
        # creates the Flask app
        self.__setupInputTransport(
            transport=transport,
            appContext=appContext,
            moduleContext=moduleContext,
        )
        # run setup on any imported modules
        for module in self.imports:
            module.setupModule(appContext, moduleContext, transport)
        # run setup on providers
        # these are the most important ones
        for provider in self.providers:
            provider.setupProvider(self, moduleContext)
        # run setup on controllers
        # this is only used for HttpTransport
        for controller in self.controllers:
            controller.setupProvider(self, moduleContext)

    def __setupInputTransport(self, transport, appContext, moduleContext):
        if transport is None:
            transport = HttpTransport()
        self.transport = transport
        moduleContext.set('transport', transport)
        transport.setupTransport(
            appContext=appContext, moduleContext=moduleContext)
        return transport

    # proxy static methods
    def __getattr__(self, name):
        return getattr(self.moduleInstance, name)

    def listen(self):
        print(f"NestHttpModule listen {self.moduleName}")
        if not self.isEnabled:
            raise Exception(f"Module not enabled: {self.moduleName}")

        def callback():
            # self.logger.log(f"NestApplicationContext stopped")
            print(f"NestApplicationContext stopped")
        # self.transport = self.moduleContext.get('transport')
        self.transport.listen(callback)
