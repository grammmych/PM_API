import tornado.ioloop
import tornado.web
import handlers.WsHandler as Ws
import classes.Sessions as SESS


class MainHandler(tornado.web.RequestHandler):
    sessions = SESS.Sessions()

    def data_received(self, chunk):
        print('MainHandler', 'data_receiver')
        pass

    def get(self):
        self.sessions.start(self)
        self.write(open('private/index.html', 'r').read())


class ApiHandler(tornado.web.RequestHandler):
    def data_received(self, chunk):
        pass

    def get(self, *args, **kwargs):
        print(args, kwargs)
        self.write('API: ')


def make_app():
    return tornado.web.Application([
        (r"/ws", Ws.WsHandler),
        (r"/api/(.*)", ApiHandler),
        (r"/", MainHandler),
        (r"/(.*)", tornado.web.StaticFileHandler, {'path': 'private'})
    ], cookie_secret="PM_SECRET_KEY")


if __name__ == "__main__":
    app = make_app()
    app.listen(4200)
    tornado.ioloop.IOLoop.current().start()
