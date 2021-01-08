import logging
from argparse import SUPPRESS, REMAINDER

from socialpy import __version__
from socialpy.commands.generic import BasicCommand
from socialpy.dispatch import iter_entry_points_names, get_cli_command


class RootCommand(BasicCommand):
    """docstring for ConfigCommand."""

    def set_logger(self, verbose):
        levels = [logging.WARNING, logging.INFO, logging.DEBUG]
        level = levels[min(len(levels)-1, verbose)]
        logging.basicConfig(level=level, format="%(asctime)s %(levelname)s %(name)s %(message)s")

    def print_command_help(self):
        for name in iter_entry_points_names('socialpy.commands'):
            print(name)

    def add_arguments(self, parser):
        parser.add_argument('-H', '--help_cmd', action='store_true', help='list all commands')
        parser.add_argument('-V', '--version', action='version', version=__version__)
        parser.add_argument('-v', '--verbose', action='count', default=0)
        parser.add_argument('command', nargs='?', choices=list(iter_entry_points_names('socialpy.commands')), help='select one command')
        parser.add_argument('args', help=SUPPRESS, nargs=REMAINDER)

    def handle(self, args):
        self.set_logger(args.verbose)

        if args.help_cmd:
            return self.print_command_help()

        if args.command:
            command = get_cli_command(args.command)
            return command.parse_args(args.args)

        return self.parser.print_help()
