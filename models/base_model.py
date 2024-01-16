#!/usr/bin/python3
"""
import module
"""
import uuid
from datetime import datetime
import models


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
                    setattr(
                        self, key, datetime
                        .strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                        )
                else:
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)
            """
            Private instance attribute: height and width
            """

    def __str__(self):
        return f'[{self.__class__.__name__}] ({self.id}) {self.__dict__}'

    def save(self):
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        my_dict = {'__class__': self.__class__.__name__}
        for key, value in self.__dict__.items():
            if isinstance(value, datetime):
                my_dict[key] = value.isoformat()
            else:
                my_dict[key] = value
        return my_dict
