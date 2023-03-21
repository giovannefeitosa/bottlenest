from bottlenest.transports.websockets.decorators import *


@WebSocketGateway(port=8766)
class EchoGateway:
    # TODO: remove empty constructor
    def __init__(self, context):
        pass

    @SubscribeMessage('message')
    def handleMessageEvent(self, data):
        print("[AppGateway] Server received message: ", data)
        return {
            'message_from_echo_gateway': 'Hello from the EchoGateway',
        }
