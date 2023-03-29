from bottlenest.common import Module
from .AppController import AppController


@Module(
    # imports=[UsersModule],
    providers=[],
    controllers=[AppController],
)
class AppModule:
    pass
