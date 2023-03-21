from .factories.WebsocketsFactory import WebsocketsFactory


class WebsocketsTransport:
    # called by user, passing any options
    def __init__(self):
        pass

    def setup(self, context):
        self.context = context
        self.module = self.context.get('module')
        self.logger = self.context.get('logger')

    def listen(self, callback):
        WebsocketsFactory.listen()
        callback()

    # def listen(self, callback):
    #     # TODO: review this port to allow multiple ports
    #     port = self.context.get('port')
    #     app = self.context.get('app')
    #     eventlet.wsgi.server(eventlet.listen(('', port)), app)
    #     callback()
