from bottlenest.common import Controller, Get


@Controller()
class AppController:
    @Get('/')
    def getHello(self, req):
        return self.appService.getHello()

    @Get('/hello/:name')
    def getHello2(self, req):
        return f"Hello {req.params.name}!"
