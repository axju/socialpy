from socialpy import SOCIALPY_DIR
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SECRET_KEY = 'usipv&3sgwersdghghfes2dn7+32_lgfn)y_z1(ar1!8l=a3x'

INSTALLED_APPS = ['socialpy.server.data',]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(SOCIALPY_DIR, 'socialpy.sqlite3'),
    }
}
