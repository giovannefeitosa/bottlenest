from bottlenest import NestFactory
from bottlenest.transports.websockets import WebsocketsTransport
from examples.websocketsServer.app.AppModule import AppModule


def main():
    app = NestFactory.createMicroservice(
        AppModule,
        transport=WebsocketsTransport(),
    )

    app.listen()


if __name__ == '__main__':
    main()
