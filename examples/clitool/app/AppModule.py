from bottlenest.common import Module
from examples.clitool.app.EchoCommand import EchoCommand


@Module(
    providers=[EchoCommand],
)
class AppModule:
    pass
