#!/usr/bin/python3
"""Console"""


import cmd
from models.base_model import BaseModel
from models import storage
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """HBNBCommand"""
    prompt = "(hbnb) "

    __classes = {
        "BaseModel",
        "User",
        "State",
        "City",
        "Place",
        "Amenity",
        "Review"
    }

    def emptyline(self):
        """Handles the emptylines."""
        pass

    def do_create(self, line):
        """Create command to create a new instance of BaseModel"""
        if not line:
            print('** class name missing **')
            return
        words = line.split()
        try:
            class_name = globals()[words[0]]
            obj1 = class_name()
            obj1.save()
            print(obj1.id)
        except KeyError:
            print("** class doesn't exist **")
            return

    def do_show(self, line):
        """Prints the string representation of an instance
          based on the class name and id"""
        if not line:
            print('** class name missing **')
            return
        words = line.split()
        class_name = words[0]
        try:
            model_class = globals()[class_name]
        except KeyError:
            print("** class doesn't exist **")
            return
        if len(words) < 2:
            print('** instance id missing **')
            return
        id = words[1]
        show = "{}.{}".format(class_name, id)
        try:
            dobj = storage.all().get(show)
            if dobj:
                print(dobj)
            else:
                print("** no instance found **")
        except Exception:
            pass

    def do_destroy(self, line):
        """Deletes an instance based on the class name and id"""
        if not line:
            print('** class name missing **')
            return
        words = line.split()
        class_name = words[0]
        try:
            model_class = globals()[class_name]
        except Exception:
            print("** class doesn't exist **")
            return
        if len(words) < 2:
            print('** instance id missing **')
            return
        id = words[1]
        show = "{}.{}".format(class_name, id)
        try:
            dobj = storage.all().get(show)
            if dobj is None:
                print("** no instance found **")
                return
            else:
                data = storage.all()
                del data[show]
                storage.save()
        except Exception:
            pass

    def do_all(self, line):
        """Prints all string representation of all instances based or
          not on the class name"""
        words = line.split()
        if len(words) > 0:
            class_name = words[0]
            try:
                model_class = globals()[class_name]
            except KeyError:
                print("** class doesn't exist **")
                return
        else:
            class_name = None
        all_list = []
        for key, val in storage.all().items():
            if class_name is None or isinstance(val, model_class):
                all_list.append(val.__str__())
        print(all_list)

    def do_update(self, line):
        """Updates an instance based on the class name and
          id by adding or updating attribute"""
        if not line:
            print('** class name missing **')
            return
        words = line.split()
        class_name = words[0]
        if words[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
            return
        try:
            model_class = globals()[class_name]
        except KeyError:
            print("** class doesn't exist **")
            return
        if len(words) < 2:
            print('** instance id missing **')
            return
        id = words[1]
        show = "{}.{}".format(class_name, id)
        if show not in storage.all().keys():
            print("** no instance found **")
            return
        if len(words) == 2:
            print('** attribute name missing **')
            return
        if len(words) == 3:
            try:
                type(eval(words[2])) != dict
            except NameError:
                print('** value missing **')
                return
        if len(words) == 4:
            dictobj = storage.all()
            obj = dictobj[show]
            if words[2] in obj.__class__.__dict__.keys():
                valtype = type(obj.__class__.__dict__[words[2]])
                obj.__dict__[words[2]] = valtype(words[3])
            else:
                obj.__dict__[words[2]] = words[3]
        elif type(eval(words[2])) == dict:
            obj = storage.all()[show]
            for k, v in eval(words[2]).items():
                if (k in obj.__class__.__dict__.keys()) and \
                     (type(obj.__class__.__dict__[k]) in {str, int, float}):
                    valtype = type(obj.__class__.__dict__[k])
                    obj.__dict__[k] = valtype(v)
                else:
                    obj.__dict__[k] = v
        storage.save()

    def do_quit(self, line):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, line):
        """Exit the program"""
        print("")
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()
