import classes.AbstractProc
import classes.Req as R


class ProcMain(classes.AbstractProc.AbstractProc):
    def processing(self):
        if self.event == 'ping':
            return R.Req.make_response('pong')

