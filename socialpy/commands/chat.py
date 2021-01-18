from socialpy.utils import manage_filenames
from socialpy.commands.generic import BasicCommand
from socialpy.storage.api import ApiFileStorageDispatch, ApiEncryptFileStorageDispatch
from socialpy.storage.user import UserFileStorage, UserEncryptFileStorage


class ChatCommand(BasicCommand):
    """docstring for ConfigCommand."""

    def add_arguments(self, parser):
        super(ChatCommand, self).add_arguments(parser)
        parser.add_argument('-uf', '--userfile', default=manage_filenames('user'), help='set storage file')
        parser.add_argument('-up', '--userpassword', help='password of storage file')
        parser.add_argument('-af', '--apifile', default=manage_filenames('api'), help='set storage file')
        parser.add_argument('-ap', '--apipassword', help='password of storage file')
        parser.add_argument('-a', '--api', help='api')
        subparser = parser.add_subparsers(dest='action')

        parser_send = subparser.add_parser('send', help='send a message')
        parser_send.add_argument('user', help='user id')
        parser_send.add_argument('message', help='the message')

        parser_show = subparser.add_parser('show', help='show some messages')
        parser_show.add_argument('-l', '--limit', type=int, default=10, help='limit of messages')
        parser_show.add_argument('user', help='user id')

        subparser.add_parser('new', help='comming soon')

    def get_user(self, args):
        if args.userpassword:
            users = UserEncryptFileStorage(args.userfile, args.userpassword)
        else:
            users = UserFileStorage(args.userfile)
        users.load()
        return users[args.user]

    def get_api(self, args, user):
        if args.apipassword:
            apis = ApiEncryptFileStorageDispatch(args.apifile, args.apipassword)
        else:
            apis = ApiFileStorageDispatch(args.apifile)
        apis.load()
        if args.api:
            return apis[args.api]
        elif len(apis) > 0 and user.check('ids', list):
            for apiname, userid in user['ids']:
                if len(list(apis.filter(api=apiname))):
                    _, api = next(apis.filter(api=apiname))
                    return api
        return None

    def handle(self, args):
        super(ChatCommand, self).handle(args)
        if not args.action:
            self.parser.print_help()
            return 0

        user = self.get_user(args)
        if not user:
            self.logger.warning('No user with id="%s"', args.user)
            return 0

        api = self.get_api(args, user)
        if not api:
            self.logger.warning('Set the api')
            return 0

        api.login()
        if args.action == 'send':
            self.logger.info('Send: userid="%s", msg="%s"', args.user, args.message)
            api.send(args.message, user=dict(user))
        elif args.action == 'show':
            self.logger.info('Show msg from userid="%s"', args.user)
            width = max(2, len(user.userids(api.name)))
            for msg in api.chat(user=dict(user), limit=args.limit):
                print('{datetime} {userid:>{width}} --> {msg}'.format(width=width, **msg))

        return 1
