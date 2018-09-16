#!/usr/bin/env python
import os
import argparse

from socialpy import SOCIALPY_KEY_FILE, SOCIALPY_DIR, API_NAMES
from socialpy.client import Gateway
from socialpy.client.apis import API_DEF


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
    parser.add_argument('action', nargs='?', type=str, choices=['setup', 'show', 'post', 'clear'])
    parser.add_argument('--text', type=str, help='...')
    parser.add_argument('--image', type=str, help='...')
    parser.add_argument('--file', type=str, help='...')
    parser.add_argument(
        '--networks', type=str, nargs='+',
        choices=API_NAMES,
        help='...')

    args = parser.parse_args()

    if args.file:
        gateway = Gateway()
        if os.path.exists(args.file):
            gateway.load_from_file(args.file)
            gateway.save_to_file(SOCIALPY_KEY_FILE)
            print('Import keys fomr the file {}'.format(args.file))
        else:
            print('No file')
        exit()

    if args.action == 'setup':
        setup()
        exit()

    if args.action == 'show':
        gateway = Gateway()
        gateway.load_from_file(SOCIALPY_KEY_FILE)

        if gateway.apis:
            print('\nYour gateway setup:')
            for key, data in gateway.apis.items():
                print('{:.<25}{}'.format(key,'radey' if data.check() else 'bad'))
        else:
            print('no gateway is rady')
        exit()

    if args.action == 'clear':
        gateway = Gateway()
        gateway.load_from_file(SOCIALPY_KEY_FILE)

        if args.networks:
            gateway.clear(args.networks)
        else:
            gateway.apis = {}

        gateway.save_to_file(SOCIALPY_KEY_FILE)
        exit()

    if args.action == 'post':
        if not args.text and not args.image:
            print('Ther is nothing to post. Use --help to see options.')
            exit()

        gateway = Gateway()
        gateway.load_from_file(SOCIALPY_KEY_FILE)

        if args.networks:
            gateway.clear(args.networks)
            #for name in API_NAMES:
            #    if name in gateway.apis and name not in args.networks:
            #        del gateway.apis[name]

        kwargs = {}
        if args.text: kwargs['text'] = args.text
        if args.image: kwargs['image'] = args.image

        print('\npost on {}\n'.format(gateway.networks()))

        gateway.post(**kwargs)
        exit()

    parser.print_help()

if __name__ == "__main__":
    main()
