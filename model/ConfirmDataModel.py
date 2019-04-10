import datetime
import uuid
from model.BaseModel import BaseModel
from peewee import *


class Confirm_Data(BaseModel):
    token = TextField(primary_key=True)
    data = TextField()
    expire_date = DateField()

    @staticmethod
    def clear_expired_rows():
        Confirm_Data.delete().where(Confirm_Data.expire_date < datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

    def get_data_by_token(self, token):
        try:
            return self.get(self.token == token)
        except DoesNotExist:
            return None

    def set_data(self, data, timeout=30):
        token = uuid.uuid4().hex
        expire_date = (datetime.datetime.now() + datetime.timedelta(minutes=timeout)).strftime("%Y-%m-%d %H:%M:%S")
        try:
            confirm = self.insert(token=token, data=data, expire_date=expire_date).execute()
            return token
        except Exception as e:
            raise e
