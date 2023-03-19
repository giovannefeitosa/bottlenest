from bottlenest.common import Module
from examples.helloworld.users.module import UsersModule
from examples.helloworld.app.controller import AppController
from examples.helloworld.app.service import AppService


@Module(
    imports=[UsersModule],
    controllers=[AppController],
    providers=[AppService],
)
class AppModule:
    pass
