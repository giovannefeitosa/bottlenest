Controllers
============

Controllers are responsible for handling incoming requests and returning responses to the client.

.. image:: /_static/img/Controllers_1.png

A controller's purpose is to receive specific requests for the application. The routing mechanism controls which controller receives which requests. Frequently, each controller has more than one route, and different routes can perform different actions.

In order to create a basic controller, we use classes and decorators. Decorators associate classes with required metadata and enable Nest to create a routing map (tie requests to the corresponding controllers).


Routing
--------

In the following example we'll use the ``@Controller()`` decorator, which is required to define a basic controller. We'll specify an optional route path prefix of cats. Using a path prefix in a ``@Controller()`` decorator allows us to easily group a set of related routes, and minimize repetitive code. For example, we may choose to group a set of routes that manage interactions with a cat entity under the route ``/cats``. In that case, we could specify the path prefix cats in the ``@Controller()`` decorator so that we don't have to repeat that portion of the path for each route in the file.

.. code-block:: python
    :linenos:

    from bottlenest.common import Controller, Get

    @Controller('cats')
    class CatsController:
      @Get()
      def findAll():
        return 'This action returns all cats'


The ``@Get()`` HTTP request method decorator before the ``findAll()`` method tells Nest to create a handler for a specific endpoint for HTTP requests. The endpoint corresponds to the HTTP request method (GET in this case) and the route path. What is the route path? The route path for a handler is determined by concatenating the (optional) prefix declared for the controller, and any path specified in the method's decorator. Since we've declared a prefix for every route (``cats``), and haven't added any path information in the decorator, Nest will map GET /cats requests to this handler. As mentioned, the path includes both the optional controller path prefix and any path string declared in the request method decorator. For example, a path prefix of cats combined with the decorator ``@Get('breed')`` would produce a route mapping for requests like GET /cats/breed.

In our example above, when a GET request is made to this endpoint, Nest routes the request to our user-defined ``findAll()`` method. Note that the method name we choose here is completely arbitrary. We obviously must declare a method to bind the route to, but Nest doesn't attach any significance to the method name chosen.

This method will return a 200 status code and the associated response, which in this case is just a string.
