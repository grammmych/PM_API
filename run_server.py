import tornado.ioloop
import tornado.web
import handlers.WsHandler as Ws
import classes.Session as SESS


class MainHandler(tornado.web.RequestHandler):

    def data_received(self, chunk):
        pass

    def get(self):
        SESS.Session.start(self)
        self.write(open('private/index.html', 'r').read())


class ApiHandler(tornado.web.RequestHandler):
    def data_received(self, chunk):
        pass

    def get(self, *args, **kwargs):
        print('API: Get', args, kwargs)
        if args[0] == 'get_user_config':
            pass
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
