
class BasicModel:
    """docstring for BasicModel."""

    def __init__(self, **kwargs):
        super(BasicModel, self).__init__()
        self.kwargs = kwargs

    def __str__(self):
        return '{}'.format(self.kwargs)


class User(BasicModel):
    """docstring for User."""
    pass


class Message(BasicModel):
    """docstring for Chat."""
    pass


class Chat(BasicModel):
    """docstring for Chat."""
    pass
