class NestSubscribeMessage:
    def __init__(self, callback, eventName):
        self.eventName = eventName
        self.callback = callback

    def setup(self, cls, context):
        print(f"setup event {self.eventName}")
        socket = context.get('socket')
        socket.on(self.eventName, self._callbackWrapper(cls))
        # app.add_url_rule(
        #     self.path,
        #     methods=[self.method],
        #     view_func=self._callbackWrapper(controller),
        # )
