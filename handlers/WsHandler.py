import tornado.websocket
import classes.Req as r
import classes.ProcMain as p


class Client:
    def __init__(self, conn):
        self.conn = conn

    def send_msg(self, msg):
        self.conn.write_message(msg)


class Clients:
    clients = []

    def add_client(self, conn):
        pass


class WsHandler(tornado.websocket.WebSocketHandler):
    clients = Clients()

    def data_received(self, chunk):
        pass

    def open(self, *args, **kwargs):
        token = self.get_secure_cookie("token").decode("utf-8")
        print("WS opened", (token == 'token_value'))
        self.clients.add_client(conn=self)

    def on_message(self, message):
        print("WS Msg:", message)
        try:
            req = r.Req.init_from_json(message)
            proc = p.ProcMain(req)
            self.write_message(proc.processing())
        except Exception as err:
            print(err.__str__())

    def on_close(self):
        print('WS closed')
