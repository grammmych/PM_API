import tornado.ioloop
import tornado.web
import handlers.WsHandler as Ws
from classes.Session import Session
from classes.Req import Req
from classes.ProcMain import ProcMain
from controller.Confirm import Confirm


class MainHandler(tornado.web.RequestHandler):

    def data_received(self, chunk):
        pass

    def get(self):
        print("MainHandler ---->>>>")
        Session.start(self)
        self.write(open('private/index.html', 'r').read())


class ConfirmHandler(tornado.web.RequestHandler):

    def data_received(self, chunk):
        pass

    def get(self, *args, **kwargs):
        print("ConfirmHandler ---->>>>")
        try:
            req = Req.init_from_get_request(self)
            req.events.insert(0, "confirm")
            conf = Confirm(req)
            self.write(conf.proc())
        except Exception as e:
            print("ConfirmError:", e.__str__())
            self.write("Error")
            #self.redirect("/")


class ApiHandler(tornado.web.RequestHandler):
    def data_received(self, chunk):
        pass

    def get(self, *args, **kwargs):
        print("ApiGETHandler ---->>>>")
        try:
            req = Req.init_from_get_request(self)
            proc = ProcMain(req)
            self.write(proc.processing())
        except Exception as e:
            self.write(Req.make_error_response(e.__str__()))

    def post(self, *args, **kwargs):
        print("ApiPOSTHandler ---->>>>")
        try:
            req = Req.init_from_post_request(self)
            print("PreparedReq:", req.events, req.data)
            proc = ProcMain(req)
            self.write(proc.processing())
        except Exception as e:
            self.write(Req.make_error_response(e.__str__()))


def make_app():
    return tornado.web.Application([
        (r"/ws", Ws.WsHandler),
        (r"/api/(.*)", ApiHandler),
        (r"/confirm/(.*)", ConfirmHandler),
        (r"/(.*\..*)", tornado.web.StaticFileHandler, {'path': 'private'}),
        (r"/.*", MainHandler)
    ], cookie_secret="PM_SECRET_KEY")


if __name__ == "__main__":
    app = make_app()
    app.listen(4200)
    tornado.ioloop.IOLoop.current().start()
