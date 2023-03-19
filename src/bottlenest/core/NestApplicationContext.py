from bottlenest.core.NestContainer import NestContainer
from bottlenest.core.NestLogger import NestLogger
from bottlenest.http.HttpTransport import HttpTransport


class NestApplicationContext:
    def __init__(self, module, transport):
        self.module = module
        self.logger = self.setupLogger()
        self.container = self.setupContainer()
        self.logger.setContext(self)
        self.transport = self.setupTransport(transport)
        # self.logger.log('NestApplicationContext initialized')
        # self.logger.log('NestApplicationContext module: ' +
        #                 str(self.module.name))
        # self.logger.log('NestApplicationContext options: ' + str(self.options))
        # self.logger.log('NestApplicationContext container: ' +
        #                str(self.container))
        # self.logger.log('NestApplicationContext logger: ' + str(self.logger))
        self.init()

    def init(self):
        self.app = self.transport
        # self.container.set('app', self.app)
        self.container.set('transport', self.transport)
        self.container.set('NestApplicationContext', self)
        self.container.set('NestContainer', self.container)
        self.module.initProviders(module=self.module, container=self.container)
        self.module.initControllers(
            module=self.module, container=self.container)

    def setupLogger(self):
        logger = NestLogger()
        return logger

    def setupContainer(self):
        container = NestContainer()
        container.set('module', self.module)
        container.set('logger', self.logger)
        return container

    def setupTransport(self, transport):
        if transport is None:
            transport = HttpTransport()
        transport.init(context=self.container)
        return transport

    def listen(self):
        self.logger.log('NestApplicationContext listen')

        def callback():
            self.logger.log(f"NestApplicationContext listening")
        self.transport.listen(callback)
        return self.app
