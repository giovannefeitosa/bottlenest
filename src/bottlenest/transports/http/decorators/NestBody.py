from bottlenest.core.NestMethodDecorator import NestMethodDecorator


class NestBody(NestMethodDecorator):
    __name__ = 'NestBody'

    def __init__(self, callback, dto):
        self.callback = callback
        self.dto = dto

    def setupMethodDecorator(self, moduleContext, dto):
        print("[NestBody] setupMethodDecorator", moduleContext, dto)
        self.callback(moduleContext, {})
