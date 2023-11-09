#!/usr/bin/python3


import cmd
from models.base_model import BaseModel

class HBNBCommand(cmd.Cmd):
    '''HBNBCommand'''
    def do_create(self, line):
        '''Create command to create a new instance of BaseModel'''
        if not line:
            print('** class name missing **')
        else:
            try:
                class_name = globals()[line]
                obj1 = class_name()
                obj1.save()
                print(obj1.id)
            except KeyError:
                print("** class doesn't exist **")

    def do_show(self, line):
        '''Prints the string representation of an instance based on the class name and id'''
        if not line:
            print('** class name missing **')
        else:
            try:
                words = line.split()
                class_name = words[0]
                if len(words) < 2:
                    print('** instance id missing **')
                else:
                    id = words[1]
                    model_class = globals()[class_name]
                    obj = None
                    if id in model_class.globals()[id]:
                        obj = model_class.globals()[id]
                    if obj is not None:
                        print(obj)
                    else:
                        print('** no instance found **')
                    
            except KeyError:
                print("** class doesn't exist **")

    def do_quit(self, line):
        '''Quit command to exit the program'''
        return True
    
    def do_EOF(self, line):
        '''Exit the program'''
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()
