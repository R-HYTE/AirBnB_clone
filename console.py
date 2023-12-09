#!/usr/bin/env python3
''' Program that contains the entry point of the command interpreter '''
import cmd
import re

from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models import storage
from models.user import User


class HBNBCommand(cmd.Cmd):
    """
    Interactive command-line interface
    for managing instances in the Airbnb project.
    """
    prompt = "(hbnb) "
    valid_classes = {
            "BaseModel",
            "User",
            "State",
            "City",
            "Place",
            "Amenity",
            "Review"
    }

    def emptyline(self):
        """Do nothing upon receiving an empty line."""
        pass

    def default(self, arg):
        """Default behavior for cmd module when input is invalid"""
        print("*** Unknown syntax: {}".format(arg))

    def do_quit(self, arg):
        """Quit command to exit the program."""
        return True

    def do_EOF(self, arg):
        """EOF signal to exit the program."""
        print("")
        return True

    def parse_arguments(self, arg):
        """Parse the arguments from the input."""
        return arg.split()

    def do_create(self, arg):
        """Create a new class instance and print its id."""
        args = self.parse_arguments(arg)
        if not args:
            print("** class name missing **")
        elif args[0] not in self.valid_classes:
            print("** class doesn't exist **")
        else:
            instance = eval(args[0])()
            print(instance.id)
            storage.save()

    def do_show(self, arg):
        """
        Display the string representation of a class instance of a given id
        """
        args = self.parse_arguments(arg)
        obj_dict = storage.all()
        if not args or args[0] not in self.valid_classes:
            print("** class name missing **")
        elif len(args) < 2:
            print("** instance id missing **")
        elif f"{args[0]}.{args[1]}" not in obj_dict:
            print("** no instance found **")
        else:
            key = f"{args[0]}.{args[1]}"
            print(f"Object key: {key}")
            print(obj_dict[key])

    def do_destroy(self, arg):
        """Delete a class instance of a given id."""
        args = self.parse_arguments(arg)
        obj_dict = storage.all()

        if not args or args[0] not in self.valid_classes:
            print("** class name missing **")
        elif len(args) < 2:
            print("** instance id missing **")
        elif f"{args[0]}.{args[1]}" not in obj_dict:
            print("** no instance found **")
        else:
            del obj_dict[f"{args[0]}.{args[1]}"]
            storage.save()

    def do_all(self, arg):
        """Display string representations of all instances of a given class."""
        args = self.parse_arguments(arg)
        if args and args[0] not in self.valid_classes:
            print("** class doesn't exist **")
        else:
            obj_list = [
                    str(obj)
                    for obj in storage.all().values()
                    if not args or obj.__class__.__name__ == args[0]
            ]
            print(obj_list)

    def do_count(self, arg):
        """Retrieve the number of instances of a given class."""
        args = self.parse_arguments(arg)
        count = sum(
                1 for obj in storage.all().values()
                if args and obj.__class__.__name__ == args[0]
        )
        print(count)

    def do_update(self, arg):
        """Update a class instance of a given id with new attributes."""
        args = self.parse_arguments(arg)
        obj_dict = storage.all()

        if not args or args[0] not in self.valid_classes:
            print("** class name missing **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        if f"{args[0]}.{args[1]}" not in obj_dict:
            print("** no instance found **")
            return

        instance = obj_dict[f"{args[0]}.{args[1]}"]

        if len(args) < 3:
            print("** attribute name missing **")
            return

        if len(args) < 4:
            print("** value missing **")
            return

        attribute_name, attribute_value = args[2], args[3]
        setattr(
                instance,
                attribute_name,
                type(getattr(instance, attribute_name))(attribute_value)
        )
        storage.save()


if __name__ == "__main__":
    HBNBCommand().cmdloop()
