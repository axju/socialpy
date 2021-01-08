from socialpy.storage.generic import BasicStorage
from socialpy.storage.mixin import FileStorageMixin, EncryptFileStorageMixin
from socialpy.dispatch import get_entry_point


class ApiStorage(BasicStorage):
    """docstring for ApiStorage."""

    def __getitem__(self, id):
        return self.create_api(self.data.get(id))

    def get_api_cls(self, api):
        return get_entry_point('socialpy.apis', api)

    def create_api(self, item):
        cls = self.get_api_cls(item.get('api'))
        return cls(*item.get('args', []), **item.get('kwargs', {}))


class ApiFileStorage(FileStorageMixin, ApiStorage):
    pass


class ApiEncryptFileStorage(EncryptFileStorageMixin, ApiStorage):
    pass
