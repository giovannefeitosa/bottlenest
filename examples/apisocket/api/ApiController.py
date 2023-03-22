from bottlenest.common import Controller, Get


@Controller()
class ApiController:
    @Get('/')
    def getHome(self, request):
        return 'Hello from ApiController!'
