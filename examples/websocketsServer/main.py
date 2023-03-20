from bottlenest import NestFactory
from bottlenest.transports.http import HttpTransport
from examples.websocketsServer.app.AppModule import AppModule


def bootstrap():
    app = NestFactory.createMicroservice(
        AppModule,
        transport=HttpTransport(port=4000),
    )

    return app.listen()


if __name__ == '__main__':
    bootstrap()
