from bottlenest.common import Module
from .controller import AppController
from examples.helloworld.users.module import UsersModule


@Module(
    imports=[UsersModule],
    controllers=[AppController],
    # providers=[]
)
class AppModule:
    pass
