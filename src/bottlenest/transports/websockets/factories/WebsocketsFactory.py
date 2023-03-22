import eventlet
import socketio
from ...http.HttpTransport import HttpTransport


class WebsocketsFactory:
    __gateways__: dict[str, dict] = {}
    __appContext__ = None

    @staticmethod
    def setAppContext(appContext) -> None:
        print("---x-x--x--x-------------x-x--x--------------> setAppContext")
        if WebsocketsFactory.__appContext__ is None:
            WebsocketsFactory.__appContext__ = appContext

    @staticmethod
    def registerGateway(provider, providerContext) -> None:
        # add gateway
        sio = socketio.Server()
        providerContext.set('sio', sio)
        WebsocketsFactory.__gateways__[provider.getName()] = {
            'provider': provider,
            'providerContext': providerContext,
            'sio': sio,
            # 'app': httpTransport.app,
            # 'port': provider.port,
        }

    @staticmethod
    def setupGateway(pool, gatewayDict):
        sio = gatewayDict['sio']
        provider = gatewayDict['provider']
        providerContext = gatewayDict['providerContext']
        port = provider.port
        httpTransport = HttpTransport(port=provider.port)
        httpTransport.setupTransport(
            moduleContext=providerContext,
            appContext=WebsocketsFactory.__appContext__,
        )
        # app = socketio.WSGIApp(sio)

        def _onConnect(sid, environ, auth):
            print(f"[NestWebsocketGateway] onConnect {sid}")
        sio.on('connect')(_onConnect)

        app = socketio.WSGIApp(sio, httpTransport.app)
        print(f"[listen] Starting server on port {port}")
        # pool.spawn(eventlet.wsgi.server,
        #           eventlet.listen(("", port)), app)
        # run pool.spawn with Flask (app) and eventlet.listen(("", port))
        pool.spawn(eventlet.wsgi.server,
                   eventlet.listen(("", port)), app)

    @staticmethod
    def listen() -> None:
        print("Listen WEBSOCKETSSSSSS now!")

        def startServer(gateways):
            pool = eventlet.GreenPool(len(gateways))
            for gateway in gateways:
                WebsocketsFactory.setupGateway(pool, gateway)
            try:
                pool.waitall()
            except KeyboardInterrupt:
                pass

        startServer(WebsocketsFactory.__gateways__.values())
        # asyncio.run(asyncio.
        # eventlet.wsgi.server(eventlet.listen(('', port)), app)
