from .basic import BasicApi
from facepy import GraphAPI

class Facebook(BasicApi):

    def setup(self, **kwargs):
        self.load(kwargs)

    def load(self, data):
        self.token = data.get('token')
        self.api = GraphAPI(self.token)

    def save(self):
        return {'token': self.token}

    def post(self, **kwargs):
        if 'text' in kwargs:
            self.api.post('me/feed', message=kwargs['text'])
