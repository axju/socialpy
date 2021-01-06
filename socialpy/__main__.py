import logging
from argparse import ArgumentParser, SUPPRESS, REMAINDER

from socialpy import __version__
from socialpy.utils.dispatch import list_entry_points_names, get_cli_command


def parse_args():
    parser = ArgumentParser(description='Use social networks like a hacker')
    parser.add_argument('-H', '--help_cmd', action='store_true', help='list all commands')
    parser.add_argument('-V', '--version', action='version', version=__version__)
    parser.add_argument('-v', '--verbose', action='count', default=0)
    parser.add_argument('command', nargs='?', choices=list(list_entry_points_names('socialpy.commands')), help='select one command')
    parser.add_argument('args', help=SUPPRESS, nargs=REMAINDER)
    args = parser.parse_args()
    return parser, args


def set_logger(verbose):
    levels = [logging.WARNING, logging.INFO, logging.DEBUG]
    level = levels[min(len(levels)-1, verbose)]
    logging.basicConfig(level=level, format="%(asctime)s %(levelname)s %(name)s %(message)s")


def print_command_help():
    for name in list_entry_points_names('socialpy.commands'):
        print(name)


def main():
    parser, args = parse_args()
    set_logger(args.verbose)

    if args.help_cmd:
        return print_command_help()

    if args.command:
        command = get_cli_command(args.command)
        return command.parse_args(args.args)

    return parser.print_help()


if __name__ == '__main__':
    main()
