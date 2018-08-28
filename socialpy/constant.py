import os

'''The directory for all data.'''
SOCIALPY_DIR = os.path.join(os.path.expanduser('~'), '.socialpy')

'''The file with the keys. Maybe this file contains passwords in clear text.'''
SOCIALPY_KEYS = os.path.join(SOCIALPY_DIR, 'env')
