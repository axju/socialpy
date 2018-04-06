from socialpy.apis import MAPPING
from json import load, dump

class Gateway(object):
    '''This is the main gateway. It collect all apis and manage the data'''

    def __init__(self, **kwargs):
        self.apis = {}

        #for key, value in kwargs.items():
        #    print(key, value)

    def __getitem__(self, key):
        if key in self.apis:
            return self.apis[key]

        if key in MAPPING:
            self.apis[key] = MAPPING[key]()
            return self.apis[key]

    def save_to_file(self, filename):
        data = {}
        for name, api in self.apis.items():
            data[name] = api.save()

        with open(filename, 'w') as outfile:
            dump(data, outfile, indent=4, sort_keys=True)

    def load_from_file(self, filename):
        for key, data in load(open(filename)).items():
            if key in MAPPING:
                self.apis[key] = MAPPING[key]()
                self.apis[key].load(data)

    def post(self, **kwargs):
        '''Post something on all available networks'''
        for name, api in self.apis.items():
            print(name)
            print('check: ', api.check())
            print('status:', api.status)
            if api.check():
                api.post(**kwargs)
                #try:
                #    api.post(**kwargs)
                #except Exception as e:
                #    print('Error while posting with', name)
                #    print(e)

            print()
