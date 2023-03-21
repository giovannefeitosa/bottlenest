from bottlenest.common import Module
from bottlenest.transports.cli import CommandFactory
from examples.clitool.commands.EchoCommand import EchoCommand
from examples.clitool.commands.TrainCommand import TrainCommand


@Module(
    providers=[EchoCommand, TrainCommand],
)
class AppModule:
    pass


if __name__ == '__main__':
    CommandFactory.run(AppModule)
