from socialpy.utils import manage_filenames
from socialpy.commands.generic import BasicCommand
from socialpy.commands.mixin import StorageCommandMixin
from socialpy.storage.api import ApiFileStorage, ApiEncryptFileStorage


class PostCommand(StorageCommandMixin, BasicCommand):
    """docstring for ConfigCommand."""

    DEFAULT_FILE = manage_filenames('api')
    STORAGE_CLS = ApiFileStorage
    STORAGE_CLS_ENCRYPT = ApiEncryptFileStorage

    def handle(self, args):
        super(PostCommand, self).handle(args)
        post = {}
        filter = {}
        for name, api in self.storage.filter(**filter):
            self.logger.debug('post on api %s', name)
            api.post(**post)
