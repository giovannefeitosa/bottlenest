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
            'port': provider.port,
        }

    @staticmethod
    def listen() -> None:
        print("Listen now!")

        def startServer(gateways):
            pool = eventlet.GreenPool(len(gateways))
            for gateway in gateways:
                port = gateway['port']
                app = gateway['app']
                print(f"[listen] Starting server on port {port}")
                pool.spawn(eventlet.wsgi.server,
                           eventlet.listen(("", port)), app)
            pool.waitall()

        startServer(WebsocketsFactory.__gateways__.values())
        # asyncio.run(asyncio.
        # eventlet.wsgi.server(eventlet.listen(('', port)), app)
