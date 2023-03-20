from bottlenest.transports.websockets.decorators import *


@WebSocketGateway(port=8765)
class AppGateway:
    # TODO: remove the need of an empty constructor
    def __init__(self, context):
        pass

    @SubscribeMessage('message')
    def handleMessageEvent(self, req):
        print("[AppGateway] Server received message: ", req)
        return {
            'message': 'Hello from the server',
        }
