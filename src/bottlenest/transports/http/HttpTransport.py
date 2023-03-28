from flask import Flask
from .errors import HttpError
import traceback
import eventlet
from eventlet import wsgi
from bottlenest.core.NestTransport import NestTransport


class HttpTransport(NestTransport):
    def __init__(self, port=3500):
        self.port = port
        self.app = None

    def getFlaskApp(self):
        return self.app

    def getTransportKey(self):
        return 'HttpTransport', f"{self.port}"

    # called automatically
    # when you run NestFactory.createMicroservice
    # (inside NestApplicationContext)
    def setupTransport(self, appContext, moduleContext):
        print("HttpTransport setupTransport")
        self.appContext = appContext
        self.moduleContext = moduleContext
        # self.logger = self.moduleContext.get('logger')
        appName = f"http-{self.port}"
        print(f"Starting http server on port {self.port}")
        self.app = Flask(appName)
        # self.appContext.set('app', self.app)
        # if isinstance(self.moduleContext.get('transport'), HttpTransport):
        #     print("---------------------> setting up error handlers")
        #     self.setupErrorHandlers()

    # handle any http errors
    def setupErrorHandlers(self):
        @self.app.errorhandler(Exception)
        def defaultErrorHandler(e):
            print(
                'NestApplicationContext handle_exception', e, traceback.format_exc())
            # check if e is an instance of HttpError
            if isinstance(e, HttpError):
                return e.toDict(), e.statusCode
            return {"messages": [e.__str__()]}, 500

    # start listening for requests
    # this is called
    def listen(self, pool):
        print(f"HttpTransport listen port={self.port}")
        # self.app.run(port=self.port, debug=False)
        # spawned = pool.spawn(self.app.run, port=self.port, debug=False)

        def _startHttpServer(port, app):
            wsgi.server(eventlet.listen(('0.0.0.0', port)), app)
        pool.spawn(_startHttpServer, self.port, self.app)
        # return self.app.run(port=self.port, debug=False)
