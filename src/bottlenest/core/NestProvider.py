from abc import ABC


class NestProvider(ABC):
    def __init__(self, providerClass, moduleContext):
        print(f"NestProvider init")
