import sys
from argparse import ArgumentParser
from getpass import getpass
from logging import getLogger


class BasicCommand:
    """docstring for BasicCommand."""

    def __init__(self, **kwargs):
        super(BasicCommand, self).__init__()
        self.logger = getLogger('{}.{}'.format(__name__, self.__class__.__name__))
        for name, value in kwargs.items():
            setattr(self, name, value)

    def parse_args(self, argv=None):
        self.parser = ArgumentParser(description='Use social networks like a hacker')
        self.add_arguments(self.parser)
        if argv is None:
            args = self.parser.parse_args(sys.argv[1:])
        else:
            args = self.parser.parse_args(argv)
        return self.handle(args)

    def add_arguments(self, parser):
        pass

    def handle(self, args):
        pass


class BasicConfig(BasicCommand):
    """docstring for BasicConfig."""

    def __init__(self, **kwargs):
        super(BasicConfig, self).__init__()
        self.values = kwargs.get('values', getattr(self, 'values', {}))

    def add_arguments(self, parser):
        for name, conf in self.values.items():
            names = ['-'+conf['short'], '--'+name] if 'short' in conf else ['--'+name]
            parser.add_argument(*names, type=conf.get('type', str), help=conf.get('help', ''))

    def convert_args(self, args):
        result = {}
        for name, conf in self.values.items():
            value = getattr(args, name, None)
            _type = conf.get('type', str)
            if value is None:
                tmp = conf.get('input', True)
                default = conf.get('default')
                prompt = name
                prompt += '[{}]: '.format(default) if default else ': '
                if isinstance(tmp, str) and tmp == 'hide':
                    value = getpass(prompt=prompt) or conf.get('default', _type())
                elif tmp:
                    value = input(prompt) or conf.get('default', _type())

            if value is not None:
                result[name] = _type(value)

        self.logger.debug('convert_args result=%s', result)
        return result

    def handle(self, args):
        return self.convert_args(args)
