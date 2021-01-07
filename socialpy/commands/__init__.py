from socialpy.utils.generic import BasicCommand
from socialpy.commands.storage import ApiStorageCommand, UserStorageCommand


__all__ = ['ApiStorageCommand', 'UserStorageCommand', 'PostCommand']


class PostCommand(BasicCommand):
    """docstring for ConfigCommand."""

    def add_arguments(self, parser):
        pass

    def handle(self, args):
        pass
