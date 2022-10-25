#!/usr/bin/python3
import cmd
from models.base_model import BaseModel



class HBNBCommand(cmd.Cmd):

    prompt: str = "(hbnb)  "

    __classes ={
    "BaseModel",
    "User",
    "State",
    "City",
    "Place",
    "Amenity",
    "Review"
    }

    def do_EOF(self, line):
        """EOF signal to exit the program."""
        print("")
        return True

    def do_quit(self, line):
        """Quit command to exit the program"""
        return True

    def emptyline(self):
        """Do nothing upon receiving an empty line."""
        pass

    def do_create(self, args):
        """Creates a new instance of BaseModel
        Args:
            arg(line):  BaseModel command
        """
        args_split = args.split()

        if (len(args_split) == 0):
            print("** class name missing **")
        elif (args_split[0] not in self.__classes):
            print("** class doesn't exist **")
        else:
            model = BaseModel()
            model.save()
            print(model.id)



if __name__ == '__main__':
    HBNBCommand().cmdloop()
