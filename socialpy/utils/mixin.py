import os
import json


class FileStorageMixin:
    """docstring for FileStorage."""

    def __init__(self, filename=None):
        super(FileStorageMixin, self).__init__()
        self.filename = os.path.abspath(filename) if isinstance(filename, str) else None

    def load(self):
        if not os.path.isfile(self.filename):
            return False
        with open(self.filename) as file:
            self.data = json.load(file)
        return True

    def save(self):
        with open(self.filename, 'w') as file:
            json.dump(self.data, file, indent=4)
