from bottlenest.core.NestContainer import NestContainer
from bottlenest.core.NestLogger import NestLogger
import sys
import inquirer


class CommandFactory:
    __commands__ = {}
    # ["echo", "<your_message_here>"]
    __args__ = sys.argv[1:]
    # __module__ = None
    # __container__ = None

    @staticmethod
    def run(module):
        """This run will be called from whithin main.py"""
        # initial setup
        logger = NestLogger()
        container = NestContainer()
        container.set('module', module)
        container.set('logger', logger)
        container.set('inquirer', inquirer)
        # load module
        module.setup(container)
        # CommandFactory.__module__ = module
        # CommandFactory.__container__ = container
        # run command
        # commandName =
        CommandFactory.runCommand(container, CommandFactory.__args__[
                                  0], CommandFactory.__args__[1:])

    @staticmethod
    def runCommand(context, commandName, commandArgs):
        """This runCommand will be called from whithin NestCommand"""
        print("CommandFactory runCommand ", commandName, commandArgs)
        command = CommandFactory.__commands__[commandName]
        command.cls.run(command, context, commandArgs)

    @staticmethod
    def register(nestCommand):
        """This register will be called from whithin NestCommand"""
        print("CommandFactory register ", nestCommand.commandName)
        CommandFactory.__commands__[nestCommand.commandName] = nestCommand
