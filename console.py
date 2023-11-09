#!/usr/bin/python3


import cmd

class HBNBCommand(cmd.Cmd):
    '''HBNBCommand'''
    def do_quit(self, line):
        '''Quit command to exit the program'''
        return True
    
    def do_EOF(self, line):
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()
