import json
from classes.Utils import Utils
from classes.Session import Session


class Req:
    events = None
    data = None
    session = None

    def __init__(self, event, data, sess):
        self.events = event
        self.data = data
        self.session = sess

    @staticmethod
    def init_from_json(json_string, sess):
        json_obj = Utils.convert_json_to_dict(json_string)
        if 'event' not in json_obj or 'data' not in json_obj:
            raise Exception('Incorrect JSON format')
        return Req(json_obj['event'], json_obj['data'], sess)

    @staticmethod
    def init_from_get_request(req_handler):
        sess = Session.start(req_handler)
        event = Req.prepare_request_path(req_handler.path_args[0])
        data = Req.prepare_request_args(req_handler.request.arguments)
        if event.__len__() < 1:
            raise Exception('Incorrect Request format')
        return Req(event, data, sess)

    @staticmethod
    def make_response(data=None):
        print("Response:", data)
        return json.dumps({
            "error": False,
            "data": data
        })

    @staticmethod
    def make_error_response(msg):
        print("Error Response:", msg)
        return json.dumps({
            "error": True,
            "msg": msg
        })

    @staticmethod
    def prepare_request_args(req_args):
        res_list = {}
        for k in req_args:
            res_list[k] = req_args[k][0].decode("UTF-8")
        return res_list

    @staticmethod
    def prepare_request_path(req_path):
        return req_path.split("/")

