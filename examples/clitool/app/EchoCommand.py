from bottlenest.transports.cli.decorators import Command
import re


@Command(
    name="echo",
    description="Echoes back the given string",
)
class EchoCommand:
    def __init__(self, context):
        self.context = context

    def run(self, context, args):
        print("EchoCommand.run: ", args.args)
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
