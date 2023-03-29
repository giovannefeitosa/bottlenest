from flask import request
from functools import wraps
from bottlenest.core.NestMethodDecorator import NestMethodDecorator


class NestRoute(NestMethodDecorator):
    __name__ = 'NestRoute'

    def __init__(self, path, method, callback):
        self.path = path
        self.method = method
        self.callback = callback

    def setupMethodDecorator(self, provider, flaskApp):
        print(f"[NestRoute] setupMethodDecorator {self.method} {self.path}")
        flaskApp.add_url_rule(
            self._nestjsToFlaskPath(self.path),
            methods=[self.method],
            view_func=self._callbackWrapper(provider, self.callback),
        )

    def _callbackWrapper(self, provider, callback):
        @wraps(callback)
        def wrapped(*args, **kwargs):
            return callback(provider, NestRequest(request))
            # return self.callback(context)
        return wrapped

    # Flask routing is different than NestJS routing
    def _nestjsToFlaskPath(self, path: str) -> str:
        result = ''
        parts = path.split('/')
        for part in parts:
            if part.startswith(':'):
                result += '/<' + part[1:] + '>'
            else:
                result += '/' + part
        return result[1:]

##################################################################


class NestRequest:
    __name__ = 'NestRequest'

    def __init__(self, request):
        self.request = request
        self.params = NestRequestParams(self.request)
        self.query = {}
        self.body = request.get_json(silent=True, force=True)
        self.headers = {}

        if self.body is None:
            self.body = {}


class NestRequestParams(object):
    __name__ = 'NestRequestParams'

    def __init__(self, request):
        super(NestRequestParams, self).__init__()
        self.request = request

    def __getattribute__(self, __name: str):
        if __name == 'request':
            return super(NestRequestParams, self).__getattribute__(__name)
        else:
            return self.request.view_args[__name]
            # return self.request.args.get(__name, type=str)
