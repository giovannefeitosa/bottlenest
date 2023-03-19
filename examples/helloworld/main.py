from bottlenest import *
from examples.helloworld.app.module import AppModule

port = 4000


def bootstrap():
    app = NestFactory.createMicroservice(AppModule, {
        'transport': Transport.HTTP,
    })

    return app.listen(port)


if __name__ == '__main__':
    bootstrap().run(port=port)
