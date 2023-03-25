Providers
==========

Providers are a fundamental concept in Nest. Many of the basic Nest classes may be treated as a provider - services, repositories, factories, helpers, and so on. The main idea of a provider is that it can be injected as a dependency; this means objects can create various relationships with each other, and the function of "wiring up" instances of objects can largely be delegated to the Nest runtime system.

.. image:: /_static/img/Components_1.png

In the previous chapter, we built a simple ``CatsController``. Controllers should handle HTTP requests and delegate more complex tasks to providers. Providers are plain JavaScript classes that are declared as ``providers`` in a :doc:`module <Module>`.

.. note::
    Since Nest enables the possibility to design and organize dependencies in a more OO way, we strongly recommend following the SOLID principles.

Services
--------

Let's start by creating a simple ``CatsService``. This service will be responsible for data storage and retrieval, and is designed to be used by the ``CatsController``, so it's a good candidate to be defined as a provider.

.. code-block:: python
    :caption: cats/CatsService.py

    from bottlenest.common import Injectable
    from .interfaces.Cat import Cat

    @Injectable()
    class CatsService:
        cats: Cat[] = []

        def create(cat: Cat):
            self.cats.append(cat)

        def findAll() -> Cat[]:
            return self.cats

Our ``CatsService`` is a basic class with one property and two methods. The only new feature is that it uses the ``@Injectable()`` decorator. The ``@Injectable()`` decorator attaches metadata, which declares that ``CatsService`` is a class that can be managed by the Nest `IoC <https://en.wikipedia.org/wiki/Inversion_of_control>`_ container. By the way, this example also uses a ``Cat`` interface, which probably looks something like this:

.. code-block:: python
    :caption: cats/interfaces/Cat.py

    from pydantic import BaseModel

    class Cat(BaseModel):
        id: int | None
        name: str
        age: int
        breed: str | None

.. code-block:: python
    :caption: cats/CatsController.py

    from bottlenest.common import Controller, Get, Post, Body
    from bottlenest.interfaces import ProviderContext, RouteContext
    from .dto.CreateCatDto import CreateCatDto
    from .CatsService import CatsService
    from .interfaces.Cat import Cat

    @Controller('cats')
    class CatsController:
        catsService: CatsService

        @Post()
        @Body(CreateCatDto)
        def create(self, context: RouteContext) -> Cat:
            cat = self.catsService.create(context.body)
            return cat

        @Get()
        def findAll(self) -> Cat[]:
            return self.catsService.findAll()

The ``CatsService`` is injected through the class constructor. This shorthand allows us to both declare and initialize the catsService member immediately in the same location.

.. _ref-providers-dependency-injection:

Dependency injection
--------------------

Nest is built around the strong design pattern commonly known as **Dependency injection**. We recommend reading a great article about this concept in the official `Angular <https://angular.io/guide/dependency-injection>`_ documentation.

In Nest, thanks to TypeScript capabilities, it's extremely easy to manage dependencies because they are resolved just by type. In the example below, Nest will resolve the ``catsService`` by creating and returning an instance of ``CatsService`` (or, in the normal case of a singleton, returning the existing instance if it has already been requested elsewhere). This dependency is resolved and passed to your controller's constructor (or assigned to the indicated property):

.. code-block:: python

    @Controller('cats')
    class CatsController:
        catsService: CatsService

Custom Providers
----------------

Nest has a built-in inversion of control ("IoC") container that resolves relationships between providers. This feature underlies the dependency injection feature described above, but is in fact far more powerful than what we've described so far. There are several ways to define a provider: you can use plain values, classes, and either asynchronous or synchronous factories. More examples are provided :doc:`here </fundamentals/CustomProviders>`.

TODO: Continue this section from https://docs.nestjs.com/providers#custom-providers

