from bottlenest import NestFactory
from bottlenest.http import HttpTransport
from examples.helloworld.app.module import AppModule


def bootstrap():
    app = NestFactory.createMicroservice(
        AppModule,
        transport=HttpTransport(port=4000),
    )

    return app.listen()


if __name__ == '__main__':
    bootstrap()
