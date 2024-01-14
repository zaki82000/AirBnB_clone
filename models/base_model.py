#!/usr/bin/python3
"""
import module
"""
import uuid
from datetime import datetime


class BaseModel:
    """
    class BaseModel that defines all common attributes/methods for other clases
    """
    def __init__(self):
            self.updated_at = datetime.now()
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            
            """
            Private instance attribute: height and width
            """

    def __str__(self):
        return (f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}")

    def save(self):
        self.updated_at = datetime.now()

    def to_dict(self):
        obj = self.__dict__.copy()
        obj['__class__'] = self.__class__.__name__
        obj['created_at'] = self.created_at.strftime("%Y-%m-%dT%H:%M:%S.%f")
        obj['id'] = self.id
        obj['updated_at'] = self.updated_at.strftime("%Y-%m-%dT%H:%M:%S.%f")
        return obj
