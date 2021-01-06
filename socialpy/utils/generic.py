from argparse import ArgumentParser
from getpass import getpass
from logging import getLogger


class BasicApi:
    """docstring for BasicApi."""

    def __init__(self, *args, **kwargs):
        super(BasicApi, self).__init__()
        self.logger = getLogger('{}.{}'.format(__name__, self.__class__.__name__))
        self.args = args
        self.kwargs = kwargs

    def post(self, **kwargs):
        self.logger.info('post')

    def send(self, user, message):
        self.logger.info('sent to user %s', user)


class BasicCommand:
    """docstring for BasicCommand."""

    def __init__(self, **kwargs):
        super(BasicCommand, self).__init__()
        for name, value in kwargs.items():
            setattr(self, name, value)

    def parse_args(self, args):
        parser = ArgumentParser(description='Use social networks like a hacker')
        self.add_arguments(parser)
        _args = parser.parse_args(args)
        return self.handle(_args) or 1

    def add_arguments(self, parser):
        pass

    def handle(self, args):
        pass


class BasicConfig(BasicCommand):
    """docstring for BasicConfig."""

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
                prompt = '{} : '.format(name)
                tmp = conf.get('input', True)
                if isinstance(tmp, str) and tmp == 'hide':
                    value = getpass(prompt=prompt) or conf.get('default', _type())
                elif tmp:
                    value = input(prompt) or conf.get('default', _type())

            if value is not None:
                result[name] = _type(value)

        return result

    def handle(self, args):
        return self.convert_args(args)


class BasicStorage:
    """docstring for BasicStorage."""

    def __init__(self):
        super(BasicStorage, self).__init__()
        self.data = {}

    def __len__(self):
        return len(self.data)

    def __getitem__(self, name):
        return self.data.get(name)

    def __setitem__(self, name, data):
        self.data[name] = self.data.get(name)
        if not isinstance(self.data[name], dict):
            self.data[name] = {}
        self.data[name].update(data)

    def update(self, name, **kwargs):
        self.__setitem__(name, kwargs)

    def filter(self, **kwargs):
        """get(api='socialpy.apis.dummy', tag='tag')"""
        for name, item in self.data.items():
            if not kwargs or all([True if item.get(key) == value else False for key, value in kwargs.items()]):
                yield name, self[name]

    def load(self):
        pass

    def save(self):
        pass
