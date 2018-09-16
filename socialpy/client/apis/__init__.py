#from socialpy.client.apis.facebook import Facebook
from socialpy.client.apis.twitter import Twitter
#from socialpy.client.apis.instagram import Instagram

API_DEF = {
    #'facebook': {'cls': Facebook, 'setup': ['token']},
    'twitter': {'cls': Twitter, 'setup': ['ckey', 'csecret', 'akey', 'asecret']},
    #'instagram': {'cls': Instagram, 'setup': ['user', 'pw']},
}
