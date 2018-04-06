from socialpy.apis.basic import BasicApi
from InstagramAPI import InstagramAPI

class Instagram(BasicApi):

    def login(self, user, pw):
        self.api = InstagramAPI(user, pw)
        if not self.api.login():
            self.api = None
            return False
        return True

    def post(self, **kwargs):
        if self.pars_args(kwargs, ['text','image']):
            self.api.uploadPhoto(kwargs['image'], caption=kwargs['text'])
