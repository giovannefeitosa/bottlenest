from bottlenest.common import Controller, Get
from bottlenest.config import ConfigService


@Controller()
class AppController:
    configService: ConfigService

    @Get('/')
    def getHello(self, req):
        return {
            'fromEnv': self.configService.get('THE_BEST_PYTHON_FRAMEWORK')
        }
