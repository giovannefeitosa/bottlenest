from bottlenest.transports.cli import Command, CommandArgument


@Command(
    name="build",
    description="Generates a build of the project",
)
class BuildCoreCommand:
    __name__ = 'BuildCoreCommand'

    def __init__(self, context):
        self.context = context

    def run(self, context, args):
        print(f"{self.__name__}.run:")
        print(args)
