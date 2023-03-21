from bottlenest.common import Module
from ..users.module import UsersModule
from ..app.controller import AppController
from ..app.service import AppService


@Module(
    imports=[UsersModule],
    controllers=[AppController],
    providers=[AppService],
)
class AppModule:
    pass
