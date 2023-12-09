#!/usr/bin/env python3
''' Program that contains the entry point of the command interpreter '''
import cmd
from models import storage
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "

    def do_create(self, arg):
        """Create a new instance of BaseModel"""
        if not arg:
            print("** class name missing **")
            return

        try:
            new_instance = eval(arg)()
            new_instance.save()
            print(new_instance.id)
        except NameError:
            print("** class doesn't exist **")

    def do_show(self, arg):
        """Show the string representation of an instance"""
        if not arg:
            print("** class name missing **")
            return

        args = arg.split()
        class_name = args[0]

        # Check if the class name exists in the registered classes
        if class_name not in storage.all().keys():
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        key = f"{class_name}.{args[1]}"

        objects = storage.all()[class_name]
        if key not in objects:
            print("** no instance found **")
        else:
            print(objects[key])

    def do_destroy(self, arg):
        """Delete an instance based on the class name and id"""
        if not arg:
            print("** class name missing **")
            return

        args = arg.split()

        # Check if the class name exists in the registered classes
        if args[0] not in storage.all():
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        key = "{}.{}".format(args[0], args[1])
        objects = storage.all()

        if key not in objects:
            print("** no instance found **")
        else:
            del objects[key]
            storage.save()

    def do_all(self, arg):
        """Print string representation of all instances"""
        class_name = arg.split()[0] if arg else None

        objects = storage.all()

        if not class_name:
            print([str(obj) for obj in objects.values()])
        else:
            if class_name not in objects:
                print("** class doesn't exist **")
            else:
                print([str(obj) for obj in objects[class_name]])

    def do_update(self, arg):
        """Update an instance based on the class name and id"""
        args = arg.split()

        if not args:
            print("** class name missing **")
            return

        class_name = args[0]
        if class_name not in storage.all():
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        instance_id = args[1]
        key = f"{class_name}.{instance_id}"
        objects = storage.all()

        if instance_id not in [k.split('.')[1] for k in objects.get(class_name, {}).keys()]:
            print("** no instance found **")
            return

        if len(args) < 3:
            print("** attribute name missing **")
            return

        attribute_name = args[2]
        if len(args) < 4:
            print("** value missing **")
            return

        attribute_value_str = args[3]
    
        # Handle the case where a string argument has a space between double quotes
        if attribute_value_str[0] == '"' and attribute_value_str[-1] == '"':
            attribute_value_str = attribute_value_str[1:-1]

        # Get the class of the instance
        instance_class = objects[key].__class__

        # Check if the attribute is valid and can be updated
        if attribute_name in ["id", "created_at", "updated_at"]:
            print("** can't update attribute **")
            return

        # Get the attribute type from the class
        attribute_type = type(getattr(instance_class(), attribute_name, None))

        # Cast the attribute value to the correct type
        try:
            attribute_value = attribute_type(attribute_value_str)
        except (ValueError, TypeError):
            print("** invalid value **")
            return

        # Update the attribute and save the changes
        setattr(objects[key], attribute_name, attribute_value)
        storage.save()

    def do_quit(self, arg):
        """Quit command to exit the program
        """
        return True

    def do_EOF(self, arg):
        """EOF command to exit the program
        """
        return True

    def emptyline(self):
        """Do nothing on an empty line"""
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()
