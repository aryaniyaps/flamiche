==================
Installation guide
==================

This guide helps you in installing Flamiche on your machine.

Requirements
============

Flamiche requires Python (3.8, 3.9, 3.10). You can get the latest version of Python `here`_ 
or with your operating system’s package manager. You can verify that Python is installed by 
typing python from your shell.

.. _here: https://www.python.org/downloads/

You should see something like:::

    Python 3.x.y
    [GCC 4.x] on linux
    Type "help", "copyright", "credits" or "license" for more information.
    >>>

We **highly recommend** and officially support only the latest patch release of Python.

Virtual environments
====================

We recommend using a virtual environment to manage the dependencies for your project, both in 
development and in production.

What problem does a virtual environment solve? The more Python projects you have, the more likely 
it is that you need to work with different versions of Python libraries, or even Python itself. 
Newer versions of libraries for one project can break compatibility in another project.

Virtual environments are independent groups of Python libraries, one for each project. Packages 
installed for one project will not affect other projects or the operating system’s packages.

Python comes bundled with the venv module to create virtual environments.


Create an environment
=====================

Create a project folder and a venv folder within:

.. tabs::
    
    .. tab:: MacOS/Linux

        ```text
        $ mkdir myproject
        $ cd myproject
        $ python3 -m venv venv
        ```

    .. tab:: Windows

        ```text
        > mkdir myproject
        > cd myproject
        > py -3 -m venv venv
        ```

Activate the environment
========================

Before you work on your project, activate the corresponding environment:

.. tabs::

    .. tab:: MacOS/Linux

        ```text
        $ . venv/bin/activate
        ```
    
    .. tab:: Windows

        ```text
        > venv\Scripts\activate
        ```

Install Flamiche
================

Within the activated environment, installation can be done using `pip`_:::

    pip install flamiche

.. _pip: https://pip.pypa.io/en/stable/

Flamiche is now installed on your machine and ready to go!