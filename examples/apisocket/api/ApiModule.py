from bottlenest import Module
from .ApiController import ApiController


@Module(
    controllers=[ApiController],
)
class ApiModule:
    pass
