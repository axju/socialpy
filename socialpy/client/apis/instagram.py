from .basic import BasicApi
from InstagramAPI import InstagramAPI

class Instagram(BasicApi):

    def setup(self, **kwargs):
        self.load(kwargs)        
        if not self.api.login():
            self.api = None
            return False
        return True

    def load(self, data):
        self.user = data.get('user')
        self.pw = data.get('pw')
        self.api = InstagramAPI(self.user, self.pw)

    def save(self):
        return {'user': self.user, 'pw': self.pw}

    def post(self, **kwargs):
        if self.pars_args(kwargs, ['text','image']):
            self.api.uploadPhoto(kwargs['image'], caption=kwargs['text'])
