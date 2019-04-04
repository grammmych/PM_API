from controller.AbstractController import AbstractController


class Authentication(AbstractController):

    def get_user_config(self):
        print("Exec get_user_config")
        if self.request.session.is_set_sess_var("user_data"):
            pass
        else:
            return None
