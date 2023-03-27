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
        # ? I'm not creating an instance of moduleClass here
        # ? should I?
        moduleContext = NestModuleContext(appContext)
        for importedModule in imports:
            importedModule(appContext)
        for provider in providers:
            provider(moduleContext)
        for controller in controllers:
            controller(moduleContext)
