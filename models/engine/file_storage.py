#!/usr/bin/python3
import json
from models.base_model import BaseModel


class FileStorage:

    __file_path = "file.json"
    __objects = {}

    def all(self):
        return self.__objects

    def new(self, obj):
        key = f"{obj.__class__.__name__}, {obj.id}"
        self.__objects[key] = obj

    def save(self):
        data = {key: value.to_dict() for key, value in self.__objects.items()}
        with open(self.__file_path, 'w') as f:
            json.dump(data, f)

    def reload(self):
        try:
            with open(self.__file_path, 'r') as f:
                data = json.load(f)
                for key, value in data.items():
                    obj = eval(f"{value['__class__']}(**(value))")
                    self.__objects[key] = obj

        except FileNotFoundError:
            pass
