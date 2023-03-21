from abc import ABC, abstractmethod, ABCMeta, abstractproperty
from bottlenest.metaClasses.NestProviderContext import NestProviderContext


class NestProvider(ABC):
    # def __call__(cls, *args, **kwargs):
    #    instance = super(NestProvider, cls).__call__(*args, **kwargs)
    #    # instance.setup(*args, **kwargs)
    #    return instance

    # @abstractmethod
    @property
    def name(self):
        return self.cls.__name__

    @property
    @abstractmethod
    def eventName(self):
        return 'NestEvent'

    def __init__(self, cls):
        self.cls = cls
        # self.name = cls.__name__

    def _getEventNames(self):
        eventClassName = self.eventName()
        eventNames = dir(self.classInstance)
        eventNames = [name for name in eventNames if type(
            getattr(self.classInstance, name)).__name__ == eventClassName]
        return eventNames

    # overridable
    # called from whithin the module's setup
    def setup(self, module, moduleContext):
        self._setup(module, moduleContext)

    def _setup(self, module, moduleContext):
        # self.module = module
        # self.moduleContext = moduleContext
        eventContext = NestProviderContext(self, moduleContext)
        self.classInstance = self.cls(eventContext)
        # self.classInstance = self.cls(moduleContext)
        eventNames = self._getEventNames()
        for eventName in eventNames:
            # print("---->> eventName: ", eventName)
            event = getattr(self.classInstance, eventName)
            event.setup(self.classInstance, moduleContext)
