from bottlenest.core.NestContainer import NestContainer
from bottlenest.core.NestLogger import NestLogger


class CommandFactory:
    __commands__ = []
    __module__ = None
    __container__ = None

    @staticmethod
    def run(module):
        print("CommandFactory run")
        logger = NestLogger()
        container = NestContainer()
        container.set('module', module)
        container.set('logger', logger)
        CommandFactory.__module__ = module
        CommandFactory.__container__ = container
        module.setup(container)

    @staticmethod
    def register(cls, name, description):
        print("CommandFactory register", cls)
