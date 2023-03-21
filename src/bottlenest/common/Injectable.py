def Injectable():
    def wrapper(originalClass):
        return NestInjectable(
            originalClass=originalClass,
        )
    return wrapper


class NestInjectable:
    __name__ = 'NestInjectable'

    def __init__(self, originalClass):
        # self.__name__ = originalClass.__name__
        self.providerName = originalClass.__name__
        self.originalClass = originalClass
        self.providerInstance = None
        # self.dependencies = []

    def setup(self, module, container):
        # self.module = module
        # self.container = container
        # TODO: This should be a singleton manager
        self.providerInstance = self.originalClass(container)
        # providerName = f"{module.moduleName}.{self.providerName}"
        providerName = self.providerName
        container.set(providerName, self)

    def __repr__(self):
        return f"{self.providerName}()"

    def __str__(self):
        return f"{self.providerName}()"
