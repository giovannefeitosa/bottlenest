Custom providers
================

In earlier chapters, we touched on various aspects of **Dependency Injection (DI)** and how it is used in Nest. One example of this is the :ref:`constructor based <ref-providers-dependency-injection>` dependency injection used to inject instances (often service providers) into classes. You won't be surprised to learn that Dependency Injection is built into the Nest core in a fundamental way. So far, we've only explored one main pattern. As your application grows more complex, you may need to take advantage of the full features of the DI system, so let's explore them in more detail.

DI fundamentals
---------------

Dependency injection is an `inversion of control (IoC) <https://en.wikipedia.org/wiki/Inversion_of_control>`_ technique wherein you delegate instantiation of dependencies to the IoC container (in our case, the BottleNest runtime system), instead of doing it in your own code imperatively. Let's examine what's happening in this example from the Providers chapter.

First, we define a provider. The ``@Injectable()`` decorator marks the ``CatsService`` class as a provider.

.. code-block:: python

    from bottlenest.common import Injectable
    from .interfaces.Cat import Cat

    @Injectable()
    class CatsService:
        cats: Cat[] = []

        findAll(self) -> Cat[]:
          return self.cats

Then we request that Nest inject the provider into our controller class:

.. code-block:: python

    from bottlenest.common import Controller, Get
    from .interfaces.Cat import Cat
    from .CatsService import CatsService

    @Controller('cats')
    class CatsController:
        catsService: CatsService

        @Get()
        def findAll(self) -> Cat[]:
            return self.catsService.findAll()


TODO: Continue from here https://docs.nestjs.com/fundamentals/custom-providers#di-fundamentals
