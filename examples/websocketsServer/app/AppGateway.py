from bottlenest.transports.websockets.decorators import *


@WebSocketGateway(port=8765)
class AppController:
    # TODO: remove the need of an empty constructor
    def __init__(self, context):
        pass

    @SubscribeMessage('message')
    def handleMessageEvent(self, req):
        print("handleMessageEvent", req)
        return {
            'message': 'Hello from the server',
        }
