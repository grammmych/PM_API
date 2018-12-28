class AbstractProc:

    def __init__(self, req):
        self.req = req

    @property
    def event(self):
        return self.req.event

    @property
    def data(self):
        return self.req.data
