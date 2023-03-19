from bottlenest.common import Module
from .controller import UsersController
from .service import UsersService


@Module(
    # imports=[],
    controllers=[UsersController],
    providers=[UsersService],
)
class UsersModule:
    pass
