class NestSubscribeMessage:
    def __init__(self, cls, eventName):
        self.cls = cls
        self.eventName = eventName
        self.name = eventName

    def setup(self, cls, context):
        print(f"setup event {self.eventName}")
        socket = context.get('socket')
        socket.on(self.eventName, self._callbackWrapper(cls))
        # app.add_url_rule(
        #     self.path,
        #     methods=[self.method],
        #     view_func=self._callbackWrapper(controller),
        # )
