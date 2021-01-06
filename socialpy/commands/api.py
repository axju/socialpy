from argparse import SUPPRESS, REMAINDER

from socialpy import SOCIALPY_API_FILE
from socialpy.storage.api import ApiFileStorage
from socialpy.utils.generic import BasicCommand
from socialpy.utils.dispatch import get_api_config, list_entry_points_names


class ApiCommand(BasicCommand):
    """docstring for ConfigCommand."""

    def add_arguments(self, parser):
        parser.add_argument('-f', '--filename', default=SOCIALPY_API_FILE, help='set api file')
        parser.add_argument('-p', '--password', help='password of api file')
        parser.add_argument('action', choices=['add', 'show', 'storage'], default='show', help='select action')
        parser.add_argument('name', nargs='?', help='api')
        parser.add_argument('key', nargs='?', help='storage key')
        parser.add_argument('args', help=SUPPRESS, nargs=REMAINDER)

    def handle(self, args):
        if args.password:
            pass
        else:
            storage = ApiFileStorage(args.filename)

        storage.load()
        if args.action == 'add':
            if not args.name:
                print('You have to set the api, try -h for halp')
                return 0
            name = args.key if args.key else args.name
            config = get_api_config(args.name)
            kwargs = config.parse_args(args.args)
            storage.update(name, api=args.name, kwargs=kwargs)
            storage.save()

        elif args.action == 'storage':
            if args.name in list(list_entry_points_names('socialpy.apis')):
                data = storage.filter(api=args.name) if args.name else storage.filter()
                for name, item in data:
                    print(name, storage.data[name])
            elif args.name in storage.data:
                print(storage.data.get(args.name))

        elif args.action == 'show':
            for name in list_entry_points_names('socialpy.apis'):
                print(name)
