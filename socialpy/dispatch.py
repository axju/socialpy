from logging import getLogger
from pkg_resources import iter_entry_points
from inspect import isclass


def iter_entry_points_names(group):
    for enp in iter_entry_points(group=group):
        yield enp.name


def iter_entry_points_load(group):
    for enp in iter_entry_points(group=group):
        yield enp.name, enp.load()


def get_entry_point(group, name):
    for enp in iter_entry_points(group=group):
        if name == enp.name:
            return enp.load()


class ApiDispatcher(object):
    """docstring for ApiDispatcher."""

    class DummyCall(object):

        def __init__(self, name):
            self.logger = getLogger(f'{__name__}.ApiDispatcher')
            self.name = name

        def __call__(self, *args, **kwargs):
            self.logger.warning('No methode "%s" args="%s", kwargs="%s"', self.name, args, kwargs)
            return self.name

    def __init__(self, name, args=[], kwargs={}):
        super(ApiDispatcher, self).__init__()
        self.name, self.args, self.kwargs = name, args, kwargs
        self._cls, self._instance = None, None

        if not isinstance(self.kwargs, dict):
            self.kwargs = {}
        if not isinstance(self.args, list):
            self.args = []

    @property
    def cls(self):
        if not isclass(self._cls):
            self._cls = get_entry_point('socialpy.apis', self.name)
        if not isclass(self._cls):
            raise Exception(f'No api class for {self.name}')
        return self._cls

    @property
    def instance(self):
        if not isinstance(self._instance, self.cls):
            self._instance = self.cls(*self.args, **self.kwargs)
        if not isinstance(self._instance, self.cls):
            raise Exception(f'Can not create instance for {self.name}')
        return self._instance

    def __getattr__(self, name):
        if name not in ['cls', 'instance']:
            if hasattr(self.instance, name):
                return getattr(self.instance, name)
            else:
                return self.DummyCall(name)
        return getattr(self, name)
