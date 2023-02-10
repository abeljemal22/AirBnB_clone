#!/usr/bin/python3

"""

This is the console base for the unit

"""

import cmd

from models.base_model import BaseModel

from models import storage

import json

import shlex

from models.user import User

from models.state import State

from models.city import City

from models.amenity import Amenity

from models.place import Place

from models.review import Review





class HBNBCommand(cmd.Cmd):

        """ Holberton command prompt to access models data """

            prompt = '(hbnb) '

                my_dict = {

                                "BaseModel": BaseModel,

                                        "User": User,

                                                "State": State,

                                                        "City": City,

                                                                "Amenity": Amenity,

                                                                        "Place": Place,

                                                                                "Review": Review

                                                                                            }



                    def do_nothing(self, arg):

                                """ Does nothing """

                                        pass



                                        def do_quit(self, arg):

                                                    """ Close program and saves safely data """

                                                            return True



                                                            def do_EOF(self, arg):

                                                                        """ Close program and saves safely data, when

                                                                                user input is CTRL + D

                                                                                        """

                                                                                                print("")

                                                                                                        return True



                                                                                                        def emptyline(self):

                                                                                                                    """ Overrides the empty line method """

                                                                                                                            pass



                                                                                                                            def do_create(self, arg):

                                                                                                                                        """ Creates a new instance of the basemodel class

                                                                                                                                                Structure: create [class name]

                                                                                                                                                        """

                                                                                                                                                                if not arg:

                                                                                                                                                                                print("** class name missing **")

                                                                                                                                                                                            return

                                                                                                                                                                                                my_data = shlex.split(arg)

                                                                                                                                                                                                        if my_data[0] not in HBNBCommand.my_dict.keys():

                                                                                                                                                                                                                        print("** class doesn't exist **")

                                                                                                                                                                                                                                    return

                                                                                                                                                                                                                                        new_instance = HBNBCommand.my_dict[my_data[0]]()

                                                                                                                                                                                                                                                new_instance.save()

                                                                                                                                                                                                                                                        print(new_instance.id)



                                                                                                                                                                                                                                                            def do_show(self, arg):

                                                                                                                                                                                                                                                                        """

                                                                                                                                                                                                                                                                                Prints the string representation of an instance

                                                                                                                                                                                                                                                                                        based on the class name and id

                                                                                                                                                                                                                                                                                                Structure: show [class name] [id]

                                                                                                                                                                                                                                                                                                        """

                                                                                                                                                                                                                                                                                                                tokens = shlex.split(arg)

                                                                                                                                                                                                                                                                                                                        if len(tokens) == 0:

                                                                                                                                                                                                                                                                                                                                        print("** class name missing **")

                                                                                                                                                                                                                                                                                                                                                    return

                                                                                                                                                                                                                                                                                                                                                        if tokens[0] not in HBNBCommand.my_dict.keys():

                                                                                                                                                                                                                                                                                                                                                                        print("** class doesn't exist **")

                                                                                                                                                                                                                                                                                                                                                                                    return

                                                                                                                                                                                                                                                                                                                                                                                        if len(tokens) <= 1:

                                                                                                                                                                                                                                                                                                                                                                                                        print("** instance id missing **")

                                                                                                                                                                                                                                                                                                                                                                                                                    return

                                                                                                                                                                                                                                                                                                                                                                                                                        storage.reload()

                                                                                                                                                                                                                                                                                                                                                                                                                                objs_dict = storage.all()

                                                                                                                                                                                                                                                                                                                                                                                                                                        key = tokens[0] + "." + tokens[1]

                                                                                                                                                                                                                                                                                                                                                                                                                                                if key in objs_dict:

                                                                                                                                                                                                                                                                                                                                                                                                                                                                obj_instance = str(objs_dict[key])

                                                                                                                                                                                                                                                                                                                                                                                                                                                                            print(obj_instance)
