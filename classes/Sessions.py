import uuid
from model.Users import Users


class Sessions:
    sessions_store = []

    def start(self, cli):
        token = cli.get_secure_cookie("token")
        print("Token", token)
        user = Users.get(Users.user_id == 1)
        print('User:', user.login)

        # if not token:
        #     self.create_session(cli)
        # else:
        #     session = self.get_session(token)
        #     if session is None:
        #         self.create_session(cli)

    def create_session(self, cli):
        session = Session()
        self.add_session(session)
        cli.set_secure_cookie("token", session.key)

    def get_session(self, token):
        curr_session = None
        for sess in self.sessions_store:
            if sess.key == token:
                curr_session = sess
        return curr_session

    def add_session(self, new_session):
        self.sessions_store.append(new_session)


class Session:
    key = None
    value = None

    def __init__(self):
        self.key = uuid.uuid4().hex
