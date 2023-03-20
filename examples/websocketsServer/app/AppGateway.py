from bottlenest.transports.websockets.decorators import *


@WebSocketGateway(port=8765)
class AppGateway:
    # TODO: remove empty constructor
    def __init__(self, context):
        pass

    @SubscribeMessage('message')
    def handleMessageEvent(self, data):
        print("[AppGateway] Server received message: ", data)
        return {
            'message': 'Hello from the server',
        }
