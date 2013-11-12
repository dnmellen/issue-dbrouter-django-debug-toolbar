Issue Django debug toolbar
==============================

How to reproduce it
-----------------------------

.. code-block :: bash

    git clone git@github.com:dnmellen/issue-dbrouter-django-debug-toolbar.git
    cd issue-dbrouter-django-debug-toolbar
    mkvirtualenv issue

    # Test OK
    pip install -r requirements_good.txt
    python myproject/manage.py syncdb
    python myproject/manage.py syncdb --database='aux_db'
    python myproject/manage.py runserver
    # Access 127.0.0.1:8000 on your browser and it should work
    
    pip uninstall django-debug-toolbar

    # Test FAIL
    pip install -r requirements_bad.txt
    python myproject/manage.py runserver
    # Access 127.0.0.1:8000 on your browser and it will fail
