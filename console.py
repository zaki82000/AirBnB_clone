#!/usr/bin/python3
"""
Contains the definition of 'HBNBCommand' class.
"""
import cmd


class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb)'

    def do_quit(self, arg):
        return True

    def do_EOF(self, line):
        return True

    def emptyline(self):
        return cmd.Cmd.emptyline(self)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
