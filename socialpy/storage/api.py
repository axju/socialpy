from inspect import isclass
from socialpy.storage.generic import BasicStorage
from socialpy.storage.mixin import FileStorageMixin, EncryptFileStorageMixin
from socialpy.dispatch import get_entry_point
from socialpy.utils import manage_filenames


class ApiStorage(BasicStorage):
    """docstring for ApiStorage."""

    def __getitem__(self, id):
        return self.create_api(self.data.get(id))

    def filter(self, **kwargs):
        for id, api in super(ApiStorage, self).filter(**kwargs):
            if api is not None:
                yield id, api

    def get_api_cls(self, api):
        return get_entry_point('socialpy.apis', api)

    def create_api(self, item):
        cls = self.get_api_cls(item.get('api'))
        if isclass(cls):
            args, kwargs = item.get('args', []), item.get('kwargs', {})
            if not isinstance(kwargs, dict):
                kwargs = {}
            if not isinstance(args, list):
                args = []
            return cls(*args, **kwargs)
        return None


class ApiFileStorage(FileStorageMixin, ApiStorage):

    def __init__(self, filename=manage_filenames('api')):
        super(ApiFileStorage, self).__init__(filename)


class ApiEncryptFileStorage(EncryptFileStorageMixin, ApiStorage):

    def __init__(self, filename=manage_filenames('api'), password='1234', salt=b'\x99\x9cJ\xa2}\xdcd\x1a{"\x8e\xf6s\xaa^!'):
        super(ApiEncryptFileStorage, self).__init__(filename, password, salt)
