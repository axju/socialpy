from pkg_resources import iter_entry_points

from socialpy.commands.generic import BasicConfig, BasicCommand


def iter_entry_points_names(group):
    for enp in iter_entry_points(group=group):
        yield enp.name


def iter_entry_points_load(group):
    for enp in iter_entry_points(group=group):
        yield enp.name, enp.load()


def get_entry_point(group, name):
    for enp in iter_entry_points(group=group):
        if name == enp.name:
            return enp.load()


def get_api_config(name):
    conf = get_entry_point('socialpy.configs', name)
    if isinstance(conf, dict):
        return BasicConfig(values=conf)
    elif issubclass(conf, BasicConfig):
        return conf()
    else:
        raise Exception('Wrong type')


def get_cli_command(name):
    cmd = get_entry_point('socialpy.commands', name)
    if not issubclass(cmd, BasicCommand):
        raise Exception('Wrong type')
    return cmd()
