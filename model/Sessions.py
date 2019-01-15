from model.BaseModel import BaseModel
from peewee import *


class Sessions(BaseModel):
    session_key = CharField(primary_key=True)
    session_data = CharField()
    last_active = DateTimeField()
