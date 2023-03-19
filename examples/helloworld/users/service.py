from bottlenest.common import Injectable
from bottlenest.http import HttpError, BadRequestError


@Injectable()
class UsersService:
    def __init__(self, context):
        self.users = []

    def getUsers(self):
        return self.users

    def addUser(self, data):
        if 'name' not in data:
            raise HttpError('name is required', 400)
        # if self.users already have a user with this name, raise a BadRequestError
        for data['name'] in [user['name'] for user in self.users]:
            raise BadRequestError('name already exists')
        self.users.append(data)
        return self.users
