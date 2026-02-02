# wire_list.py
# Class that holds a global list of wires used in the circuit
# And keeps track of wire "staleness" 
# -> wires that were already assigned to an input 

class WireList:
    wires = []
    size = 0
    def_counter = 0 #default wire name counter

    def __str__(self):
        assgn_str = "wire"
        for i in range(WireList.size):
            assgn_str += f" {WireList.wires[i]}"
            
            if i < (WireList.size-1):
                assgn_str +=","

        assgn_str += ";\n\n"
        return assgn_str
    
    def add_wire(self, name=None):
        if name is None:
            name = f"w{WireList.def_counter}"
            WireList.def_counter += 1

        WireList.wires.append(name)
        WireList.size += 1
   
    def pop_wire(self):
       WireList.def_counter -= 1
       WireList.size -= 1
       WireList.wires.pop()

    def peek(self):
        return WireList.wires[WireList.size-1]


