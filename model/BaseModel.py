from peewee import *

db = MySQLDatabase('pm_db', user='pm_user', password='pmuserpass', host='127.0.0.1', port=8989)


class BaseModel(Model):
    class Meta:
        database = db
