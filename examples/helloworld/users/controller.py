from bottlenest.common import Controller, Get, Post, Param
from bottlenest.errors.http import HttpError, BadRequestError

leUsers = []


@Controller()
class UsersController:
    @Get('/users')
    def getUsers(req):
        return leUsers

    @Post('/users')
    def postUsers(req):
        if 'name' not in req.body:
            raise HttpError('name is required', 400)
        # if leUsers already have a user with this name, raise a BadRequestError
        for req.body['name'] in [user['name'] for user in leUsers]:
            raise BadRequestError('name already exists')
        leUsers.append(req.body)
        return leUsers
