import os
from .__about__ import (
    __author__, __copyright__, __email__, __license__, __summary__, __title__,
    __url__, __version__
)

__all__ = [
    '__title__', '__summary__', '__url__', '__version__', '__author__',
    '__email__', '__license__', '__copyright__',
]

'''The directory for all data.'''
SOCIALPY_DIR = os.path.join(os.path.expanduser('~'), '.socialpy')

'''The file with the keys. Maybe this file contains passwords in clear text.'''
SOCIALPY_KEY_FILE = os.path.join(SOCIALPY_DIR, 'env')

'''Some global names'''
API_NAMES = ['facebook', 'twitter', 'instagram']
POST_STATUS = ['new', 'publish', 'arcive']
