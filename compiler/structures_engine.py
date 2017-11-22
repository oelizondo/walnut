# StructuresEngine module
# This module is in charge of the management of collections, this includes:
# 1) Setting the next memory available after the completion of the collection
# 2) Setting the correct number to be able to jump to the correct memory location
# 3) Setting the dimensions to the current collection
#
# attributes
#
# program_engine = this is used to obtain the variable information of the
#                  next to be current collection
# current_collection = helper attribute that will have the information of the variable
#                      to be modified.
# R = helper method that keeps track of the memory will occupy the collection
#
class StructuresEngine:
    def __init__(self, program_engine):
        self.program_engine = program_engine
        self.current_collection = None
        self.R = 1

    # Name: set_current_collection
    # This function registers a new collection being made as the current collection
    # for further semantic operations. This is called from the parser once
    # a bracket presents itself.
    #
    # parameter
    #
    # identifier: name of the new collection being set.
    #
    def set_current_collection(self, identifier):
        self.current_collection = self.program_engine.current_context.variable_directory.variables.get(identifier)

    # Name: inject_cell
    # This function adds a cell (object containing limit and k) to the current collection
    #
    # parameter
    #
    # limit: the upper limit of the collection
    #
    # error_handler
    #
    # 1) it returns when a limit is not set or below the permitted upper limit (must be bigger than 0)
    #
    def inject_cell(self, limit):
        if(limit != None and int(limit) <= 0):
            print("Out of bounds, cannot declare an array with: " + limit + ", value must be bigger than 0")
            sys.exit()
        self.current_collection['dimension'].append(self.generate_cell(int(limit)))
        self.update_r()

    # Name: generate_cell
    # This function returns the new generated cell to the inject cell function to
    # set it to the current_collection
    #
    # parameter
    #
    # limit: the upper limit of the collection
    #
    def generate_cell(self, limit):
        return {
            'limit': limit - 1,
            'k': 0
        }

    # Name: update_r
    # This function updates the calculation of of the total memory
    # needed for the collection.
    #
    def update_r(self):
        self.R = self.R * (self.current_collection['dimension'][-1]['limit'] + 1)

    # Name: fill_k
    # This function sets the jumps needed to do within each dimension to
    # access the correct memory location.
    #
    def fill_k(self):
        if len(self.current_collection['dimension']) == 1:
            self.current_collection['dimension'][0]['k'] = 0
        else:
            self.current_collection['dimension'][0]['k'] = self.R / int(self.current_collection['dimension'][0]['limit'] + 1)
            self.current_collection['dimension'][-1]['k'] = 0

    # Name: set_next_memory_avail
    # This function will update the new memory available to avoid
    # override from other memory sets
    #
    def set_next_memory_avail(self):
        self.program_engine.memory_direction += self.R
        self.R = 1
