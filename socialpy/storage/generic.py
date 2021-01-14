from logging import getLogger


class BasicStorage:
    """docstring for BasicStorage."""

    def __init__(self):
        super(BasicStorage, self).__init__()
        self.logger = getLogger('{}.{}'.format(__name__, self.__class__.__name__))
        self.data = {}

    def __len__(self):
        return len(self.data)

    def __getitem__(self, id):
        return self.data.get(id)

    def __setitem__(self, id, data):
        self.data[id] = self.data.get(id)
        if not isinstance(self.data[id], dict):
            self.data[id] = {}
        self.data[id].update(data)

    def __delitem__(self, id):
        del self.data[id]

    def update(self, id, **kwargs):
        self.__setitem__(id, kwargs)

    def filter(self, **kwargs):
        """get(api='socialpy.apis.dummy', tag='tag')"""
        for id, item in self.data.items():
            if not kwargs or all([True if item.get(key) == value else False for key, value in kwargs.items()]):
                yield id, self[id]

    def load(self):
        pass

    def save(self):
        pass
