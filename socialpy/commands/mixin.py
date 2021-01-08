from socialpy.utils import manage_filenames
from socialpy.storage.misc import FileStorage, EncryptFileStorage


class StorageCommandMixin:
    """docstring for StorageCommandMixin."""

    DEFAULT_FILE = None
    STORAGE_CLS = FileStorage
    STORAGE_CLS_ENCRYPT = EncryptFileStorage

    def __init__(self, **kwargs):
        super(StorageCommandMixin, self).__init__()
        self.storage = None

    def add_arguments(self, parser):
        super(StorageCommandMixin, self).add_arguments(parser)
        parser.add_argument('-f', '--filename', default=self.DEFAULT_FILE, help='set storage file')
        parser.add_argument('-p', '--password', help='password of storage file')

    def handle(self, args):
        super(StorageCommandMixin, self).handle(args)
        if args.password:
            self.storage = self.STORAGE_CLS_ENCRYPT(args.filename, args.password)
        else:
            self.storage = self.STORAGE_CLS(args.filename)

        manage_filenames(args.filename, create=True)
        self.storage.load()
