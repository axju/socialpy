from socialpy.gateway import Gateway

class Schedule0x01:

    def __init__(self, posts, dt):
        self.gateway = Gateway()
        self.posts = posts
        self.dt = dt

    def run(self):
        pass
