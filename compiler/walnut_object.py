# WalnutObject module
# This module stores the name and to which walnut class does the
# object belongs to.
#
# attributes
#
# walnut_class: the class to which the objects belongs to.
# name: the id of the walnut object
#

import sys
class WalnutObject:
    def __init__(self, walnut_class):
        self.walnut_class = walnut_class
        self.name = ''
