import os
import django
from django.conf import settings
from django.core.management import call_command

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "socialpy.data.settings")
django.setup()

def runserver():
    call_command('runserver',  '127.0.0.1:8000')

def deletedatabase():
    file = settings.DATABASES['default']['NAME']
    os.remove(file)
    print('delete database:', file)

def setupdatabase():
    call_command('migrate')
