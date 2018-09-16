import os
from json import load, dump

from socialpy.client.apis import API_DEF


class Gateway(object):
    """This is the main gateway. It collect all apis and manage the login-data"""

    def __init__(self, **kwargs):
        self.apis = {}

        if 'keyfile' in kwargs:
            self.load_from_file(kwargs['keyfile'])

    def __getitem__(self, key):
        if key in self.apis:
            return self.apis[key]

        if key in API_DEF:
            self.apis[key] = API_DEF[key]['cls']()
            return self.apis[key]



    def save_to_file(self, filename):
        data = {}
        for name, api in self.apis.items():
            data[name] = api.save()

        with open(filename, 'w') as outfile:
            dump(data, outfile, indent=4, sort_keys=True)

    def load_from_file(self, filename):
        if not os.path.isfile(filename): return

        for key, data in load(open(filename)).items():
            if key in API_DEF:
                self.apis[key] = API_DEF[key]['cls']()
                self.apis[key].load(data)

    def clear(self, networks):
        '''Remove all apis which ar not in the networks parameterself.'''
        tmp = []
        for name in self.apis:
            if name not in networks:
                tmp.append(name)
        for name in tmp:
            del self.apis[name]

    def check(self, networks):
        for name in networks:
            if name not in self.apis:
                return False
        return True

    def networks(self):
        return [ name for name in self.apis ]

    def post(self, **kwargs):
        """Post something on all available networks"""
        for name, api in self.apis.items():
            print(name)
            #print('status:', api.status)
            if api.check():
                print('posting...')
                api.post(**kwargs)
                #try:
                #    api.post(**kwargs)
                #except Exception as e:
                #    print('Error while posting with', name)
                #    print(e)
            else:
                print('not radey for posting')
            print()
