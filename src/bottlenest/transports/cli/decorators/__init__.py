from bottlenest.transports.cli.decorators.NestCommand import NestCommand


def Command(name, description):
    def decorator(cls):
        return NestCommand(
            cls=cls,
            commandName=name,
            description=description,
        )
    return decorator
