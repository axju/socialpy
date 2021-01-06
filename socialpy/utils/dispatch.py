from pkg_resources import iter_entry_points

from socialpy.utils.generic import BasicConfig, BasicCommand


def iter_apis():
    for enp in iter_entry_points(group='socialpy.apis'):
        yield enp.name


def list_entry_points_names(group):
    for enp in iter_entry_points(group=group):
        yield enp.name


def get_api_config(name):
    for enp in iter_entry_points(group='socialpy.configs'):
        if name == enp.name:
            conf = enp.load()
            if isinstance(conf, dict):
                return BasicConfig(values=conf)
            elif issubclass(conf, BasicConfig):
                return conf()
            else:
                raise Exception('Wrong type')


def get_cli_command(name):
    for enp in iter_entry_points(group='socialpy.commands'):
        if name == enp.name:
            cmd = enp.load()
            if not issubclass(cmd, BasicCommand):
                raise Exception('Wrong type')
            return cmd()
