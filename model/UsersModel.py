from model.BaseModel import BaseModel
from peewee import *
import re


class Users(BaseModel):
    user_id = IntegerField(primary_key=True)
    login = TextField()
    passwd = TextField()
    email = TextField()
    crt_date = DateField()

    @staticmethod
    def get_user_for_login(email, password):
        try:
            return Users.get(Users.email == email, Users.passwd == password)
        except DoesNotExist:
            raise Exception("User not found!")

    @staticmethod
    def check_email_and_username_unique(email, username):
        result = Users.select().where(
            (Users.email == email) |
            (Users.login == username)
        )
        return False if(len(result)) else True

    @staticmethod
    def is_valid_email(email):
        if len(email) > 7:
            if re.match(r"^[A-Za-z0-9\.\+_-]+@[A-Za-z0-9\._-]+\.[a-zA-Z]*$", email) is not None:
                return True
            else:
                return False
        return False
