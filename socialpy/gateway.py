from socialpy.apis import API_DEF
from json import load, dump

class Gateway(object):
    """This is the main gateway. It collect all apis and manage the login-data"""

    def __init__(self, **kwargs):
        self.apis = {}

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
        for key, data in load(open(filename)).items():
            if key in API_DEF:
                self.apis[key] = API_DEF[key]['cls']()
                self.apis[key].load(data)

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
