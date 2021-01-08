from pkg_resources import iter_entry_points


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
