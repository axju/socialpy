import os
import json
import base64
from cryptography.fernet import Fernet, InvalidToken
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC


class FileStorageMixin:
    """docstring for FileStorage."""

    def __init__(self, filename=None):
        super(FileStorageMixin, self).__init__()
        self.filename = os.path.abspath(filename) if isinstance(filename, str) else None

    def load(self):
        if not os.path.isfile(self.filename):
            return False
        with open(self.filename) as file:
            try:
                self.data = json.load(file)
            except Exception as e:
                self.logger.exception('%s', e)
                return False
        return True

    def save(self):
        with open(self.filename, 'w') as file:
            json.dump(self.data, file, indent=4)


class EncryptFileStorageMixin:
    """docstring for EncryptFileStorageMixin."""

    def __init__(self, filename, password, salt=b'\x99\x9cJ\xa2}\xdcd\x1a{"\x8e\xf6s\xaa^!'):
        super(EncryptFileStorageMixin, self).__init__()
        self.filename = os.path.abspath(filename)
        self.f = Fernet(self.generate_key(password, salt))

    def generate_key(self, password, salt):
        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,
            salt=salt,
            iterations=100000,
        )
        key = base64.urlsafe_b64encode(kdf.derive(password.encode()))
        return key

    def load(self):
        if not os.path.isfile(self.filename):
            return False
        with open(self.filename, 'rb') as file:
            _data = file.read()
        try:
            self.data = json.loads(self.f.decrypt(_data))
            if not isinstance(self.data, dict):
                self.logger.warning('Wrong data type.')
                return False
            else:
                return True
        except InvalidToken:
            self.logger.warning('Wrong password')
        except Exception as e:
            self.logger.exception('%s', e)
        return False

    def save(self):
        _data = self.f.encrypt(json.dumps(self.data).encode())
        with open(self.filename, 'wb') as file:
            file.write(_data)
