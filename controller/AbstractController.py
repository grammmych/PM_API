class AbstractController:
    request = None

    def __init__(self, request):
        self.request = request

    def proc(self):
        if hasattr(self, self.request.events[1]):
            fn = getattr(self, self.request.events[1])
            return fn()
        else:
            raise Exception('Method `%s` not find in `%s`' % (self.request.events[1], self.__class__.__name__))
