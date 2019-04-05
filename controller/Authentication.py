from controller.AbstractController import AbstractController
from model.Users import Users


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
                or type(self.request.data["username"]) != str\
                or self.request.data["username"].strip() == ""\
                or "password" not in self.request.data \
                or type(self.request.data["password"]) != str\
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
