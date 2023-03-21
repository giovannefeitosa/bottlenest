from bottlenest.common import Module
from bottlenest.transports.cli import CommandFactory
from .commands.ConnectCommand import ConnectCommand


@Module(
    providers=[ConnectCommand],
)
class AppModule:
    pass


def main():
    CommandFactory.run(AppModule)


if __name__ == '__main__':
    main()
