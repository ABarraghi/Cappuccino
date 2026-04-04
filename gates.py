# gates.py
# Define logic gate behavior in an Object-Oriented fashion

class Gate:
    instance_counter = 0

    def __init__(self):
        # Assign a unique instance name and increment the global counter
        self.inst_name = f"U{Gate.instance_counter}"
        Gate.instance_counter += 1

    def __str__(self):
        return "Base Gate class method reached\n"

class Buffer(Gate):
    def __init__(self, in_wire, out_wire):
        super().__init__()
        self.in_wire = in_wire
        self.out_wire = out_wire

    def __str__(self):
        # assign statements do not take module instance names
        if self.in_wire != self.out_wire:
            return f"assign {self.out_wire} = {self.in_wire};\n"
        else:
            return ""

class Inv(Gate):
    def __init__(self, in_wire, out_wire):
        super().__init__()
        self.in_wire = in_wire
        self.out_wire = out_wire
        
    def __str__(self):
        return f"inv1$ {self.inst_name} (.out({self.out_wire}), .in({self.in_wire}));\n"

class Xor(Gate):
    def __init__(self, in_wire_0, in_wire_1, out_wire):
        super().__init__()
        self.in_wire_0 = in_wire_0
        self.in_wire_1 = in_wire_1
        self.out_wire = out_wire
        
    def __str__(self):
        return f"xor2$ {self.inst_name} (.out({self.out_wire}), .in0({self.in_wire_0}), .in1({self.in_wire_1}));\n"

class Xnor(Gate):
    def __init__(self, in_wire_0, in_wire_1, out_wire):
        super().__init__()
        self.in_wire_0 = in_wire_0
        self.in_wire_1 = in_wire_1
        self.out_wire = out_wire
        
    def __str__(self):
        return f"xnor2$ {self.inst_name} (.out({self.out_wire}), .in0({self.in_wire_0}), .in1({self.in_wire_1}));\n"

#Assume that NAND and NOR gates have less than or equal to 4 inputs (i.e. use the standard gates library)
class Nand(Gate):
    def __init__(self, out_wire):
        super().__init__()
        self.in_wires = {}
        self.out_wire = out_wire
        
    def __str__(self):
        if len(self.in_wires) == 2:
                return f'nand2$ {self.inst_name} (.out({self.out_wire}), .in0({self.in_wires["in_wire_0"]}), .in1({self.in_wires["in_wire_1"]}));\n'
        elif len(self.in_wires) == 3:
                return f'nand3$ {self.inst_name} (.out({self.out_wire}), .in0({self.in_wires["in_wire_0"]}), .in1({self.in_wires["in_wire_1"]}), .in2({self.in_wires["in_wire_2"]}));\n'
        elif len(self.in_wires) == 4:
                return f'nand4$ {self.inst_name} (.out({self.out_wire}), .in0({self.in_wires["in_wire_0"]}), .in1({self.in_wires["in_wire_1"]}), .in2({self.in_wires["in_wire_2"]}), .in3({self.in_wires["in_wire_3"]}));\n' 
 
class Nor(Gate):
    def __init__(self, out_wire):
        super().__init__()
        self.in_wires = {}
        self.out_wire = out_wire
        
    def __str__(self):
        if len(self.in_wires) == 2:
                return f'nor2$ {self.inst_name} (.out({self.out_wire}), .in0({self.in_wires["in_wire_0"]}), .in1({self.in_wires["in_wire_1"]}));\n'
        elif len(self.in_wires) == 3:
                return f'nor3$ {self.inst_name} (.out({self.out_wire}), .in0({self.in_wires["in_wire_0"]}), .in1({self.in_wires["in_wire_1"]}), .in2({self.in_wires["in_wire_2"]}));\n'
        elif len(self.in_wires) == 4:
                return f'nor4$ {self.inst_name} (.out({self.out_wire}), .in0({self.in_wires["in_wire_0"]}), .in1({self.in_wires["in_wire_1"]}), .in2({self.in_wires["in_wire_2"]}), .in3({self.in_wires["in_wire_3"]}));\n' 

# Assumes state name is the out_wire 
class Dff(Gate):
    def __init__(self, in_wire, out_wire):
        super().__init__()
        self.in_wire = in_wire
        self.out_wire = out_wire
        
    def __str__(self):
        return f"dff$ {self.out_wire}_dff (.clk(clk), .d({self.in_wire}), .q({self.out_wire}), .qbar(), .r(res), .s(set));\n"
