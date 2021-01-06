from socialpy.utils.generic import BasicStorage, BasicApi
from socialpy.utils.mixin import FileStorageMixin


class ApiStorage(BasicStorage):
    """docstring for ApiStorage."""

    def __getitem__(self, name):
        return self.create_api(self.data.get(name))

    def get_api_cls(self, api):
        return BasicApi

    def create_api(self, item):
        cls = self.get_api_cls(item.get('api'))
        return cls(*item.get('args', []), **item.get('kwargs', {}))


class ApiFileStorage(FileStorageMixin, ApiStorage):
    pass
