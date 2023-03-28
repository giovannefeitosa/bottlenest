# from bottlenest.core.NestTransport import NestTransport
from bottlenest.transports.http.HttpTransport import HttpTransport


class NestModuleContext:
    def __init__(self, appContext):
        self.appContext = appContext
        self.container = {}

    def get(self, key, defaultValue=None):
        print("NestModuleContext get", key)
        return self.container[key] if key in self.container else defaultValue

    def set(self, key, value):
        print("NestModuleContext set", key, value)
        self.container[key] = value

    def registerProvider(self, provider):
        print("NestModuleContext registerProvider", provider.__name__)
        self.container[provider.__name__] = provider

    def getOrCreateTransport(self, transport):
        try:
            transport = self.appContext.getTransport(transport)
        except Exception:
            self.appContext.addTransport(transport)
        return transport

    def getDefaultHttpTransport(self) -> HttpTransport:
        return self.appContext.getDefaultHttpTransport()

    # TODO: is this inject method needed?
    # def inject(self, injectable):
    #     moduleName = self.container['module'].name
    #     providerName = injectable.__name__
    #     key = f"{moduleName}.{providerName}"
    #     provider = self.container[key] if key in self.container else None
    #     if provider:
    #         return provider.instance
    #     else:
    #         raise Exception(f"Provider not found: {key}")
