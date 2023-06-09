from bottlenest.common import Controller, Get, Post
from .service import UsersService


@Controller()
class UsersController:
    usersService: UsersService

    @Get('/users')
    def getUsers(self, req):
        return self.usersService.getUsers()

    @Post('/users')
    def postUsers(self, req):
        return self.usersService.addUser(req.body)
