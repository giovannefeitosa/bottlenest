from bottlenest.common import Module
import os
from bottlenest.config import ConfigModule, ConfigService
from examples.envFile.app.AppController import AppController

# Adapt envFilePath for your needs
envFilePath = os.path.join(os.getcwd(), 'examples/envFile', '.env')


@Module(
    imports=[ConfigModule.forRoot(envFilePath=envFilePath)],
    controllers=[AppController],
    providers=[ConfigService],
)
class AppModule:
    pass
