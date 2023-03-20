import inquirer
from bottlenest.metaClasses.NestProvider import NestProvider
from bottlenest.transports.cli.CommandFactory import CommandFactory
import sys


class NestCommand(NestProvider):
    __name__ = 'NestCommand'

    def __init__(self, cls, commandName, description):
        self.cls = cls
        self.commandName = commandName
        self.description = description
        CommandFactory.register(self)

    def eventName(self):
        # return NestRoute.__name__
        return self.commandName

    def setup(self, module, context):
        self._setup(module, context)
        # args = sys.argv[1:]
        # self.provider.run(inquirer, args)
