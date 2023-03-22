from bottlenest import Module
from .WsGateway import WsGateway


@Module(
    providers=[WsGateway],
)
class WsModule:
    pass
