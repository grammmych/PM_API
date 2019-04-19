import json
from tornado.template import Loader
from controller.AbstractController import AbstractController
from model.UsersModel import Users
from model.ConfirmDataModel import Confirm_Data


class Authentication(AbstractController):

    def get_user_config(self):
        print("Exec get_user_config")
        if self.request.session.is_set_sess_var("user_data"):
            user_data = self.request.session.get_sess_var("user_data")
            return {
                "name": user_data["login"]
            }
        else:
            return None

    def login(self):
        print("Exec login")
        if "username" not in self.request.data \
                or type(self.request.data["username"]) != str \
                or self.request.data["username"].strip() == "" \
                or "password" not in self.request.data \
                or type(self.request.data["password"]) != str \
                or self.request.data["password"].strip() == "":
            raise Exception("Username or password are incorrect!")

        try:
            users_query = Users.get_user_for_login(self.request.data["username"], self.request.data["password"])
        except Exception as e:
            raise e
        users_query.passwd = ""
        self.request.session.set_sess_var("user_data", {
            "user_id": users_query.user_id,
            "login": users_query.login
        })
        return "Login Success!"

    def logout(self):
        print("Exec logout")
        self.request.session.del_sess_var("user_data")
        return "Logout success!"

    def registration(self):
        try:
            confirm_table = Confirm_Data()
            Confirm_Data.clear_expired_rows()
            print("RegData:", self.request.data)
            if not Users.is_valid_email(self.request.data["email"]):
                raise Exception("E-mail not valid")
            if not Users.check_email_and_username_unique(self.request.data["email"], self.request.data["login"]):
                raise Exception("Login or E-mail not unique")
            json_data = json.dumps(self.request.data)
            token = confirm_table.set_data(json_data)
            print("ConfirmDataSaved:", token)
            return "OK"
        except Exception as e:
            raise e

    def confirm_registration(self):
        try:
            print("ConfirmRegData:", self.request.data)
            Confirm_Data.clear_expired_rows()
            confirm_table = Confirm_Data()
            loader = Loader("templates")

            return loader.load("base.html").generate()
            return "OK"
        except Exception as e:
            raise e
