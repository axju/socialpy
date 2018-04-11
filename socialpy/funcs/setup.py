from socialpy import Gateway
from socialpy.apis import API_DEF


def run():
    gateway = Gateway()

    print('Setup your personal gateway')

    for name, data in API_DEF.items():
        print()
        print(name, ':')
        print('For', name, 'you need', len(data['setup']), 'values.', data['setup'])
        if str(input('Setup Twitter? Y/n ')).lower() in ['n', 'no', 'nein']:
            continue

        kwargs = {}
        for value in data['setup']:
            kwargs[value] = str(input('Value for '+value+': '))

        gateway[name].setup(**kwargs)

    gateway.save_to_file('.env')
