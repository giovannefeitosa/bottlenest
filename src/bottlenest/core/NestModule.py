from bottlenest.core.NestModuleContext import NestModuleContext


class NestModule:
    def __init__(
        self,
        # from decorator
        moduleClass,
        imports,
        providers,
        controllers,
        # from NestApplicationContext
        appContext,
    ):
        self._modules = []
        self._providers = []
        # ? I'm not creating an instance of moduleClass here
        # ? should I?
        # moduleContext is exposed
        # because of NestApplicationContext.listen
        self.moduleContext = NestModuleContext(appContext)
        for importedModule in imports:
            self._modules.push(importedModule(appContext))
        for provider in providers:
            self._providers.append(provider(self.moduleContext))
        for controller in controllers:
            self._providers.append(controller(self.moduleContext))

    def listen(self, pool):
        for module in self._modules:
            module.listen(pool)
        for provider in self._providers:
            provider.listen(pool)
