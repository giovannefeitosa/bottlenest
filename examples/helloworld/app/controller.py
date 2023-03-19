from bottlenest.common import Controller, Get, Param


@Controller()
class AppController:
    @Get('/')
    def getHello(req):
        return 'Hello World!'

    @Get('/hello/:name')
    def getHello2(req):
        return f"Hello {req.params.name}!"
