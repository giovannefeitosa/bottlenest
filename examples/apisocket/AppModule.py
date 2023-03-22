from bottlenest import Module
from bottlenest.transports.http import HttpTransport
from .api.ApiModule import ApiModule
from .ws.WsModule import WsModule


@Module(
    imports=[WsModule, ApiModule],
)
class AppModule:
    pass
