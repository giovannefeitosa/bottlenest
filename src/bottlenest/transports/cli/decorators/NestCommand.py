import inquirer
from bottlenest.metaClasses.NestProvider import NestProvider


class NestCommand(NestProvider):
    __name__ = 'NestCommand'

    def __init__(self, cls, commandName, description):
        self.cls = cls
        self.commandName = commandName
        self.description = description

    def eventName(self):
        # return NestRoute.__name__
        return 'todo'

    def setup(self, module, context):
        self._setup(module, context)
        self.provider.run(inquirer, context)
