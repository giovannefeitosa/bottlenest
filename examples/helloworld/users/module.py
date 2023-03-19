from bottlenest.common import Module
from .controller import UsersController


@Module(
    # imports=[],
    controllers=[UsersController],
    # providers=[]
)
class UsersModule:
    pass
