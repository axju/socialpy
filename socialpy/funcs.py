import os
import django
import shutil

from socialpy import SOCIALPY_DIR

def setup():
    """This function setup your Gateway"""

    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "socialpy.server.settings.base")
    try:
        django.setup()
        from django.core.management import call_command
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc

    # create the data folder
    try:
        os.makedirs(SOCIALPY_DIR)
    except Exception as e:
        pass

    # setup the server
    call_command('migrate', '--noinput')
    call_command('collectstatic', '--noinput')

def clear():
    shutil.rmtree(SOCIALPY_DIR)

def check(**kwargs):
    if 'create' in kwargs and kwargs['create']:
        if not os.path.isdir(SOCIALPY_DIR):
            setup()
    return os.path.isdir(SOCIALPY_DIR)
