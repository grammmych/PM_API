import json


class Req:
    event = None
    data = None

    def __init__(self, event, data):
        self.event = event
        self.data = data

    @staticmethod
    def init_from_json(json_string):
        json_obj = Req.convert_json_to_dict(json_string)
        if 'event' not in json_obj or 'data' not in json_obj:
            raise Exception('Incorrect JSON format')
        return Req(json_obj['event'], json_obj['data'])

    @staticmethod
    def convert_json_to_dict(str_json):
        if str_json[0] == "\"":
            str_json = json.loads(str_json)
        return json.loads(str_json)

    @staticmethod
    def make_response(event, data=None):
        return json.dumps({
            "event": event,
            "data": data
        })
