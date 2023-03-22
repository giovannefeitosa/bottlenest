from bottlenest import NestFactory
from bottlenest.transports.http import HttpTransport
from .AppModule import AppModule


def main():
    app = NestFactory.createMicroservice(
        AppModule,
        transport=HttpTransport(port=8012),
    )

    app.listen()


if __name__ == '__main__':
    main()
