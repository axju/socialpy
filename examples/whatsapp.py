from time import sleep
from socialpy.storage.api import ApiFileStorage
from socialpy.utils import set_logger


set_logger(3)

storage = ApiFileStorage()
storage.load()
api = storage['socialpy.whatsapp']
api.login()

# for chat in api.chats():
#     print(chat)


user = {
    'ids': {
        'socialpy.whatsapp': 'Username',
    },
}

api.send('Hi, how are you?', user=user)
sleep(5)
