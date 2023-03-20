from bottlenest import NestFactory
from bottlenest.transports.websockets import WebsocketsTransport
from examples.websocketsServer.app.AppModule import AppModule


def bootstrap():
    app = NestFactory.createMicroservice(
        AppModule,
        transport=WebsocketsTransport(),
    )

    return app.listen()


if __name__ == '__main__':
    bootstrap()
