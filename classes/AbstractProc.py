class AbstractProc:

    def __init__(self, req):
        self.req = req

    @property
    def events(self):
        return self.req.events

    @property
    def data(self):
        return self.req.data
