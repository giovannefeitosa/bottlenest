from bottlenest.common import Controller, Get, Post
from examples.helloworld.users.service import UsersService


@Controller()
class UsersController:
    def __init__(self, context):
        self.usersService = context.inject(UsersService)

    @Get('/users')
    def getUsers(self, req):
        return self.usersService.getUsers()

    @Post('/users')
    def postUsers(self, req):
        return self.usersService.addUser(req.body)
