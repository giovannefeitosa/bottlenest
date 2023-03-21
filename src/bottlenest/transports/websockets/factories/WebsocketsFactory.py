import eventlet
import socketio


class WebsocketsFactory:
    __gateways__: dict[str, dict] = {}

    @staticmethod
    def registerGateway(provider, providerContext) -> None:
        sio = socketio.Server()
        app = socketio.WSGIApp(sio)

        providerContext.set('sio', sio)
        providerContext.set('app', app)

        def _onConnect(sid, environ, auth):
            print(f"[NestWebsocketGateway] onConnect {sid}")
        sio.on('connect')(_onConnect)

        # add gateway
        WebsocketsFactory.__gateways__[provider.getName()] = {
            'provider': provider,
            'providerContext': providerContext,
            'sio': sio,
            'app': app,
        }

    @staticmethod
    def listen() -> None:
        print("Listen now!")
        # eventlet.wsgi.server(eventlet.listen(('', port)), app)
