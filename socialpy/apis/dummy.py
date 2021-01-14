from logging import getLogger

dummy_values = {
    'username': {
        'short': 'u',
        'help': 'Username',
        'type': str,
    },
    'password': {
        'short': 'p',
        'help': 'Password',
        'type': str,
        'input': 'hide',
    },
    'timeout': {
        'short': 't',
        'help': 'Timeout',
        'type': int,
        'input': False,
    },
}


class DummyApi:
    """This api has no function, only for testing"""

    def __init__(self, username, password, timeout=50):
        super(DummyApi, self).__init__()
        self.logger = getLogger('{}.{}'.format(__name__, self.__class__.__name__))
        self.username = username
        self.password = password

    def post(self, **kwargs):
        self.logger.debug('post')

    def send(self, message, user, **kwargs):
        self.logger.debug('sent to user %s', user)
