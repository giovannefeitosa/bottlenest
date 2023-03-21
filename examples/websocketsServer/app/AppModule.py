from bottlenest.common import Module
import os
from examples.websocketsServer.app.AppGateway import AppGateway
from examples.websocketsServer.app.EchoGateway import EchoGateway


@Module(
    providers=[AppGateway, EchoGateway],
)
class AppModule:
    pass
