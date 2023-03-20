from bottlenest import NestFactory
from bottlenest.transports.cli import CliTransport
from examples.clitool.app.AppModule import AppModule


def bootstrap():
    app = NestFactory.createMicroservice(
        AppModule,
        transport=CliTransport(),
    )

    app.listen()


if __name__ == '__main__':
    bootstrap()
