from socialpy.utils.generic import BasicApi


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


class DummyApi(BasicApi):
    """docstring for DummyApi."""

    def __init__(self, username, password, timeout=50):
        super(DummyApi, self).__init__()
        self.username = username
        self.password = password
