import os
from pkg_resources import get_distribution, DistributionNotFound

try:
    __version__ = get_distribution('socialpy').version
except DistributionNotFound:
    __version__ = 'None'

del get_distribution, DistributionNotFound


'''The directory for all data.'''
SOCIALPY_DIR = os.path.join(os.path.expanduser('~'), '.socialpy')

'''The file with the accounts.'''
SOCIALPY_ACCOUNTS_FILE = os.path.join(SOCIALPY_DIR, 'accounts.json')
SOCIALPY_API_FILE = os.path.join(SOCIALPY_DIR, 'apis.json')
