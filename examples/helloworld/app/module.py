from bottlenest.common import Module
from .controller import AppController
from .service import AppService


@Module(
    # imports=[UsersModule],
    providers=[AppService],
    controllers=[AppController],
)
class AppModule:
    pass
