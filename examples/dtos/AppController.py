from bottlenest.common import Controller, Get, Post, Body
from .dtos.CatDto import CatDto


@Controller()
class AppController:
    @Get('/')
    def getHello(self, req):
        return "Make a post for this url!"

    @Post('/')
    @Body(CatDto)
    def getHello2(self, req):
        # return CatDto(req.body)
        return req.body
