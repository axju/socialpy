from socialpy.storage.generic import BasicStorage
from socialpy.storage.mixin import FileStorageMixin, EncryptFileStorageMixin
from socialpy.utils import manage_filenames
from socialpy.models import User


class UserStorage(BasicStorage):
    """docstring for ApiStorage."""

    def __getitem__(self, id):
        return User(**self.data.get(id, {}))


class UserFileStorage(FileStorageMixin, UserStorage):

    def __init__(self, filename=manage_filenames('user')):
        super(UserFileStorage, self).__init__(filename)


class UserEncryptFileStorage(EncryptFileStorageMixin, UserStorage):

    def __init__(self, filename=manage_filenames('user'), password='1234', salt=b'\x99\x9cJ\xa2}\xdcd\x1a{"\x8e\xf6s\xaa^!'):
        super(UserEncryptFileStorage, self).__init__(filename, password, salt)
