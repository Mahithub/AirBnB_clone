#!/usr/bin/python3

from uuid import uuid4
from datetime import datetime

class BaseModel:
    def __init__(self):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = self.created_at

    def __str__(self):
        print("[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)):
    def save(self):
        self.updated_at = datetime.now()
    def to_dict(self):
        redict = self.__dict__.copy()
        redict['created_at'] = self.created_at.isoformat()
        redict['updated_at'] = self.updated_at.isoformat()
        redict['__class__'] = self.__class__.__name__
        return redict
