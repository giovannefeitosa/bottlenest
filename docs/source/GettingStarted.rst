Getting Started
===============

BottleNest is a versatile microservices framework for Python 3, inspired by NestJS for Node.js. With intuitive syntax and modern design patterns, it provides routing, controllers, middleware, and dependency injection. BottleNest allows for scalable, maintainable, and high-performance microservices, ideal for small-scale applications or large-scale enterprise systems in Python.

Installation
------------

Install BottleNest with pip:


.. code-block:: bash
    :linenos:

    pip install bottlenest

    python -m bottlenest new project-name


The `project-name` directory will be created, poetry and a few other boilerplate files will be installed.


.. code-block:: markdown
    
    project-name
    ├── src
    |   └── project-name
    |       ├── app
    |       |   ├── AppController.py
    |       |   ├── AppModule.py
    |       |   └── AppService.py
    |       ├── main.py
    |       └── __init__.py
    |  
    ├── pyproject.toml
    ├── README.md
    └── .gitignore


Running the application
-----------------------

Once the installation process is complete, you can run the following command at your OS command prompt to start the application listening for inbound HTTP requests:

.. code-block:: bash
    :linenos:

    poetry run start


This command starts the app with the HTTP server listening on the port defined in the src/main.ts file. Once the application is running, open your browser and navigate to http://localhost:3000/. You should see the Hello World! message.

To watch for changes in your files, you can run the following command to start the application:


.. code-block:: bash
    :linenos:

    poetry run start:dev

This command will watch your files, automatically recompiling and reloading the server.
