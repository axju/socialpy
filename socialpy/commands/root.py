from argparse import SUPPRESS, REMAINDER

from socialpy import __version__
from socialpy.commands.generic import BasicCommand
from socialpy.dispatch import iter_entry_points_load, iter_entry_points_names, get_entry_point
from socialpy.utils import set_logger


class RootCommand(BasicCommand):
    """docstring for ConfigCommand."""

    def __init__(self, **kwargs):
        super(RootCommand, self).__init__(commands=list(iter_entry_points_names('socialpy.commands')))

    def print_command_help(self):
        width = len(self.commands)
        for name, cmd in iter_entry_points_load('socialpy.commands'):
            help = getattr(cmd, '__help__', None) or cmd.__doc__
            print('{name:>{width}} {help}'.format(name=name, help=help, width=width))

    def add_arguments(self, parser):
        parser.add_argument('-H', '--help_cmd', action='store_true', help='list all commands')
        parser.add_argument('-V', '--version', action='version', version=__version__)
        parser.add_argument('-v', '--verbose', action='count', default=0)
        parser.add_argument('command', nargs='?', choices=self.commands, help='select one command')
        parser.add_argument('args', help=SUPPRESS, nargs=REMAINDER)

    def handle(self, args):
        set_logger(args.verbose)

        if args.help_cmd:
            return self.print_command_help()

        if args.command:
            cmd = get_entry_point('socialpy.commands', args.command)
            if not issubclass(cmd, BasicCommand):
                raise Exception('Wrong type')
            command = cmd()
            return command.parse_args(args.args)

        return self.parser.print_help()
