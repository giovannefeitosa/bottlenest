from bottlenest.common import Controller, Get, Post, Body
from .dtos.CatDto import CatDto


@Controller()
class AppController:
    @Get('/')
    def getHello(self, req):
        return "Make a post for this url!"

    @Post('/')
    def getHello2(self, req):
        cat = CatDto(req.body)
        return {
            'name': cat.name,
            'age': cat.age,
        }
