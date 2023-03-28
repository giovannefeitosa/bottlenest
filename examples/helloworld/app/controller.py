from bottlenest.common import Controller, Get
from .service import AppService


@Controller()
class AppController:
    appService: AppService

    @Get('/')
    def getHello(self, req):
        return self.appService.getHello()

    @Get('/hello/:name')
    def getHello2(self, req):
        return f"Hello {req.params.name}!"
