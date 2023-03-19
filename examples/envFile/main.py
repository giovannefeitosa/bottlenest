from bottlenest import NestFactory
from bottlenest.transports.http import HttpTransport
from examples.envFile.app.AppModule import AppModule


def bootstrap():
    app = NestFactory.createMicroservice(
        AppModule,
        transport=HttpTransport(port=4000),
    )

    return app.listen()


if __name__ == '__main__':
    bootstrap()
