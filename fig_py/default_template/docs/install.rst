Installation Guide
==================

To install ``{{ project_name }}``, run the following commands in your terminal. It is **highly** reccomended that you initialize a virtual environment with ``virtualenvwrapper``:

.. code-block:: bash

   $ mkvirtualenv {{ project_name }}
   $ git clone https://github.com/{{ github_user }}/{{ project_name }}.git
   $ cd {{ project_name }}
   $ pip install -r requirements.txt
   $ pip install .

Tests can be run with ``nose`` in the projects root directory:

.. code-block:: bash

   $ nosetests



