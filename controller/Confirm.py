import json
from controller.AbstractController import AbstractController
from model.ConfirmDataModel import Confirm_Data
from tornado.template import Loader


class Confirm(AbstractController):

    def registration(self):
        print("ConfReg:", self.request.data)
        if "t" not in self.request.data:
            raise Exception("There is no token in request")
        confirm_data_table = Confirm_Data()
        confirm = confirm_data_table.get_data_by_token(self.request.data["t"])
        if confirm is None:
            raise Exception("Confirm registration token not find")
        print("RegData:", )
        loader = Loader("templates")
        return loader.load("base.html").generate()
