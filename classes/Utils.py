import json


class Utils:

    @staticmethod
    def convert_json_to_dict(str_json):
        if str_json[0] == "\"":
            str_json = json.loads(str_json)
        return json.loads(str_json)
