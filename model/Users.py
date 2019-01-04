from model.BaseModel import BaseModel
from peewee import *


class Users(BaseModel):
    user_id = IntegerField(primary_key=True)
    login = TextField()
    passwd = TextField()
    email = TextField()
    crt_date = DateField()
