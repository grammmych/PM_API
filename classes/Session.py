import uuid
import datetime
from model.Sessions import Sessions
import peewee
import json
from classes.Req import Req


class Session:
    SESSION_LIFETIME = 30
    sess_token = None
    sess_data = None

    def __init__(self, token, data):
        if type(token) is not str and len(token) != 32:
            token = uuid.uuid4().hex
        self.sess_token = token
        self.sess_data = data

    @staticmethod
    def start(cli):
        token = cli.get_secure_cookie('token').decode('UTF-8')
        if token:
            try:
                Sessions.delete().where(Sessions.last_active <= datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
                db_sess = Sessions.get(Sessions.session_key == token)
            except peewee.DoesNotExist:
                db_sess = None
            except Exception as e:
                print('Get current session from DB Error:', e.__str__())
                db_sess = None

            if db_sess is None:
                print('crt_sess if no in DB ->>')
                sess = Session.create_session({})
                cli.set_secure_cookie('token', sess.sess_token)
            else:
                print('Get sess from DB:', db_sess.session_key)
                sess = Session.get_session(db_sess.session_key, Req.convert_json_to_dict(db_sess.session_data))
        else:
            print('crt_sess ->>')
            sess = Session.create_session({})
            cli.set_secure_cookie('token', sess.sess_token, 1)

        sess.update_session()
        print('Token', sess.sess_token)
        print('Sess:', sess)

    @staticmethod
    def create_session(data):
        return Session(uuid.uuid4().hex, data)

    @staticmethod
    def get_session(token, data):
        return Session(token, data)

    def update_session(self):
        curr_date = (datetime.datetime.now() + datetime.timedelta(minutes=Session.SESSION_LIFETIME))\
            .strftime("%Y-%m-%d %H:%M:%S")
        print('Update Time', curr_date)
        Sessions.insert(
            session_key=self.sess_token,
            session_data=json.dumps(self.sess_data),
            last_active=curr_date
        ).on_conflict('replace').execute()

    def get_sess_var(self, var_name):
        if self.is_set_sess_var(var_name):
            return self.sess_data[var_name]
        return None

    def set_sess_var(self, var_name, var_value):
        self.sess_data[var_name] = var_value

    def del_sess_var(self, var_name):
        if self.is_set_sess_var(var_name):
            del self.sess_data[var_name]

    def is_set_sess_var(self, var_name):
        return var_name in self.sess_data
