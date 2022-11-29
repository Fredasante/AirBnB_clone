#!/usr/bin/python3
"""
The Console Module
Serves as the entry point of our command interpreter.
"""


import cmd
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """Our subclass of the Cmd class"""
    prompt = '(hbnb) '
	
    def do_quit(self, arg):
        """Exits the shell"""
        return True

    def help_quit(self):
        print("Quit command to exit the program")

    def emptyline(self):
        """Overrides the emptyline method"""
        pass

    do_EOF = do_quit
    help_EOF = help_quit

    def do_create(self, args):
        """ Creates a new instance of BaseModel, saves it
        (to the JSON file) and prints the id
        """
        if len(args) == 0:
            print("** class name missing **")
            return
        try:
            arg_list = args.split(" ")
            instance = eval(arg_list[0])() 
            instance.save()
            print(instance.id)
        except:
            print("** class doesn't exist **")

    def do_show(self, args):
        """Prints the string representation of an instance based
        on the class name and id
        """
        arg_list = args.split(" ")
        if len(arg_list) == 0:
            print("** class name missing **")
            return
        if len(arg_list) == 1:
            print("** instance id missing **")
            return
        storage = FileStorage()
        storage.reload()
        obj_dict = storage.all()
        arg_list = args.split(" ")
        try:
            eval(arg_list[0])
        except NameError:
            print("** class doesn't exist **")
            return
        key = str(arg_list[0]) + "." + str(arg_list[1])
        if key not in obj_dict:
            print("** no instance found **")
        else:
            print(obj_dict[key])

    def do_destroy(self, args):
        """Deletes an instance based on the class name and id"""
        args = args.split(" ")
        if len(args) == 0:
            print("** class name missing **")
            return
        if len(args) == 1:
            print("** instance id missing **")
            return
        storage = FileStorage()
        storage.reload()
        obj_dict = storage.all()
        class_name = args[0]
        class_id = args[1]
        try:
            eval(class_name)
        except NameError:
            print("** class doesn't exist **")
            return
        key = class_name + "." + class_id
        try:
            del obj_dict[key]
        except KeyError:
            print("** no instance found **")
        storage.save()
    
    def do_all(self, args):
        """Prints all string representation of all instances based or
        not on the class name
        """
        storage = FileStorage()
        storage.reload()
        if args:
            arg_list = args.split(" ")
            try:
                eval(arg_list[0])
            except NameError:
                print("** class doesn't exist **")
                return
            obj_list = [str(obj) for key, obj in storage.all().items()
                     if type(obj).__name__ == arg_list[0]]
            print(obj_list)
        else:
            obj_list = [str(obj) for key, obj in storage.all().items()]
            print(obj_list)

    def do_update(self, args):
        """Updates an instance based on the class name and id by
        adding or updating attribute
        """
        storage = FileStorage()
        storage.reload()
        objects = storage.all()
        arg_list = args.split(" ")
        if len(arg_list) == 0:
            print("** class name missing **")
            return
        elif len(arg_list) == 1:
            print("** instance id missing **")
            return
        elif len(arg_list) == 2:
            print("** attribute name missing **")
            return
        elif len(arg_list) == 3:
            print("** value missing **")
            return
        try:
            eval(arg_list[0])
        except NameError:
            print("** class doesn't exist **")
            return
        key = str(arg_list[0]) + "." + str(arg_list[1])
        try:
            value = objects[key]
        except KeyError:
            print("** no instance found **")
            return
        try:
            attr_type = type(getattr(value, arg_list[2]))
            arg_list[3] = attr_type(arg_list[3])
        except AttributeError:
            pass
        setattr(value, arg_list[2], arg_list[3])
        value.save()        


if __name__ == '__main__':
    HBNBCommand().cmdloop()
