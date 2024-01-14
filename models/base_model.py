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
    def __init__(self, *args, **kwargs):
            if kwargs:
                for key, value in kwargs.items():
                    if key == '__class__':
                        continue
                    elif key in ('created_at', 'updated_at'):
                        # Convert string to datetime object
                        setattr(self, key, datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f"))
                    else:
                        setattr(self, key, value)
            else:
                self.id = str(uuid.uuid4())
                self.created_at = datetime.now()
                self.updated_at = datetime.now()
                    
            """
            Private instance attribute: height and width
            """

    def __str__(self):
        return (f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}")

    def save(self):
        self.updated_at = datetime.now()

    def to_dict(self):
        dict_repr = self.__dict__.copy()
        dict_repr['__class__'] = self.__class__.__name__

        # Convert datetime objects to string in ISO format
        dict_repr['created_at'] = self.created_at.isoformat()
        dict_repr['updated_at'] = self.updated_at.isoformat()

        return dict_repr