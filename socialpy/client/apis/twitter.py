from .basic import BasicApi
from tweepy import OAuthHandler, API

class Twitter(BasicApi):

    def update_api(self):
        auth = OAuthHandler(self.ckey, self.csecret)
        auth.set_access_token(self.akey , self.asecret)
        self.api = API(auth)

    def setup(self, **kwargs):
        self.load(kwargs)

    def load(self, data):
        self.ckey = data.get('ckey')
        self.csecret = data.get('csecret')
        self.akey = data.get('akey')
        self.asecret = data.get('asecret')
        self.update_api()

    def save(self):
        return {'ckey': self.ckey,
            'csecret': self.csecret,
            'akey': self.akey,
            'asecret': self.asecret}

    def post(self, **kwargs):
        if 'text' in kwargs:
            self.api.update_status(status=kwargs['text'])
