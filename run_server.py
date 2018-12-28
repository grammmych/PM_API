import tornado.ioloop
import tornado.web
import handlers.WsHandler as Ws


class MainHandler(tornado.web.RequestHandler):
    def data_received(self, chunk):
        pass

    def get(self):
        if self.get_secure_cookie("token"):
            self.write(open('private/index.html', 'r').read())
        else:
            self.set_secure_cookie("token", "token_value")
            self.redirect("/")


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
    ], cookie_secret="my_data")


if __name__ == "__main__":
    app = make_app()
    app.listen(4200)
    tornado.ioloop.IOLoop.current().start()
