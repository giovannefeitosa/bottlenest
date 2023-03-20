from abc import ABC, abstractmethod, ABCMeta


class NestProviderContext(ABCMeta):
    @abstractmethod
    def __init__(self, cls):
        pass

    @abstractmethod
    def setup(self, cls, context) -> None:
        pass
