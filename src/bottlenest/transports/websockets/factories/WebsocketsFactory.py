import eventlet
import socketio
from ...http.HttpTransport import HttpTransport


class WebsocketsFactory:
    __gateways__: dict[str, dict] = {}
    __appContext__ = None

    @staticmethod
    def setAppContext(appContext) -> None:
        WebsocketsFactory.__appContext__ = appContext

    @staticmethod
    def registerGateway(provider, providerContext) -> None:
        sio = socketio.Server()
        httpTransport = HttpTransport(port=provider.port)
        httpTransport.setup(
            moduleContext=providerContext,
            appContext=WebsocketsFactory.__appContext__,
        )
        # app = socketio.WSGIApp(sio)

        providerContext.set('sio', sio)

        def _onConnect(sid, environ, auth):
            print(f"[NestWebsocketGateway] onConnect {sid}")
        sio.on('connect')(_onConnect)

        # add gateway
        WebsocketsFactory.__gateways__[provider.getName()] = {
            'provider': provider,
            'providerContext': providerContext,
            'sio': sio,
            'app': httpTransport.app,
            'port': provider.port,
        }

    @staticmethod
    def listen() -> None:
        print("Listen now!")

        def startServer(gateways):
            pool = eventlet.GreenPool(len(gateways))
            for gateway in gateways:
                port = gateway['port']
                sio = gateway['sio']
                app = socketio.WSGIApp(sio, gateway['app'])
                print(f"[listen] Starting server on port {port}")
                # pool.spawn(eventlet.wsgi.server,
                #           eventlet.listen(("", port)), app)
                # run pool.spawn with Flask (app) and eventlet.listen(("", port))
                pool.spawn(eventlet.wsgi.server,
                           eventlet.listen(("", port)), app)
            try:
                pool.waitall()
            except KeyboardInterrupt:
                pass

        startServer(WebsocketsFactory.__gateways__.values())
        # asyncio.run(asyncio.
        # eventlet.wsgi.server(eventlet.listen(('', port)), app)
