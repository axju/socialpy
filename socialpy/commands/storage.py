from argparse import SUPPRESS, REMAINDER

from socialpy.commands.generic import BasicCommand, BasicConfig
from socialpy.commands.mixin import StorageCommandMixin
from socialpy.dispatch import iter_entry_points_load, get_entry_point
from socialpy.utils import list_to_dict, manage_filenames, get_api_infos


def get_api_config(name):
    conf = get_entry_point('socialpy.configs', name)
    if isinstance(conf, dict):
        return BasicConfig(values=conf)
    elif issubclass(conf, BasicConfig):
        return conf()
    else:
        raise Exception('Wrong type')


class BasicStorageCommand(StorageCommandMixin, BasicCommand):

    def add_arguments(self, parser):
        super(BasicStorageCommand, self).add_arguments(parser)
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
        super(BasicStorageCommand, self).handle(args)
        if args.action:
            func = getattr(self, 'handle_{}'.format(args.action))
            return func(args, self.storage)
        return self.parser.print_help()

    def handle_show(self, args, storage):
        if args.id:
            print(storage[args.id])
        else:
            filter = list_to_dict(args.filter)
            for id, item in storage.filter(**filter):
                print(id, storage[id])

    def handle_delete(self, args, storage):
        item = storage[args.id]
        if item is not None:
            del storage[args.id]
            storage.save()
            self.logger.info('delete id="%s"', args.id)


class ApiStorageCommand(BasicStorageCommand):
    """docstring for ApiStorageCommand."""

    DEFAULT_FILE = manage_filenames('api')

    def add_subparsers(self, subparser):
        subparser.add_parser('list')
        parser_add = subparser.add_parser('add')
        parser_add.add_argument('api', help='api')
        parser_add.add_argument('id', nargs='?', help='storage key')
        parser_add.add_argument('args', help=SUPPRESS, nargs=REMAINDER)

    def handle_list(self, args, storage):
        for name, api in iter_entry_points_load('socialpy.apis'):
            infos = get_api_infos(api)
            print('{:.<20}..{}'.format(name, infos.get('help')))

    def handle_add(self, args, storage):
        name = args.id if args.id else args.api
        config = get_api_config(args.api)
        kwargs = config.parse_args(args.args)
        if not isinstance(kwargs, dict):
            kwargs = {}
        storage.update(name, api=args.api, kwargs=kwargs)
        storage.save()


class UserStorageCommand(BasicStorageCommand):
    """docstring for ApiStorageCommand."""

    DEFAULT_FILE = manage_filenames('user')

    def add_subparsers(self, subparser):
        parser_add = subparser.add_parser('add')
        parser_add.add_argument('id', help='user id')
        parser_add.add_argument('--ids', nargs='*', help='socialpy.whatsapp=username')

    def handle_add(self, args, storage):
        kwargs = storage[args.id] or {'ids': {}}
        ids = list_to_dict(args.ids)
        kwargs['ids'].update(ids)
        storage.update(args.id, **kwargs)
        storage.save()
