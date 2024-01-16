#!/usr/bin/python3
"""
Contains the definition of 'HBNBCommand' class.
"""
import cmd
from models.base_model import BaseModel
from models.user import User
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.amenity import Amenity


class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb)'
    classes = (
        'BaseModel',
        'User',
        'City',
        'Place',
        'Review',
        'State',
        'Amenity'
        )

    def do_create(self, line):
        if line:
            if line not in HBNBCommand.classes:
                print("** class doesn't exist **")
            else:
                instance = eval(f"{line}()")
                instance.save()
                print(instance.id)
        else:
            print("** class name missing **")

    def to_show(self, line):
        if line:
            if line not in HBNBCommand.classes:
                print("** class doesn't exist **")
            else:
                instance = globals()[__class__.__name__].id

    def emptyline(self):
        pass

    def do_EOF(self, line):
        return True

    def do_quit(self, arg):
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()
