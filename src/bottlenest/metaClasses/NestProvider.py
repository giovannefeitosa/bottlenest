from abc import ABC, abstractmethod, ABCMeta
from bottlenest.metaClasses.NestProviderContext import NestProviderContext


class NestProvider(ABCMeta):
    # def __call__(cls, *args, **kwargs):
    #    instance = super(NestProvider, cls).__call__(*args, **kwargs)
    #    # instance.setup(*args, **kwargs)
    #    return instance

    @abstractmethod
    def __init__(self, cls):
        pass

    @abstractmethod
    def setup(self, module, context) -> NestProviderContext:
        pass

    def _setup(self, module, context) -> NestProviderContext:
        return self.setup(module, context)
