from bottlenest import NestFactory, Module
from bottlenest.transports.cli import CliTransport
from bottlenest.transports.cli import CommandFactory
from .commands.ConnectCommand import ConnectCommand


@Module(
    providers=[ConnectCommand],
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
