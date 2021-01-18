
class BasicModel(dict):
    """docstring for BasicModel."""

    def __init__(self, **kwargs):
        super(BasicModel, self).__init__(kwargs)

    def check(self, key, kind=None):
        if kind is not None and key in self:
            return isinstance(self[key], kind)
        return key in self


class User(BasicModel):
    """docstring for User."""

    def userids_iter(self, api):
        ids = self.get('ids', [])
        for name, userid in ids:
            if name == api:
                yield userid

    def userids(self, api, first=True):
        if not first:
            return self.userids_iter(api)
        for apiname, userid in self.get('ids', []):
            if apiname == api:
                if first:
                    return userid


class Message(BasicModel):
    """docstring for Chat."""
    pass


class Chat(BasicModel):
    """docstring for Chat."""
    pass
