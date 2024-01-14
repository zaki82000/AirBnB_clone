#!/usr/bin/python3
import uuid
from datetime import datetime


class BaseModel:
    def __init__(self, *args, **kwargs):
        self.id = uuid.uuid4()
        self.created_at = datetime.now()
        self.updated_at = self.created_at

    @property
    def uuid(self):
        return str(self.id)

    def __str__(self):
        return (f"[{self.__class__.__name__}] ({self.uuid}) {self.__dict__}")

    def save(self):
        self.updated_at = datetime.now()

    def to_dict(self):
        obj = self.__dict__.copy()
        obj['created_at'] = self.created_at.strftime("%Y-%m-%dT%H:%M:%S.%f")
        obj['id'] = self.uuid
        obj['updated_at'] = self.updated_at.strftime("%Y-%m-%dT%H:%M:%S.%f")
        obj['__class__'] = self.__class__.__name__
        return obj
