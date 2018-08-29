
class BasicApi:

    def __init__(self):
        self.api = None
        self.status = 'not implemented'

    def setup(self, **kwargs):
        return False

    def check(self):
        return self.api != None

    def pars_args(self, kwargs, ref):
        for key, value in kwargs.items():
            if key not in ref:
                self.status = 'missing '+key
                return False
        return True

    def post(self, **kwargs):
        pass

    def save(self):
        return {}

    def load(self, data):
        pass
