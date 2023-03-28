from bottlenest import NestFactory, Module
from bottlenest.transports.cli import CliTransport
from .commands.EchoCommand import EchoCommand
from .commands.TrainCommand import TrainCommand


@Module(
    providers=[EchoCommand, TrainCommand],
)
class AppModule:
    pass


def main():
    app = NestFactory.createMicroservice(
        AppModule,
        transport=CliTransport(),
    )

    app.listen()


if __name__ == '__main__':
    main()
