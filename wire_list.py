# wire_list.py
# Class that holds a global list of wires used in the circuit
# And keeps track of wire "staleness" 
# -> wires that were already assigned to an input 

class WireList:
    def __init__(self):
        self.size = 0
        self.def_counter = 0 #default wire name counter
        self.wires = []

    def __str__(self):
        assgn_str = "wire"
        for i in range(self.size):
            assgn_str += f" {self.wires[i]}"
            
            if i < (self.size-1):
                assgn_str +=","

        assgn_str += ";\n"
        return assgn_str

    def add_wire(self, name=None):
        if name is None:
            name = f"w{self.def_counter}"
            self.def_counter += 1

        self.wires.append(name)
        self.size += 1

    def peek(self):
        return self.wires[self.size-1]


