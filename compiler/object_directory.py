# ObjectDirectory module:
# This module is in charge to have control over the declared objects
# in the current context, having them stored in a directory.
#
# arguments:
#
# objects: is the dictionary to store all objects of the context
# current_class: helper attribute in charge of semantic validation of the declaration of an object (giving the correct class name)
# current_object: helper method in charge to insert the correct object to the directory.
#
from walnut_object import WalnutObject
import sys
class ObjectDirectory:
    def __init__(self):
        self.objects = {}
        self.current_class = ''
        self.current_object = WalnutObject(None)

    # Name: add_object
    # This method is called when a new object declaration wants to take place.
    # The validation of the class name was given by the program engine, it
    # creates the WalnutObject with the class name and sets the helper attributes
    #
    # parameters
    # walnut_class: the name of the class to which the object will belong.
    #
    def add_object(self, walnut_class):
        obj = WalnutObject(walnut_class)
        self.current_class = walnut_class.name
        self.current_object = obj

    # Name: assign_object
    # This method is called after the first class name was validated,
    # it will assign the name of the object and insert it to the directory.
    #
    # parameters
    #
    # object_id: the name of the new object
    #
    def assign_object(self, object_id):
        self.current_object.name = str(object_id)
        self.objects[object_id] = {
            'obj' : self.current_object,
            'class' : self.current_object.walnut_class
        }

    # Name: validate_class_name
    # This method is in charge to validate that the first class name placed as declaration is the same as
    # the second one to which the object will call the initializer to.
    #
    # parameter
    #
    # class_name: class_name of the initializer method trying to be called.
    #
    # error_handle
    #
    # 1) returns if the name of the first class in the declaration does not match the second.
    #
    def validate_class_name(self, class_name):
        if self.current_class != class_name:
            print("Unexpected class name: " + str(class_name) + " in object declaration, expected: " + self.current_class)
            sys.exit()
