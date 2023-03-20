from bottlenest.common import Module
import os
from examples.websocketsServer.app.AppGateway import AppGateway


@Module(
    providers=[AppGateway],
)
class AppModule:
    pass
