#!/usr/bin/python3


import cmd
from models.base_model import BaseModel
from models import storage

class HBNBCommand(cmd.Cmd):
    '''HBNBCommand'''
    prompt = "(hbnb) "
    def do_create(self, line):
        '''Create command to create a new instance of BaseModel'''
        if not line:
            print('** class name missing **')
            return
        try:
            class_name = globals()[line[0]]
            obj1 = class_name()
            obj1.save()
            print(obj1.id)
        except KeyError:
            print("** class doesn't exist **")
            return

    def do_show(self, line):
        '''Prints the string representation of an instance based on the class name and id'''
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
        '''Deletes an instance based on the class name and id'''
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
        '''Prints all string representation of all instances based or not on the class name'''
        

    def do_quit(self, line):
        '''Quit command to exit the program'''
        return True
    
    def do_EOF(self, line):
        '''Exit the program'''
        print("")
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()
