from socialpy.storage.api import ApiFileStorage
from socialpy.utils import manage_filenames, set_logger


set_logger(3)

storage = ApiFileStorage(manage_filenames('api'))
storage.load()
api = storage['socialpy.whatsapp']

api.chats()
