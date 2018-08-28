from socialpy.gateway import Gateway
from socialpy.apis import API_DEF
from socialpy.constant import SOCIALPY_KEYS, SOCIALPY_DIR
from socialpy.data.post.models import Post

import argparse
from tabulate import tabulate

import os
from django.conf import settings
from django.core.management import call_command

def server():
    parser = argparse.ArgumentParser(description='SocialPy | SERVER')
    parser.add_argument('action', type=str, choices=['run', 'setup', 'deletedb'])
    args = parser.parse_args()

    if args.action == 'run':
        call_command('runserver',  '0.0.0.0:9999', '--insecure')

    elif args.action == 'setup':
        try:
            os.makedirs(SOCIALPY_DIR)
        except Exception as e:
            pass
        call_command('migrate')
        call_command('collectstatic')

    elif args.action == 'deletedb':
        file = settings.DATABASES['default']['NAME']
        os.remove(file)
        print('delete database:', file)


def config():
    parser = argparse.ArgumentParser(description='SocialPy | CONFIG')
    args = parser.parse_args()

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

    gateway.save_to_file(SOCIALPY_KEYS)


def data():
    parser = argparse.ArgumentParser(description='SocialPy | DATA')

    parser.add_argument('action', type=str, choices=['show', 'publish'])
    parser.add_argument('--id', type=int, help='The ID of the post')
    parser.add_argument('--status', type=str, default='new', help='Filter with status')

    args = parser.parse_args()

    if args.action == 'show':
        print('\nShow Posts:\n')

        for post in Post.objects.all():
            print(post)

    if args.action == 'publish':
        print('post')
