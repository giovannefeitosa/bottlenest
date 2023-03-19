from bottlenest.common import Controller, Get
from bottlenest.config import ConfigService


@Controller()
class AppController:
    # TODO: remove the need of an empty constructor
    def __init__(self, context):
        self.configService = context.inject(ConfigService)

    @Get('/')
    def getHello(self, req):
        return {
            'fromEnv': self.configService.get('THE_BEST_PYTHON_FRAMEWORK')
        }
