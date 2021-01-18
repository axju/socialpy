from logging import getLogger
from datetime import datetime
from socialpy.models import User


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

    def chats(self, **kwargs):
        limit = kwargs.get('limit', 10)
        for i in range(limit):
            yield {'title': None, 'userids': ['me', 'test1']}

    def chat(self, **kwargs):
        user = kwargs.get('user', {})
        userid = User(**user).userids('socialpy.dummy')
        limit = kwargs.get('limit', 10)
        for i in range(limit):
            if i % 2:
                yield {'userid': 'me', 'msg': 'test1', 'datetime': datetime.now()}
            yield {'userid': userid, 'msg': 'test1', 'datetime': datetime.now()}
