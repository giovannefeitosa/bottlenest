from abc import ABC, abstractmethod, ABCMeta


class NestProvider(ABCMeta):
    # def __call__(cls, *args, **kwargs):
    #    instance = super(NestProvider, cls).__call__(*args, **kwargs)
    #    # instance.setup(*args, **kwargs)
    #    return instance

    @abstractmethod
    def __init__(self, cls):
        pass

    @abstractmethod
    def setup(self, module, context):
        pass
