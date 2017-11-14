from walnut_object import WalnutObject
import sys
class ObjectDirectory:
    def __init__(self):
        self.objects = {}
        self.current_class = ''
        self.current_object = WalnutObject(None)

    def add_object(self, walnut_class):
        obj = WalnutObject(walnut_class)
        self.current_class = walnut_class.name
        self.current_object = obj

    def assign_object(self, object_id):
        self.current_object.name = str(object_id)
        self.objects.update({self.current_class : self.current_object})

    def validate_class_name(self, class_name):
        if self.current_class != class_name:
            print("Unexpected class name: " + str(class_name) + " in object declaration, expected: " + self.current_class)
            sys.exit()
