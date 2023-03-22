from bottlenest.transports.websockets.decorators import *


@WebSocketGateway(port=8013)
class WsGateway:
    @SubscribeMessage('message')
    def handleMessageEvent(self, data):
        print("[WsGateway] Server received message: ", data)
        return {
            'message': 'Hello from the server',
        }
