from bottlenest.core.NestContainer import NestContainer
from bottlenest.core.NestLogger import NestLogger
import sys
import inquirer
import argparse


class CommandFactory:
    __commands__ = {}
    # __args__ = None
    # __currentCommand__ = None
    # __args__ = sys.argv[1:]
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
        # parse initial command line arguments
        # and set __currentCommand__
        rawCommandName = sys.argv[1]
        # CommandFactory.__module__ = module
        # CommandFactory.__container__ = container
        # run command
        CommandFactory.__runCommand(container, rawCommandName)

    @staticmethod
    def __runCommand(context, commandName):
        """This runCommand will be called from whithin NestCommand"""
        print("CommandFactory runCommand ", commandName)
        # parse command line arguments
        parser = argparse.ArgumentParser(
            prog="Program Name",
            description="Program Description",
            epilog="Program Epilog",
        )
        parser.add_argument("command", help="command to run")
        parser.add_argument("args", nargs=argparse.REMAINDER)
        commandArgs = parser.parse_args()
        # run command
        command = CommandFactory.__commands__[commandName]
        command.cls.run(command, context, commandArgs)

    @staticmethod
    def register(nestCommand):
        """This register will be called from whithin NestCommand"""
        print("CommandFactory register ", nestCommand.commandName)
        CommandFactory.__commands__[nestCommand.commandName] = nestCommand
