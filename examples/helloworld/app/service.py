from bottlenest.common import Injectable


@Injectable()
class AppService:
    def __init__(self, context):
        pass

    def getHello(self):
        return "Hello World!"
