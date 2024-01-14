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
            self.created_at = datetime.now()
            self.id = str(uuid.uuid4())
            self.updated_at = self.created_at
            """
            Private instance attribute: height and width
            """

    def __str__(self):
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        self.updated_at = datetime.now()

    def to_dict(self):
        return  {
        "my_number": self.my_number,
        "name": self.name,
        "__class__": self.__class__.__name__,
        "created_at": self.created_at.isoformat(),
        "id": self.id,
        "updated_at": self.updated_at.isoformat(),
    }