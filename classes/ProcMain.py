import classes.AbstractProc
from classes.Req import Req
from controller.Authentication import Authentication


class ProcMain(classes.AbstractProc.AbstractProc):
    def processing(self):
        try:
            main_event = self.events[0]
            if main_event == 'ping':
                response = Req.make_response('pong')
            elif main_event == 'auth':
                auth = Authentication(self.req)
                response = Req.make_response(auth.proc())
            else:
                raise Exception("Proc `%s` not found!" % main_event)
            return response
        except Exception as e:
            return Req.make_error_response(e.__str__())
