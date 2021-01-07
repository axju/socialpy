from argparse import SUPPRESS, REMAINDER

from socialpy import SOCIALPY_API_FILE, SOCIALPY_USER_FILE
from socialpy.utils.generic import BasicCommand
from socialpy.utils.dispatch import list_entry_points_names, get_api_config
from socialpy.utils.misc import list_to_dict
from socialpy.storage.misc import FileStorage


class BasicStorageCommand(BasicCommand):

    DEFAULT_FILE = None

    def add_arguments(self, parser):
        parser.add_argument('-f', '--filename', default=self.DEFAULT_FILE, help='set sorage file')
        parser.add_argument('-p', '--password', help='password of api file')
        subparser = parser.add_subparsers(dest='action')

        parser_show = subparser.add_parser('show')
        parser_show.add_argument('--filter', nargs='*', help='set a filter api=test')
        parser_show.add_argument('id', nargs='?', help='sorage id')

        parser_delete = subparser.add_parser('delete')
        parser_delete.add_argument('--filter', nargs='*', help='set a filter api=test')
        parser_delete.add_argument('id', nargs='?', help='sorage id')

        self.add_subparsers(subparser)

    def add_subparsers(self, subparser):
        pass

    def handle(self, args):
        if args.password:
            pass
        else:
            storage = FileStorage(args.filename)
        storage.load()
        func = getattr(self, 'handle_{}'.format(args.action))
        return func(args, storage)

    def handle_show(self, args, storage):
        if args.id:
            print(storage[args.id])
        else:
            filter = list_to_dict(args.filter)
            for id, item in storage.filter(**filter):
                print(id, storage[id])


class ApiStorageCommand(BasicStorageCommand):
    """docstring for ApiStorageCommand."""

    DEFAULT_FILE = SOCIALPY_API_FILE

    def add_subparsers(self, subparser):
        subparser.add_parser('list')
        parser_add = subparser.add_parser('add')
        parser_add.add_argument('api', help='api')
        parser_add.add_argument('id', nargs='?', help='storage key')
        parser_add.add_argument('args', help=SUPPRESS, nargs=REMAINDER)

    def handle_list(self, args, storage):
        for name in list_entry_points_names('socialpy.apis'):
            print(name)

    def handle_add(self, args, storage):
        name = args.id if args.id else args.api
        config = get_api_config(args.api)
        kwargs = config.parse_args(args.args)
        storage.update(name, api=args.api, kwargs=kwargs)
        storage.save()


class UserStorageCommand(BasicStorageCommand):
    """docstring for ApiStorageCommand."""

    DEFAULT_FILE = SOCIALPY_USER_FILE

    def add_subparsers(self, subparser):
        parser_add = subparser.add_parser('add')
        parser_add.add_argument('id', help='user id')
        parser_add.add_argument('args', nargs='*', help='add any values name=test age=50')

    def handle_add(self, args, storage):
        kwargs = list_to_dict(args.args)
        storage.update(args.id, **kwargs)
        storage.save()
