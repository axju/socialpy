import os

__version__ = '0.0.1'
__author__ = 'Axel Juraske'


'''The directory for all data.'''
SOCIALPY_DIR = os.path.join(os.path.expanduser('~'), '.socialpy')

'''The file with the keys. Maybe this file contains passwords in clear text.'''
SOCIALPY_KEY_FILE = os.path.join(SOCIALPY_DIR, 'env')


'''Some global names'''
API_NAMES = ['facebook', 'twitter', 'instagram']
POST_STATUS = ['new', 'publish', 'arcive']
