from mongoengine import *
import datetime
import os

if "MONGO_URI" in os.environ:
    MONGO_URI = os.environ['MONGO_URI']
else:
    MONGO_URI = "localhost"
print(MONGO_URI,flush=True)

if "DB_NAME" in os.environ:
    DB_NAME = os.environ['DB_NAME']
else:
    DB_NAME = "database"

connect(DB_NAME, host=MONGO_URI)

class User(Document):
    username = StringField()
    password = StringField()    
    boolean_field = BooleanField(default=False)
    number = IntField(default=3)
    createdate = DateTimeField(default=datetime.datetime.utcnow)

class Clients(Document):
    users = ListField(ReferenceField(User))
    quantity = {"quantity":0}

class Healthcheck(Document):
    createdate = DateTimeField(default=datetime.datetime.utcnow)
    updatedate = DateTimeField()
