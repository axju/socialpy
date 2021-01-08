import os
from logging import getLogger
from socialpy.const import DEFAULT_WORK_DIR, DEFAULT_FILE_NAMES


logger = getLogger(__name__)


def list_to_dict(values):
    if not isinstance(values, list):
        return {}
    result = {}
    for raw in values:
        key, value = raw.split('=')
        result[key] = value
    return result


def manage_filenames(filename, workdir=DEFAULT_WORK_DIR, create=False):
    """get the filenames and create workfolder (create=True) if you like"""
    if filename in DEFAULT_FILE_NAMES:
        filename = os.path.join(workdir, DEFAULT_FILE_NAMES[filename])

    _dir = os.path.dirname(filename)
    if create and not os.path.isdir(_dir):
        logger.debug('create wor dir="%s"', _dir)
        os.makedirs(_dir)

    return filename


def get_api_infos(api):
    common_funcs = ['post', 'send', 'follower', 'following', 'feed']
    return {
        'funcs': {name: hasattr(api, name) for name in common_funcs},
        'help': str(getattr(api, '__help__', None) or api.__doc__ or ''),
    }
