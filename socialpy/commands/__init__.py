from socialpy.utils.generic import BasicCommand
from socialpy.commands.api import ApiCommand


__all__ = ['ApiCommand', 'PostCommand']


class PostCommand(BasicCommand):
    """docstring for ConfigCommand."""

    def add_arguments(self, parser):
        pass

    def handle(self, args):
        pass
