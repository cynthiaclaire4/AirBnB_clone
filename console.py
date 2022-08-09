#!/usr/bin/python3
'''console'''


import cmd
import shlex
import welcome
from models.engine.file_storage import FileStorage
from models.engine.load_engine import load_engine
from datetime import datetime
import models
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


class HBNBCommand(cmd.Cmd):
    """ HBNB console """
    prompt = '(hbnb) '

    def do_EOF(self, arg):
        """Exits console"""
        return True

    def emptyline(self):
        """ overwriting the emptyline method """
        return False

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_create(self, arg):
        '''creates new instance of a class'''
        if len(arg) == 0:
            welcome.missing()
            return
        try:
            arg = shlex.split(arg)
            instance = eval(arg[0])()
            instance.save()
            print(instance.id)
        except NameError:
            welcome.cls_d_exist()
            return

    def do_show(self, arg):
        """Prints an instance as a string based on the class and id"""
        arg = shlex.split(arg)
        if len(arg) == 0:
            welcome.missing()
            return
        if len(arg) == 1:
            welcome.idmissing()
            return
        available_obj = load_engine()
        try:
            eval(arg[0])
        except NameError:
            welcome.cls_d_exist()
            return
        key = arg[0] + "." + arg[1]
        try:
            print(available_obj[key])
        except KeyError:
            welcome.no_instance()
            return

    def do_destroy(self, arg):
        '''Deletes instance based on class and id'''
        arg = shlex.split(arg)
        if len(arg) == 0:
            welcome.missing()
            return
        if len(arg) == 1:
            welcome.idmissing()
            return
        available_obj = load_engine()
        input_name = arg[0]
        input_id = arg[1]
        try:
            eval(input_name)
        except NameError:
            welcome.cls_d_exist()
            return
        key = input_name + "." + input_id
        try:
            return_val = available_obj[key]
            del return_val
        except KeyError:
            welcome.no_instance()
            return

    def do_all(self, arg):
        '''prints string representation of instance'''
        # arg = shlex.split(arg)
        available_obj = load_engine()
        return_list = list()

        try:
            if len(arg) != 0:
                eval(arg)
        except NameError:
            welcome.cls_d_exist()
            return
        for key, val in available_obj.items():
            if len(arg) == 0:
                return_list.append(val)
            else:
                if type(val) is eval(arg):
                    return_list.append(val)
        print(return_list)

    def do_update(self, arg):
        """Update an instance based on the class name, id, attribute & value"""
        arg = shlex.split(arg)
        available_obj = load_engine()
        if len(arg) == 0:
            welcome.missing()
            return
        elif len(arg) == 1:
            welcome.idmissing()
            return
        elif len(arg) == 2:
            print("** attribute name missing **")
            return
        elif len(arg) == 3:
            print("** value missing **")
            return
        try:
            eval(arg[0])
        except NameError:
            welcome.cls_d_exist()
            return
        key = arg[0] + "." + arg[0]
        try:
            obj_value = available_obj[key]
        except KeyError:
            welcome.no_instance()
            return
        try:
            type_attr = type(getattr(obj_value, arg[2]))
            arg[3] = type_attr(arg[3])
        except AttributeError:
            pass
        setattr(obj_value, arg[2], arg[3])
        obj_value.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
