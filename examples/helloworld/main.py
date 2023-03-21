from bottlenest import NestFactory
from bottlenest.transports.http import HttpTransport
from .app.module import AppModule


def main():
    app = NestFactory.createMicroservice(
        AppModule,
        transport=HttpTransport(port=4000),
    )

    app.listen()


if __name__ == '__main__':
    main()
