SocialPy
========

Use social networks like a hacker.

SocialPy has multiple function and is designed to be very flexible. The
command line tools allowed you to post viva the terminal. This is the
way hacker should post. Write your own scrips to post automatically.

SocialPy is a small private project. I do it just for fun. So some parts
are really dirty. I would clean them up, if I'm boring. Or watch Rick
and Morty? :D

Quick start
-----------

It's a python package, use pip to install.

.. code:: bash

    pip install socialpy


The data storage.

.. code:: bash

    socialpy api list
    socialpy api show id
    socialpy api show --filter api="dummy"
    socialpy api add id -u user ...

    socialpy user show id
    socialpy user show --filter name="user"
    socialpy user add id --ids socialpy.whatsapp="username"


Chat with your frinds:

.. code:: bash

    socialpy --api socialpy.twitter send userid "Hello, how are you?"
    socialpy chat send userid "Hello, how are you?"
    socialpy chat show userid
    socialpy chat new


Post content.

.. code:: bash

    socialpy post --api socialpy.insta --text "Hello you are..." --image /home/axju/...
    socialpy post --api socialpy.twitter --text "Hello you are..."


The james command.

.. code:: bash

    socialpy james send userid "Hello, how are you?"
    socialpy james --api socialpy.whatsapp send --user test "Hello, how are you?"
    socialpy james --api socialpy.whatsapp read --user test --limit 10
    socialpy james --api socialpy.whatsapp post --text "Hello you are..." --image /home/axju/...
    socialpy james --api socialpy.twitter post --text "Hello you are..."


Deverloper infos
----------------

Run tests

.. code:: bash

    coverage run --source socialpy -m unittest
    coverage report
