def WebSocketGateway(port=80, namespace=None):
    def wrapper(gatewayClass):
        return NestWebSocketGateway(
            cls=gatewayClass,
            port=port,
            namespace=namespace,
        )
    return wrapper

# música boa
# https://www.youtube.com/watch?v=KCwk1qeh0gM


class NestWebSocketGateway:
    def __init__(self, cls, port=80, namespace=None):
        self.port = port
        self.namespace = namespace
        # self.name = self.namespace
        self.cls = cls
