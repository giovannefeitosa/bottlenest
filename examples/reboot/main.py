# pyright: reportMissingImports=false, reportMissingModuleSource=false

# This file is a preview of the next version of bottlenest
# please ignore unknown functions and variables

from bottlenest.core import AppModule
from bottlenest.transports.http import HttpServer
from .AppProvider import AppProvider

AppModule(
    servers=[
        HttpServer(port=8080),
    ],
    providers=[AppProvider],
).run()
