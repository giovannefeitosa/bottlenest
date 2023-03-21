from bottlenest.transports.cli import Command, CommandArgument
import re


@Command(
    name="echo",
    description="Echoes back the given string",
)
class EchoCommand:
    def __init__(self, context):
        self.context = context

    def run(self, context, args):
        print(f"{self.__name__}.run: ", args.command, args.messageArg)
        print(args)
        # ---
        # Example from official docs
        # questions = [
        #     inquirer.List('size',
        #                   message="What size do you need?",
        #                   choices=['Jumbo', 'Large', 'Standard',
        #                            'Medium', 'Small', 'Micro'],
        #                   ),
        # ]
        # answers = inquirer.prompt(questions)
        # print("")
        # print("Answers:")
        # print(answers)
        # ---

    @CommandArgument(
        name="messageArg",
        help="The message to echo",
        type=str,
    )
    def messageArg(self, value):
        return value
