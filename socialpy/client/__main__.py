#!/usr/bin/env python
from socialpy import SOCIALPY_KEY_FILE, API_NAMES
from socialpy.client import Gateway
from socialpy.client.apis import API_DEF

import argparse

def setup():
    gateway = Gateway()

    print('Setup your personal gateway')

    for name, data in API_DEF.items():
        print()
        print(name, ':')
        print('For', name, 'you need', len(data['setup']), 'values.', data['setup'])
        if str(input('Setup {}? Y/n '.format(name))).lower() in ['n', 'no', 'nein']:
            continue

        kwargs = {}
        for value in data['setup']:
            kwargs[value] = str(input('Value for '+value+': '))

        gateway[name].setup(**kwargs)

    gateway.save_to_file(SOCIALPY_KEY_FILE)


def main():
    parser = argparse.ArgumentParser(description='SocialPy | CONFIG')
    parser.add_argument('action', nargs='?', type=str, choices=['setup', 'show', 'post'])
    parser.add_argument('--text', type=str, help='...')
    parser.add_argument('--image', type=str, help='...')
    parser.add_argument(
        '--networks', type=str, nargs='+',
        choices=API_NAMES,
        help='...')

    args = parser.parse_args()

    if args.action == 'setup':
        setup()
        exit()

    if args.action == 'show':
        gateway = Gateway()
        gateway.load_from_file(SOCIALPY_KEY_FILE)

        print('\nYour gateway setup:')
        for key, data in gateway.apis.items():
            print('{:.<25}{}'.format(key,'radey' if data.check() else 'bad'))
        exit()

    if args.action == 'post':
        print('\nPost the text "{}" with the image "{}" on the networks {}'.format(args.text, args.image, args.networks))

        exit()

    parser.print_help()

if __name__ == "__main__":
    main()
