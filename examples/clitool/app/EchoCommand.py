from bottlenest.transports.cli.decorators import Command
import inquirer


@Command(
    name="echo",
    description="Echoes back the given string",
)
class EchoCommand:
    def __init__(self, context):
        self.context = context

    def run(self, inquirer, args):
        print("EchoCommand.run: ", args)
