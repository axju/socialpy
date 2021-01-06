from logging import getLogger
from socialpy.storage.api import ApiStorage
from socialpy.utils.mixin import FileStorageMixin


class JamesApiStorage(FileStorageMixin, ApiStorage):
    pass


class James(object):
    """docstring for James."""

    def __init__(self, api_storage_cls=JamesApiStorage, api_storage_kwargs={'filename': None}):
        super(James, self).__init__()
        self.logger = getLogger('{}.{}'.format(__name__, self.__class__.__name__))
        self.apis = api_storage_cls(**api_storage_kwargs)
        self.apis.load()

    def post(self, post, filter={}):
        self.logger.debug('post=%s filter=%s', post, filter)
        for name, api in self.apis.filter(**filter):
            self.logger.info('post on api %s', name)
            api.post(**post)
