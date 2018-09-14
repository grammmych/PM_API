import tornado.ioloop
import tornado.web


class MainHandler(tornado.web.RequestHandler):
    def data_received(self, chunk):
        pass

    def get(self):
        self.write(open('private/index.html', 'r').read())


class ApiHandler(tornado.web.RequestHandler):
    def data_received(self, chunk):
        pass

    def get(self, *args, **kwargs):
        print(args, kwargs)
        self.write('API: ')


def make_app():
    return tornado.web.Application([
        (r"/api/(.*)", ApiHandler),
        (r"/", MainHandler),
        (r'/(.*)', tornado.web.StaticFileHandler, {'path': 'private'}),
    ])


if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()
