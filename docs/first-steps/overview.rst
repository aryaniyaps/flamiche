====================
Flamiche at a glance
====================

Flamiche is a lightweight `WSGI`_/ `ASGI`_ micro web framework. It is designed to 
be easy to begin with, and has the ability to scale up to complex applications.

.. _WSGI: https://wsgi.readthedocs.io/en/latest/
.. _ASGI: https://asgi.readthedocs.io/en/latest/

How Flamiche fits in your stack
===============================

Most developers follow a layered architecture when creating web applications. 
There are usually four layers in a typical layered architecture:

* **The API layer**
  
  The API layer displays the user interface and facilitates user interaction. There would 
  be user interface components that render and format data for users and user process components 
  that orchestrate user interactions. The API layer provides necessary data to the 
  client’s side. It receives input data, processes user’s requests, sends them to data services, 
  and puts results to the browser. 

* **The Data Service layer**
  
  The Data Service layer's function is to transmit data processed by the 
  Business Logic layer   to the API layer. The data service layer ensures the security 
  of information separating business logic from the client-side.

* **The Business Logic layer**
  
  The Business Logic layer ensures proper data exchange and controls application functionality. It’s the 
  layer that defines logic for business operations, business rules and satisfies business needs.  

* **The Persistence layer**
  
  The Persistence layer allows access to the application's datastore, binary files, XML files, etc. 
  This layer also performs CRUD operations – create, read, update, delete.


Flamiche helps in building your application's API layer. It handles routing and request dispatching,
leaving the rest upto you. Python has a great ecosystem of libraries that help in building other parts
of your application.