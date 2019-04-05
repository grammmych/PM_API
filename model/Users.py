from model.BaseModel import BaseModel
from peewee import *


class Users(BaseModel):
    user_id = IntegerField(primary_key=True)
    login = TextField()
    passwd = TextField()
    email = TextField()
    crt_date = DateField()

    @staticmethod
    def get_user_for_login(login, password):
        try:
            return Users.get(Users.login == login, Users.passwd == password)
        except DoesNotExist:
            raise Exception("User not found!")
