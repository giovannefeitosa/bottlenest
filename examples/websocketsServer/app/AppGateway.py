from bottlenest.transports.websockets.decorators import *


@WebSocketGateway(port=8765)
class AppGateway:

    @SubscribeMessage('message')
    def handleMessageEvent(self, data):
        print("[AppGateway] Server received message: ", data)
        return {
            'message': 'Hello from the server',
        }
