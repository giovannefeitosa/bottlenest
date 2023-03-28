from bottlenest.transports.cli import Command, CommandArgument
import re


@Command(
    name="train",
    description="Simulates a train command (machine learning)",
)
class TrainCommand:
    __name__ = 'TrainCommand'

    def __init__(self, context):
        self.context = context

    def run(self, context, args):
        data = args.data
        print(f"TrainCommand.run:")
        print(f"  data: {data}")
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
        name="--data",
        dest="data",
        help="The data file",
        type=str,
        optional=True,
    )
    def dataArg(self, value):
        return value

    @CommandArgument(
        name="--output",
        dest="output",
        help="The output file",
        type=str,
        default="output.txt",
        optional=True,
    )
    def outputArg(self, value):
        return value
