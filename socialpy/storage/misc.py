from socialpy.storage.generic import BasicStorage
from socialpy.storage.mixin import FileStorageMixin, EncryptFileStorageMixin


class FileStorage(FileStorageMixin, BasicStorage):
    pass


class EncryptFileStorage(EncryptFileStorageMixin, BasicStorage):
    pass
