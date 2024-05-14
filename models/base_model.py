#!/usr/bin/python3

import models
from uuid import uuid4
from datetime import datetime

class BaseModel:
    def __init__(self, *args, **kwargs):
        tform = "%Y-%m-%dT%H:%M:%S.%f"
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        if len(kwargs != 0):
            for k, v in kwargs.items():
                if k == "created_at" or k == "updated_at":
                    self.__dict__[k] = datetime.strptime(v, tform)
                else:
                    self.__dict__[k] = v
        else:
            models.storage.new(self)




    def __str__(self):
        print("[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)):
    def save(self):
        self.updated_at = datetime.now()
    def to_dict(self):
        redict = self.__dict__.copy()
        redict["created_at"] = self.created_at.isoformat()
        redict["updated_at"] = self.updated_at.isoformat()
        redict["__class__"] = self.__class__.__name__
        return redict
